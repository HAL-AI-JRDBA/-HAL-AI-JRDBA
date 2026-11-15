# Instalador universal HALL-AI V44 — Preview

**Windows e Linux:** escolha a pasta ou unidade de instalação. Não exige o drive D: por padrão.

## Windows
Instale Python 3.11 64-bit e execute `INSTALAR_WINDOWS.bat`. Selecione o diretório, por exemplo `C:\HALL_AI\HALL_V44_D`, `D:\HALL_AI\HALL_V44_D` ou outra unidade. Depois, execute `01_INSTALAR_HALL_D.bat` dentro da pasta escolhida. O instalador Windows legado instala recursos Python/Ollama locais e pode baixar modelos pela internet. Recomenda-se instalar primeiro em pasta vazia, sem sobrescrever uma instalação anterior.

## Linux — experimental
Instale Python 3.11, Python venv e Ollama compatível com sua distribuição. Execute `bash INSTALAR_LINUX.sh`, escolha o destino como `/opt/hall-ai/HALL_V44_D` ou `~/hall-ai/HALL_V44_D`, depois confira `LINUX_DIAGNOSTICO.json`. Execute `bash PREPARAR_LINUX_EXPERIMENTAL.sh` para instalar dependências no ambiente virtual e `bash INICIAR_LINUX_EXPERIMENTAL.sh` para testar o servidor. **Não é uma versão Linux validada ou pronta para produção**: módulos de voz, automação, Oracle Thick e outras dependências Windows podem falhar.

## Importante
- Windows original tem rotinas específicas do Windows e downloads de binários Windows; a escolha de pasta não significa portabilidade completa.
- Não se deve executar o script `.bat` no Linux nem `.sh` no Windows.
- Não executamos testes ponta-a-ponta em Windows nem Linux nesta entrega.
- Não exponha a porta 8000 na internet sem autenticação e revisão de segurança.
- A licença dos modelos e dependências de terceiros deve ser conferida separadamente.
- Esta é uma evolução **experimental do instalador**, não uma atualização estável de todas as funções da HALL.
