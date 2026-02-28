> ⚠️ CANONICAL SOURCE: This file is part of the LTC Effective Execution Engine (Utility Belt). DO NOT modify without User approval.

# UTILITY: PERSISTENT MEMORY (Knowledge Capture)

**Governance:** This command does not modify the planning doc or task status. See `.cursor/rules/context-preservation.mdc` Rule 6 for scope; `docs/ai/Effective_Execution_Manifesto.md` for the Utility Belt.

**PRIME DIRECTIVE:** Use this utility to store First-Principles, Venture Architecture rules, and strictly defined User's Requirements into the `@ai-devkit/memory` MCP server. Do not store generic, low-level coding advice.

## Step 1: Capture the Truth
Ask the User for:
- **Title:** A highly specific, 5-12 word title.
- **Core Truth:** The exact rule, principle, or context to remember.
- **Tags:** Relevant tags (e.g., `principle`, `architecture`, `requirements`).

## Step 2: Validate against Approach 2
Ensure the knowledge prioritizes Risk Management over pure Driving Output. If it is too vague, ask the User to clarify the deterministic boundaries.

## Step 3: Store & Confirm
1. **Call MCP:** Use `call_mcp_tool` with server `project-0-Integrated-Learning-Environment-ai-devkit-memory` and toolName `memory_storeKnowledge`. Arguments: `title` (required), `content` (required, markdown), optional `tags` array. See `docs/ai/implementation/ile-persistent-memory.md` §2.0 for the exact identifiers.
2. **If MCP returns UNKNOWN_TOOL:** Store the knowledge in the project instead: add it to `CLAUDE.md` §6 (e.g. under "Formatting pitfalls" or a new subsection) or to `docs/ai/implementation/ile-persistent-memory.md`, then confirm to the User what was stored and where. Tell the User the MCP tool name may need to be verified in Cursor's MCP/Tools list and updated in §2.0.
3. **Confirm to the User** exactly what was stored and how it will be used to protect future Execution Loops.
