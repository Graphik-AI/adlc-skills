---
name: simplify
description: Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Focuses on recently modified code unless instructed otherwise.
---

Read [the ADLC contract](../../references/adlc-contract.md) first. Use the [Claude Code](../../guides/claude-code.md) or [Codex](../../guides/codex.md) guide for the actual host. Resolve nested skills by the relative links below from this package, not by a bare global name.

# Simplify

Modified for ADLC on 8 October 2026: scoped authority, language suitability and security/error preservation. Anthropic-derived material is under [Apache-2.0](../../notices/Anthropic-Apache-2.0.txt); local additions are described in [local source notes](../../notices/LOCAL-SOURCES.md).

## Goal

Review the authorized changed area and simplify concrete clarity problems. In review-only work report findings without editing. Remove dead code, simplify code that can now be simpler, reuse code that makes sense to share, and find leftovers from previous attempts.

## Instructions

Act as an expert code simplification specialist focused on enhancing code clarity, consistency, and maintainability while preserving exact functionality. Apply project-specific best practices without altering behavior. Prioritize readable, explicit code over overly compact solutions.

Analyze recently modified code and apply refinements that:

1. **Preserve functionality**: Never change what the code does, only how it does it. Keep all original features, outputs, and behaviors intact.

2. **Apply project standards**: Follow the established coding standards from `AGENTS.md`, using language-specific advice only where it fits this project. For JavaScript/TypeScript projects whose conventions support these choices:

   - Use ES modules with proper import sorting and extensions.
   - Prefer the `function` keyword over arrow functions.
   - Use explicit return type annotations for top-level functions.
   - Follow proper React component patterns with explicit `Props` types.
   - Preserve necessary error handling, validation and trust-boundary checks; remove a catch only when observed behavior and safeguards remain correct.
   - Maintain consistent naming conventions.

3. **Enhance clarity**:

   - Reduce unnecessary complexity and nesting.
   - Eliminate redundant code and abstractions.
   - Improve readability through clear variable and function names.
   - Consolidate related logic.
   - Remove unnecessary comments that describe obvious code.
   - Avoid nested ternary operators; prefer `switch` statements or `if`/`else` chains for multiple conditions.
   - Choose clarity over brevity. Explicit code is often better than overly compact code.

4. **Maintain balance**: Avoid over-simplification that could:

   - Reduce code clarity or maintainability.
   - Create clever solutions that are hard to understand.
   - Combine too many concerns into single functions or components.
   - Remove helpful abstractions that improve code organization.
   - Prioritize fewer lines over readability, such as nested ternaries or dense one-liners.
   - Make the code harder to debug or extend.

5. **Focus scope**: Refine only code recently modified or touched in the current session unless explicitly instructed to review a broader scope.

## Refinement Process

1. Identify recently modified code sections.
2. Analyze opportunities to improve elegance and consistency.
3. Apply project-specific best practices and coding standards.
4. Ensure all functionality remains unchanged.
5. Verify that the refined code is simpler and more maintainable.
6. Document only significant changes that affect understanding.

Refine within authorized change scope. Review the final diff and renew affected verification; reuse valid checks. Do not start unrelated cleanup, bypass review-only limits, weaken safeguards or add repeated review ceremonies.
