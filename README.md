# Zentrik Agent Plugin

Connect an AI agent to the product decisions, customer evidence, and product context your team keeps in [Zentrik](https://zentrik.ai).

The repository root follows the [Agent Plugins](https://agent-plugins.org/) v1 format and bundles the production Zentrik Streamable HTTP MCP server with four reusable workflows:

- `brief-product-work`: ground planning, scoping, building, and review in the workspace's existing evidence.
- `set-up-product-workspace`: inspect a workspace and apply only an approved, bounded setup delta.
- `import-product-evidence`: capture supplied calls, tickets, reviews, feedback, or research with an approval step before writes.
- `manage-product-study`: plan, refine, and review a private Study through evidence-grounded draft findings.

The plugin contains no credentials and no local executable code. The MCP server authenticates through Zentrik OAuth, binds each connection to one selected workspace, and enforces the connected user's role and granted scopes.

## Choose the right surface

- Portable Agent Plugins clients load the repository root and connect to the broad `https://zentrik.ai/mcp` endpoint.
- Codex loads the OpenAI adapter at `com.openai/zentrik`, which maps to the registered Zentrik app available to ChatGPT and Codex. Both packages include the four workflows above; the app uses the narrower ChatGPT tool profile.
- MCP-only clients can connect directly to `https://zentrik.ai/mcp` and complete Zentrik OAuth.
- Server-to-server automation should use the versioned REST API at `/external/v1` with a scoped API key. The REST API is documented separately and is not bundled in this plugin.

See [SURFACES.md](SURFACES.md) for the compatibility contract and the reason the available tools differ by surface.

## Codex CLI

This repository includes a Codex marketplace catalog for local, Git, and team distribution:

```bash
codex plugin marketplace add Zentrik-AI/agent-plugins
codex plugin add zentrik@zentrik-agent-plugins
```

The repository root remains the portable artifact. The marketplace entry points Codex at the client adapter under `com.openai/zentrik`; this keeps OpenAI-specific metadata out of the portable manifest.

## Requirements

A Zentrik account and membership in at least one Zentrik workspace. No API key is required.

## Documentation and support

- Codex setup: https://zentrik.ai/docs/integrations/mcp-codex
- ChatGPT setup: https://zentrik.ai/docs/integrations/mcp-chatgpt
- MCP setup: https://zentrik.ai/docs/integrations/mcp
- MCP workflows: https://zentrik.ai/docs/integrations/mcp-workflows
- Support: support@zentrik.ai

## License

Apache-2.0. See the `LICENSE` file in the distribution repository.
