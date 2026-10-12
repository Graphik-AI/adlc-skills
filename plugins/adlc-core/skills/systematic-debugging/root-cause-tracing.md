# Root-cause tracing

Use backward tracing when a failure appears deep in a call chain or a test creates unexpected shared state. Follow the [ADLC contract](../../references/adlc-contract.md), especially scope, safe evidence and cleanup authority.

## Trace from the observation

1. Identify the failing operation and its actual inputs without exposing sensitive values. Distinguish the observed side effect from the explanation.
2. Find its caller, the value it supplied and the assumptions it made. Continue to the earliest relevant point where expected and actual state diverge.
3. Compare that origin with a working route or fixture. Test the suspected difference in a disposable environment when safe.
4. Fix the supported cause when authorized, and check the observed failure again. Add a boundary guard only when it protects a real invariant or distinct access path.

For example, an operation intended for a disposable workspace might receive an empty path because a fixture was read before setup completed. Check the actual library's empty-path behavior, the caller and fixture lifecycle; do not assume the working directory from a stack trace alone. Correct fixture timing and reject an invalid target at the operation's trusted boundary. A label such as `NODE_ENV=test` is not proof that a path is disposable.

## Instrument only the missing evidence

If source and existing logs cannot establish the call chain, add temporary instrumentation within edit authority. Record an allowlisted operation marker, safe error code, or a boolean such as `targetProvided`. Capture only the necessary redacted stack frames; paths and stack text can themselves contain sensitive details. Do not log entire arguments, environment maps, payloads, home directories or credentials. Keep temporary debug output out of the final change unless it is justified product behavior.

Use the repository's documented test runner and selectors. Do not prescribe npm for an unrelated project. Capture only relevant redacted output and preserve command failures; a filtering pipeline must not turn a failing test into a claimed pass.

## Identify test pollution safely

When a test passes alone but fails after others, first compare fixture cleanup, shared resources, ordering and concurrency. Use the test runner's supported subset/order controls to narrow the predecessor set in a disposable checkout with synthetic fixtures. Check the suspected pair and full affected group; the last test before a failure is not necessarily the polluter. Do not delete shared artifacts, reset a developer checkout or run an uninspected helper to force a clean state.

If the origin cannot be observed safely, record the missing boundary and a bounded next check. A symptom-level mitigation may be justified, but must remain labelled as such. A past upstream debugging example is not evidence that this package or the current application is verified.
