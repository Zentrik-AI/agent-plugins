# Zentrik agent surfaces

Zentrik projects one authorization and product model into several interfaces. They share the same workspace permissions and source records, but they are not intended to expose identical tool sets.

| Surface | Distribution | Endpoint | Authentication | Intended use |
| --- | --- | --- | --- | --- |
| Portable Agent Plugin | This repository's root `plugin.json` | `https://zentrik.ai/mcp` | Zentrik OAuth | Client-neutral skills plus the broad product-graph MCP tool set |
| ChatGPT and Codex app | OpenAI Plugins Directory and `com.openai/zentrik` | `https://zentrik.ai/mcp/chatgpt` | Zentrik OAuth | A smaller reviewed set for evidence search, evidence capture, and bounded planning actions |
| Direct MCP | Client MCP settings | `https://zentrik.ai/mcp` | Zentrik OAuth | Broad interactive access for MCP clients that do not install plugins |
| Claude Code plugin | [`Zentrik-AI/claude-plugins`](https://github.com/Zentrik-AI/claude-plugins) | `https://zentrik.ai/mcp` | Zentrik OAuth | Claude-specific packaging of the same client-neutral workflows |
| External REST API | Application code or automation | `https://zentrik.ai/external/v1` | Scoped Zentrik API key | Stable server-to-server integration contracts |

## Compatibility contract

- The portable package owns client-neutral metadata, MCP configuration, and reusable skills for the broad generic MCP endpoint.
- `com.openai/zentrik` is an independently versioned OpenAI-specific adapter. Its `.app.json` maps to Zentrik's existing registered app, and it includes only skills whose required tools are part of the reviewed OpenAI snapshot.
- The ChatGPT and Codex app profile is deliberately narrower than generic MCP. A tool appearing in generic MCP or REST does not automatically make it part of the reviewed app profile.
- Portable skills may lead the OpenAI adapter when generic MCP already supports them. Add a skill to the adapter only in the same reviewed release as its required OpenAI tools.
- REST resources are versioned integration contracts. MCP tools are conversational operations and can combine several underlying product actions.
- All interactive surfaces preserve the connected user's workspace membership, role, and granted OAuth scopes. The package contains no credentials.

The public guides are the source of truth for installation and user-facing availability:

- [ChatGPT](https://zentrik.ai/docs/integrations/mcp-chatgpt)
- [Codex](https://zentrik.ai/docs/integrations/mcp-codex)
- [Direct MCP](https://zentrik.ai/docs/integrations/mcp)
- [External API](https://zentrik.ai/docs/api)
