# HALL-AI V44 Universal Installer Preview

Choose a target **Windows drive/directory** or a **Linux directory**, then stage the HALL V44 files. Run `INSTALAR_WINDOWS.bat` on Windows (requires Python 3.11) or `bash INSTALAR_LINUX.sh` on Linux (requires Python 3.11). Both are interactive.

Windows setup is adapted to remove the fixed `D:\AI_HALL\HALL_V44_D` location check. Additional Windows modules may still contain legacy paths. Linux includes an experimental virtual environment, dependency preparation and server launcher, **not** guaranteed full functionality. No end-to-end OS validation has been performed. Installation may download dependencies and Ollama models, so initial installation requires internet access. Core usage is designed for local operation.

See `LEIA_PRIMEIRO_PT.md` for details.
