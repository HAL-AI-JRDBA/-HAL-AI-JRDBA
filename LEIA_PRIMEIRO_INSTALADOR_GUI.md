# HALL-AI V44 — instalador com seleção de pasta

## Windows
1. Extraia **todo o ZIP** em uma pasta temporária.
2. Instale Python 3.11 (64 bits), com Tkinter e `py` habilitados.
3. Execute `ABRIR_INSTALADOR_WINDOWS.bat`.
4. Escolha o idioma e o destino. Clique **Instalar arquivos da HALL**.
5. Ao concluir, entre na pasta escolhida e execute `01_INSTALAR_HALL_D.bat` para preparar dependências e Ollama, e `02_INICIAR_HALL_D.bat` para iniciar. A V44 original ainda pode ter referências fixas à unidade D:. Confira os logs.

## Linux (experimental)
1. Instale Python 3.11, python3.11-tk e Ollama separadamente.
2. Extraia o ZIP e execute `bash ABRIR_INSTALADOR_LINUX.sh`.
3. Selecione idioma e diretório. A etapa GUI **extrai e prepara arquivos**; não garante funcionamento de voz/backend Linux.
4. Consulte `LINUX_DIAGNOSTICO.json`, `PREPARAR_LINUX_EXPERIMENTAL.sh` e `INICIAR_LINUX_EXPERIMENTAL.sh` na pasta escolhida.

**Limites:** não substitui instalação existente, não altera pastas não vazias, não instala Python automaticamente e não comprova compatibilidade completa em outro drive ou Linux. Não é uma release estável. Sem necessidade de copiar comandos. Downloads iniciais de dependências/modelos podem exigir internet; o objetivo é operação local posteriormente.
