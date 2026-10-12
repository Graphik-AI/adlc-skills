// Adapted from the Superpowers waiting example for adlc-core on 2026-10-08.
// Removed application-specific imports; callbacks are synchronous and side-effect-free.

export interface EventSource<Event> {
  getEvents(threadId: string): readonly Event[];
}

/** Resolve the first defined result, or reject on callback error or deadline. */
export async function waitFor<Value>(
  condition: () => Value | undefined,
  description: string,
  timeoutMs = 5000,
): Promise<Value> {
  if (!Number.isFinite(timeoutMs) || timeoutMs < 0 || timeoutMs > 2_147_483_647) {
    throw new RangeError('timeoutMs must be finite and between 0 and 2147483647');
  }
  const deadline = performance.now() + timeoutMs;
  let firstCheck = true;
  while (true) {
    if (!firstCheck && performance.now() >= deadline) {
      throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
    }
    firstCheck = false;
    const result = condition();
    if (result !== undefined) return result;
    const remainingMs = deadline - performance.now();
    if (remainingMs <= 0) {
      throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
    }
    await new Promise<void>((resolve) => setTimeout(resolve, Math.min(10, remainingMs)));
  }
}

export function waitForEvent<Event extends { type: string }>(
  source: EventSource<Event>,
  threadId: string,
  eventType: Event['type'],
  timeoutMs = 5000,
): Promise<Event> {
  return waitForEventMatch(source, threadId, (event) => event.type === eventType, 'event type', timeoutMs);
}

export async function waitForEventCount<Event extends { type: string }>(
  source: EventSource<Event>,
  threadId: string,
  eventType: Event['type'],
  count: number,
  timeoutMs = 5000,
): Promise<Event[]> {
  if (!Number.isSafeInteger(count) || count < 0) {
    throw new RangeError('count must be a nonnegative safe integer');
  }
  return waitFor(() => {
    const events = source.getEvents(threadId).filter((event) => event.type === eventType);
    return events.length >= count ? events : undefined;
  }, 'event count', timeoutMs);
}

export function waitForEventMatch<Event>(
  source: EventSource<Event>,
  threadId: string,
  predicate: (event: Event) => boolean,
  description: string,
  timeoutMs = 5000,
): Promise<Event> {
  return waitFor(() => source.getEvents(threadId).find(predicate), description, timeoutMs);
}
