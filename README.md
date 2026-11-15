# HALL-AI V44 — International source publication candidate

**AJDS Informatica LTDA • Brazil**  
**Status: experimental pre-release; not production validated.**

HALL-AI is a local-first enterprise AI platform targeting Windows with Ollama, agent workflows, RAG, voice, and database assistance. Its local inference profile does not require a paid cloud model API after first-time downloads. Optional external integrations may require network access.

## Start here

- [Português — instalação](docs/INSTALL_PT_BR.md)
- [English — installation](docs/INSTALL_EN.md)
- [Español — instalación](docs/INSTALL_ES.md)
- [Français — installation](docs/INSTALL_FR.md)
- [Deutsch — Installation](docs/INSTALL_DE.md)
- [中文 — 安装说明](docs/INSTALL_ZH.md)
- [Release V44 download](https://github.com/HAL-AI-JRDBA/-HAL-AI-JRDBA/releases/tag/v44.0)
- [Hugging Face demonstration](https://huggingface.co/spaces/HAL-AI-JRDBA/README) (interface preview, not the local engine)
- [Security / publication limitations](SECURITY_AND_PUBLICATION.md)

## Source tree

`HALL_V44_D/` — V44 Windows distribution source and installer scripts.  
`HALL_V44_D/db_erp_oracle_workspace_web_agentic_rag_full/` — application and supporting modules.  
`docs/` — international installation guides.  
`PUBLICACAO_VERIFICACAO.txt` — files withheld pending manual credential review.

## Important completeness limitation

This is a **source publication candidate, not a fully verified or complete source distribution**. The conservative automated scan excluded **48 files** for manual review, including essential backend and frontend modules. Some features **will not run from this archive alone**. The downloadable V44 pre-release ZIP is separate, and its code has not been comprehensively audited. Do not represent the repository candidate as functionally complete until exclusions are resolved and tests pass.

## Requirements

The supplied Windows V44 setup targets **Windows 10 22H2 or Windows 11 x64**, uses a managed **Python 3.11** environment, a local portable **Ollama** installation, and a `D:\AI_HALL\HALL_V44_D` path. A Windows machine with ~20 GB free on D: is recommended by the V44 instructions; models and optional tools require extra storage. The first installation uses internet downloads.

## License

Intended project license: Apache License 2.0. Third-party dependencies, assets, and LLM weights follow their own licenses. Ownership and license compatibility have not been fully audited. Existing repository LICENSE should be preserved.
