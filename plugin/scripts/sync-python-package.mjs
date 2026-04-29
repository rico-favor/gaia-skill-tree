import { cpSync, mkdirSync, rmSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const pluginRoot = resolve(__dirname, '..');
const repoRoot = resolve(pluginRoot, '..');
const sourceRoot = resolve(repoRoot, 'src', 'gaia_cli');
const targetRoot = resolve(pluginRoot, 'python', 'gaia_cli');

rmSync(targetRoot, { recursive: true, force: true });
mkdirSync(resolve(pluginRoot, 'python'), { recursive: true });
cpSync(sourceRoot, targetRoot, { recursive: true });
