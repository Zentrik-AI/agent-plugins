# Zentrik Agent Plugin

Connect an AI agent to the product decisions, customer evidence, and product context your team keeps in [Zentrik](https://zentrik.ai).

This package follows the [Agent Plugins](https://agent-plugins.org/) v1 format and bundles the production Zentrik Streamable HTTP MCP server with three reusable workflows:

- `brief-product-work` — ground planning, scoping, building, and review in the workspace's existing evidence.
- `set-up-product-workspace` — inspect a workspace and apply only an approved, bounded setup delta.
- `import-product-evidence` — capture supplied calls, tickets, reviews, feedback, or research with an approval step before writes.

The plugin contains no credentials and no local executable code. The MCP server authenticates through Zentrik OAuth, binds each connection to one selected workspace, and enforces the connected user's role and granted scopes.

## MCP endpoint

The bundled server is `https://zentrik.ai/mcp` over Streamable HTTP. Clients that do not load Agent Plugins can connect to that endpoint directly and complete the same OAuth flow.

## Codex CLI

This repository includes a Codex marketplace catalog for local, Git, and team distribution:

```bash
codex plugin marketplace add Zentrik-AI/agent-plugins
codex plugin add zentrik@zentrik-agent-plugins
```

The package at the repository root remains the portable Agent Plugins artifact. The `.agents/plugins/marketplace.json` file only gives Codex a catalog entry; it does not change the portable package format.

## Requirements

A Zentrik account and membership in at least one Zentrik workspace. No API key is required.

## Documentation and support

- MCP setup: https://zentrik.ai/docs/integrations/mcp
- MCP workflows: https://zentrik.ai/docs/integrations/mcp-workflows
- Support: support@zentrik.ai

## License

Apache-2.0. See the `LICENSE` file in the distribution repository.
