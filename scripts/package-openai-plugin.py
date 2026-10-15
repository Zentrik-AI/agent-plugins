#!/usr/bin/env python3
"""Package the adapter for Zentrik's existing OpenAI directory listing."""
import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True, type=Path)
args = parser.parse_args()
repo = Path(__file__).resolve().parent.parent
adapter = repo / 'com.openai/zentrik'
output = args.output.resolve()
if output.suffix != '.zip' or output.is_relative_to(adapter):
    parser.error('Output must be a ZIP outside the adapter source directory.')
apps = json.loads((adapter / '.app.json').read_text())['apps']
if set(apps) != {'zentrik'} or set(apps['zentrik']) != {'id'}:
    parser.error('Expected the existing single registered Zentrik app mapping.')
app_id = apps['zentrik']['id']
if not app_id.startswith('asdk_app_'):
    parser.error('Expected a registered asdk_app_ identity.')
adapter_manifest = json.loads((adapter / '.codex-plugin/plugin.json').read_text())
manifest = {
    '$schema': 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
    **{key: value for key, value in adapter_manifest.items()
       if key not in ('apps', 'skills', 'mcpServers', 'interface')},
    'extensions': {
        **adapter_manifest.get('extensions', {}),
        'com.openai': {
            **adapter_manifest.get('extensions', {}).get('com.openai', {}),
            'interface': adapter_manifest['interface'],
        },
    },
}
# Preserve the published listing identity; the CLI marketplace keeps "zentrik".
manifest['name'] = 'app-' + app_id.removeprefix('asdk_app_')
interface = manifest['extensions']['com.openai']['interface']
interface['shortDescription'] = 'Evidence for product decisions'
interface['supportURL'] = 'https://zentrik.ai/contact'
# Include the existing endpoint explicitly: legacy release ZIPs can omit it,
# but the current portal rejects an update that would remove its MCP server.
mcp = {
    '$schema': 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json',
    'mcpServers': {'zentrik': {
        'type': 'streamable-http',
        'url': 'https://zentrik.ai/mcp/chatgpt',
        'extensions': {'com.openai': {'auth': {'type': 'oauth'}}},
    }},
}
output.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(output, 'w', ZIP_DEFLATED) as package:
    package.writestr('plugin.json', json.dumps(manifest, indent=2) + '\n')
    package.writestr('mcp.json', json.dumps(mcp, indent=2) + '\n')
    for source in sorted(adapter.rglob('*')):
        if not source.is_file():
            continue
        relative = source.relative_to(adapter).as_posix()
        if relative.startswith(('assets/', 'skills/')):
            package.write(source, relative)
    for name in ('LICENSE', 'NOTICE'):
        package.write(repo / name, name)
print(f'Packaged {manifest["name"]} {manifest["version"]}: {output}')
