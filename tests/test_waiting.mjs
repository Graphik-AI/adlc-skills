import assert from 'node:assert/strict';
import test from 'node:test';
import { waitFor, waitForEvent, waitForEventCount, waitForEventMatch } from '../plugins/adlc-core/skills/systematic-debugging/condition-based-waiting-example.ts';

const sleep = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));

test('waitFor preserves falsy completed values and checks immediately', async () => {
  for (const value of [false, 0, '', null]) {
    assert.equal(await waitFor(() => value, 'fixture', 0), value);
  }
});

test('event helpers read fresh state and preserve matching event data', async () => {
  const events = [{ type: 'OTHER', value: 0 }];
  const source = { getEvents: () => events };
  const byType = waitForEvent(source, 'fixture', 'DONE', 1000);
  const byCount = waitForEventCount(source, 'fixture', 'DONE', 2, 1000);
  const byPredicate = waitForEventMatch(source, 'fixture', (event) => event.value === 2, 'second result', 1000);
  events.push({ type: 'DONE', value: 1 }, { type: 'DONE', value: 2 });
  assert.deepEqual(await byType, events[1]);
  assert.deepEqual(await byCount, events.slice(1));
  assert.deepEqual(await byPredicate, events[2]);
  assert.deepEqual(await waitForEventCount({ getEvents: () => [] }, 'fixture', 'DONE', 0, 0), []);
});

test('deadline rejects and polling stops after rejection', async () => {
  let reads = 0;
  await assert.rejects(waitFor(() => { reads += 1; return undefined; }, 'absent fixture', 25), /Timeout waiting for absent fixture/);
  const stoppedAt = reads;
  await sleep(30);
  assert.equal(reads, stoppedAt);
  assert.ok(reads >= 1);
});

test('getter errors on a later poll reject without escaping a timer', async () => {
  const failure = new Error('synthetic getter failure');
  let reads = 0;
  await assert.rejects(waitForEvent({ getEvents() { if (++reads > 1) throw failure; return []; } }, 'fixture', 'DONE', 1000), (error) => error === failure);
  const stoppedAt = reads;
  await sleep(30);
  assert.equal(reads, stoppedAt);
});

test('predicate errors preserve the original failure', async () => {
  const failure = new Error('synthetic predicate failure');
  await assert.rejects(waitForEventMatch({ getEvents: () => [{ type: 'DONE' }] }, 'fixture', () => { throw failure; }, 'fixture', 1000), (error) => error === failure);
});

test('invalid limits reject before reading a source', async () => {
  const unexpectedRead = () => { throw new Error('must not read'); };
  for (const timeout of [-1, NaN, Infinity, 2_147_483_648]) {
    await assert.rejects(waitFor(unexpectedRead, 'fixture', timeout), RangeError);
  }
  for (const count of [-1, 0.5, NaN, Infinity]) {
    await assert.rejects(waitForEventCount({ getEvents: unexpectedRead }, 'fixture', 'DONE', count), RangeError);
  }
});
