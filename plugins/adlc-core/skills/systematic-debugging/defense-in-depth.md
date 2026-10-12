# Defense in depth at real boundaries

Use this after identifying invalid input or an unsafe side effect. Follow the [ADLC contract](../../references/adlc-contract.md); a debugging fix does not authorize broad hardening or redesign.

Several checks can be justified when they protect different boundaries. Repeating the same validation at every call adds maintenance cost and does not make a defect impossible. Map the actual ways the operation can be reached, including alternate trusted callers and tests, before choosing where a check belongs.

| Boundary | Reason for a check | Evidence to collect |
| --- | --- | --- |
| Untrusted entry point | Reject malformed or disallowed inputs before acting. | Relevant invalid and valid cases; parameterized operations and safe error output. |
| Domain operation | Preserve an invariant that remains necessary for another valid entry route. | A caller bypassing the first entry still cannot violate that invariant. |
| Side-effect boundary | Limit a file, process or external operation to its authorized target. | Reject out-of-scope targets and accept the intended disposable fixture. |
| Diagnostic observation | Explain a failure without exposing sensitive state. | Only necessary allowlisted/redacted fields are retained. Logging is not an access control. |

For a filesystem operation, reject an empty target before resolution. If containment matters, use the platform's path APIs and the actual authorized root; a string prefix can incorrectly accept a sibling path. Account for symlinks and the gap between checking and using a path when that boundary is attacker-controlled. Reuse the project's established safe operation instead of inventing a universal path validator in a debugging patch. A temporary-directory name or test environment flag does not grant authority to mutate it.

Test the guarantee each added guard is intended to provide, including relevant rejected cases and the allowed path. Do not remove existing safeguards because a first check looks redundant; establish whether another route depends on them. Keep errors and logs free of full sensitive values. If stronger isolation is required but unavailable, describe the concrete remaining risk rather than asserting that the bug is impossible.
