# Como publicar os arquivos navegáveis no GitHub

**Importante:** esta pasta é candidata à publicação; 48 arquivos precisam de revisão manual. Publicar esta versão pode deixar módulos incompletos. Não substitui o ZIP da Release já publicada.

## Pelo Git for Windows (recomendado)

1. Instale o Git for Windows: https://git-scm.com/downloads/win
2. Abra PowerShell em uma pasta de trabalho e execute:

```powershell
git clone https://github.com/HAL-AI-JRDBA/-HAL-AI-JRDBA.git
cd .\-HAL-AI-JRDBA
```

3. Extraia este ZIP em uma pasta temporária no seu computador e copie seu conteúdo **para dentro da pasta clonada**, preservando o arquivo `LICENSE` e a pasta `.git` do repositório.
4. Confira as alterações antes de enviar:

```powershell
git status
git add README.md .gitignore SECURITY_AND_PUBLICATION.md COMO_PUBLICAR_NO_GITHUB_PT_BR.md docs HALL_V44_D PUBLICACAO_VERIFICACAO.txt
git status
git commit -m "docs: add multilingual guides and V44 source candidate"
git push origin main
```

Caso alguma operação reporte conflito, não force o push: verifique o erro e reconcilie a versão local com o remoto. Você precisa estar autenticado no GitHub pelo Git Credential Manager ou equivalente.

## Resultado esperado

O código aparecerá navegável em `HALL_V44_D/`, e os guias em `docs/`. O GitHub manterá o botão de download da Release em **Releases**. Os arquivos automáticos `Source code (zip)` passarão a refletir o conteúdo do branch associado à versão/tag, observando que a tag `v44.0` existente não muda automaticamente após um novo commit.
