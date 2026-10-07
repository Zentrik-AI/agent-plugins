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
manifest = json.loads((adapter / '.codex-plugin/plugin.json').read_text())
# Preserve the published listing identity; the CLI marketplace keeps "zentrik".
manifest['name'] = 'app-' + app_id.removeprefix('asdk_app_')
manifest.pop('apps', None)
manifest['mcpServers'] = './.mcp.json'
manifest['interface']['shortDescription'] = 'Evidence for product decisions'
manifest['interface']['supportURL'] = 'https://zentrik.ai/contact'
server = {'mcpServers': {'zentrik': {'url': 'https://zentrik.ai/mcp/chatgpt'}}}
output.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(output, 'w', ZIP_DEFLATED) as package:
    for source in sorted(adapter.rglob('*')):
        if not source.is_file():
            continue
        relative = source.relative_to(adapter).as_posix()
        if relative == '.codex-plugin/plugin.json':
            package.writestr(relative, json.dumps(manifest, indent=2) + '\n')
        elif relative.startswith(('assets/', 'skills/')):
            package.write(source, relative)
    package.writestr('.mcp.json', json.dumps(server, indent=2) + '\n')
    for name in ('LICENSE', 'NOTICE'):
        package.write(repo / name, name)
print(f'Packaged {manifest["name"]} {manifest["version"]}: {output}')
