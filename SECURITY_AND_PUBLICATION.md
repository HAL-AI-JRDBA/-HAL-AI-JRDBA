# Security and publication readiness

This source archive is a candidate. It has NOT undergone a complete credential, dependency, or licensing audit or a Windows runtime test.

- 48 files were withheld by a conservative pattern check; see `PUBLICACAO_VERIFICACAO.txt`. They may include false positives and important application entry points.
- Do not upload `.env` files, real credentials, customer files, model caches, downloaded binaries, logs, or local databases.
- Treat `.bat` and `.ps1` installers as executable code. Review their download sources and hashes before using them.
- Database examples must use non-production accounts and test environments.
- The V44 official download archive is a pre-release and is not production certified.
- GitHub `Source code (zip)` is generated from the repository tree; it does not automatically contain the separately uploaded Release asset.
- Do not force-push over existing commits or delete the repository LICENSE.

## Verification before a stable release

1. Manually review the 48 withheld files and restore safe ones.
2. Scan for tokens and credentials, check package licenses and redistributed assets.
3. Install on a clean supported Windows x64 PC and exercise startup, local Ollama, voice activation/deactivation, chat, RAG, and non-production SQL access.
4. Publish test results and an explicit feature matrix.
