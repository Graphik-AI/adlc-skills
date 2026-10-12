# Condition-based waiting

Wait for the state that the task actually requires instead of guessing how long it takes. Follow the [ADLC contract](../../references/adlc-contract.md). Polling does not authorize repeated external, paid or production operations.

Use the framework's existing bounded assertions or event subscription when suitable. For a small local synchronous state getter, [the bundled TypeScript example](condition-based-waiting-example.ts) provides dependency-free polling and event helpers. It accepts a structural event source supplied by the caller; no upstream application types or plugin are required.

```typescript
import { waitFor } from './condition-based-waiting-example.ts';

// getResult is the application's existing synchronous, side-effect-free getter.
const result = await waitFor(() => getResult(), 'local result', 1000);
```

The generic helper treats only `undefined` as pending; `false`, `0`, `null` and an empty string are completed values. For a boolean condition, return `true` when ready and `undefined` while pending. Event helpers wait for a matching type, a count or a predicate. Their descriptions must be safe labels, never credentials or customer data.

Choose a deadline appropriate to the actual local operation. The helper checks immediately, reads fresh state between bounded delays and rejects on timeout. Getter and predicate exceptions reject the returned promise rather than escaping a timer callback. Timeouts cannot interrupt a blocking synchronous getter; getters must return promptly. Async/network checks need the owning framework's cancellation and timeout support, not this example. The example uses platform timers and a monotonic clock; it is instruction support, not an installed service or an automatic project dependency.

For execution without a project TypeScript toolchain, this package was checked with Node 22.22.3 native type stripping. Use the package verification instructions for the tested command; support for an arbitrary older runtime is not implied.

When testing debounce, throttling or an actual elapsed-time requirement, a controlled clock may be the right seam. Establish the trigger, advance the specified interval and assert behavior at the relevant boundary. A documented timing requirement differs from sleeping until a flaky test happens to pass. Preserve the original failure and reassess the hypothesis instead of extending timeouts until a test turns green.
