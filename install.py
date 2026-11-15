#!/usr/bin/env python3
'HALL-AI V44: preparador multiplataforma (stdlib Python).'
import argparse, os, platform, shutil, subprocess, sys, zipfile, re, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
TRANSLATIONS={
 'pt':('Selecione o sistema: 1 Windows / 2 Linux','Diretório de instalação (pode escolher qualquer unidade/pasta)','Instalação preparada.','O Linux é experimental: a aplicação V44 foi criada para Windows.'),
 'en':('Select system: 1 Windows / 2 Linux','Install directory (choose any drive/folder)','Files prepared.','Linux is experimental: V44 was developed for Windows.'),
 'es':('Seleccione el sistema: 1 Windows / 2 Linux','Directorio de instalación (cualquier unidad/carpeta)','Archivos preparados.','Linux es experimental: V44 fue diseñada para Windows.'),
 'fr':('Choisissez le système : 1 Windows / 2 Linux',"Répertoire d’installation (lecteur/dossier au choix)",'Fichiers préparés.','Linux expérimental : V44 a été conçue pour Windows.'),
 'de':('System wählen: 1 Windows / 2 Linux','Installationsverzeichnis (beliebiges Laufwerk/Ordner)','Dateien vorbereitet.','Linux ist experimentell: V44 wurde für Windows entwickelt.'),
 'zh':('选择系统：1 Windows / 2 Linux','安装目录（可选择磁盘和目录）','文件已准备好。','Linux 为实验性支持：V44 原本针对 Windows 开发。'),
}

def patch_windows(home):
    'Patch only the two original Windows setup scripts, preserving all other sources.'
    setup=home/'setup'
    envfile=setup/'ambiente_hall_d.ps1'
    setupfile=setup/'hall_d.ps1'
    t=envfile.read_text(encoding='utf-8-sig')
    t=t.replace("if ([IO.Path]::GetFullPath($HallHome).TrimEnd([char]'\\') -ine 'D:\\AI_HALL\\HALL_V44_D') {", "if (-not (Test-Path -LiteralPath (Join-Path $HallHome 'db_erp_oracle_workspace_web_agentic_rag_full') -PathType Container)) {")
    t=t.replace("[IO.DriveInfo]::new('D:\\').AvailableFreeSpace", "[IO.DriveInfo]::new([IO.Path]::GetPathRoot([IO.Path]::GetFullPath($HallHome))).AvailableFreeSpace")
    t=t.replace("$env:HOMEDRIVE='D:'; $env:HOMEPATH=$profileD.Substring(2)", "$env:HOMEDRIVE=[IO.Path]::GetPathRoot($profileD).TrimEnd('\\'); $env:HOMEPATH=$profileD.Substring([IO.Path]::GetPathRoot($profileD).Length - 1)")
    envfile.write_text(t,encoding='utf-8-sig')
    h=setupfile.read_text(encoding='utf-8-sig')
    # Hardcoded D: in this file is only messaging, so do not change program behavior.
    setupfile.write_text(h,encoding='utf-8-sig')

def safe_extract(archive,dest):
    root=dest.resolve()
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            if item.is_dir():continue
            name=item.filename.replace('\\','/')
            parts=Path(name).parts
            if not parts or '..' in parts or name.startswith('/') or re.match(r'^[A-Za-z]:',name):
                raise ValueError('Unsafe entry: '+name)
            out=(dest/name).resolve()
            if not out.is_relative_to(root):raise ValueError('Unsafe path: '+name)
            out.parent.mkdir(parents=True,exist_ok=True)
            with z.open(item) as src, out.open('wb') as dst:shutil.copyfileobj(src,dst)

def diagnostic_linux(home):
    app=home/'db_erp_oracle_workspace_web_agentic_rag_full'
    checks={
      'python':sys.version.split()[0],
      'python_3_11':sys.version_info[:2]==(3,11),
      'ollama_executable':shutil.which('ollama'),
      'backend_main':(app/'web_app/backend/main.py').exists(),
      'requirements':(app/'requirements.txt').exists(),
      'windows_only_scripts_present':len(list(home.rglob('*.bat'))),
      'note':'Compatibility not established: Windows-specific Python imports, OS calls, voice drivers, Oracle Client and paths may need adaptations.'
    }
    (home/'LINUX_DIAGNOSTICO.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False),encoding='utf8')
    return checks

def write_linux_scripts(home):
    app='db_erp_oracle_workspace_web_agentic_rag_full'
    launcher='''#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE/'''+app+'''"
if [[ ! -x "$HERE/.venv-linux/bin/python" ]]; then
 echo "Ambiente não preparado. Execute primeiro: bash PREPARAR_LINUX_EXPERIMENTAL.sh"; exit 2
fi
export OLLAMA_HOST="127.0.0.1:11435"
export OLLAMA_BASE_URL="http://127.0.0.1:11435"
export HALL_OLLAMA_URL="$OLLAMA_BASE_URL"
export HALL_PUBLIC_URL="http://127.0.0.1:8000"
exec "$HERE/.venv-linux/bin/python" -m uvicorn web_app.backend.main:app --host 127.0.0.1 --port 8000
'''
    prep='''#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
command -v python3.11 >/dev/null || { echo "Instale Python 3.11";exit 2; }
command -v ollama >/dev/null || { echo "Instale Ollama para Linux";exit 2; }
python3.11 -m venv "$HERE/.venv-linux"
"$HERE/.venv-linux/bin/python" -m pip install --upgrade pip
"$HERE/.venv-linux/bin/python" -m pip install -r "$HERE/'''+app+'''/requirements.txt" uvicorn
printf "Dependências básicas instaladas; execute INICIAR_LINUX_EXPERIMENTAL.sh para testar.\\n"
'''
    for name,body in [('PREPARAR_LINUX_EXPERIMENTAL.sh',prep),('INICIAR_LINUX_EXPERIMENTAL.sh',launcher)]:
        p=home/name;p.write_text(body,encoding='utf8');p.chmod(0o755)

def main():
    p=argparse.ArgumentParser(description='HALL-AI V44 Windows/Linux installer')
    p.add_argument('--lang',choices=list(TRANSLATIONS));p.add_argument('--os',choices=['windows','linux']);p.add_argument('--dest');p.add_argument('--yes',action='store_true');p.add_argument('--install-deps',action='store_true',help='Run supported dependency installer (Windows legacy or Linux experimental)')
    args=p.parse_args()
    lang=args.lang or (input('Language / Idioma [pt/en/es/fr/de/zh] (pt): ').strip().lower() or 'pt')
    if lang not in TRANSLATIONS:lang='pt'
    words=TRANSLATIONS[lang]
    actual='windows' if os.name=='nt' else 'linux' if sys.platform.startswith('linux') else 'other'
    desired=args.os or (('windows' if input(words[0]+' [1]: ').strip()!='2' else 'linux'))
    if desired!=actual:raise SystemExit('Execute o instalador dentro do sistema escolhido. Detected: '+actual+'; selected: '+desired)
    if actual not in ('windows','linux'):raise SystemExit('Unsupported OS: '+actual)
    default=(str(Path.home()/'HALL_AI'/'HALL_V44_D') if actual=='linux' else str(Path.home()/'HALL_AI'/'HALL_V44_D'))
    dest=Path(args.dest or (input(words[1]+' ['+default+']: ').strip() or default)).expanduser().resolve()
    home=dest
    if home.exists() and any(home.iterdir()):
        raise SystemExit('Destination not empty; choose a new empty directory. No files changed: '+str(home))
    free=shutil.disk_usage(home.parent if home.parent.exists() else Path.home()).free
    if free<10*1024**3:print('WARNING: Less than 10 GB free. Model downloads may require more storage.')
    print('System:',desired,'| Target:',home)
    if not args.yes and input('Proceed? [y/N]: ').strip().lower() not in ('y','yes','s','sim'):return
    home.mkdir(parents=True,exist_ok=True)
    # Extract into a temporary directory in the selected destination, then move actual app tree.
    stage=home/'_tmp_unpack'
    try:
        stage.mkdir()
        safe_extract(ROOT/'HALL_V44_PAYLOAD.zip',stage)
        src=stage/'HALL_V44_D'
        if not src.is_dir():raise RuntimeError('Missing HALL_V44_D directory in payload')
        for item in src.iterdir():shutil.move(str(item),str(home/item.name))
        # Root readme/license are not duplicated if existing
        for name in ('README.md','PUBLICACAO_LEIA_PRIMEIRO.txt'):
            f=stage/name
            if f.exists():shutil.copy2(f,home/name)
    finally:shutil.rmtree(stage,ignore_errors=True)
    if desired=='windows':
        patch_windows(home)
        instructions='Run 01_INSTALAR_HALL_D.bat to install / 02_INICIAR_HALL_D.bat to start. Windows x64 only. Some legacy modules may still assume drive D:. Backup first.'
        if args.install_deps:
            if not args.yes:raise SystemExit('Explicit --yes required with --install-deps')
            run=subprocess.run(['cmd.exe','/c',str(home/'01_INSTALAR_HALL_D.bat')],cwd=str(home))
            if run.returncode:raise SystemExit(run.returncode)
    else:
        write_linux_scripts(home)
        checks=diagnostic_linux(home)
        instructions=words[3]+' Check LINUX_DIAGNOSTICO.json; run PREPARAR_LINUX_EXPERIMENTAL.sh for dependencies, then INICIAR_LINUX_EXPERIMENTAL.sh. Ollama must be installed separately.'
        if args.install_deps:
            if not args.yes:raise SystemExit('Explicit --yes required with --install-deps')
            run=subprocess.run(['bash',str(home/'PREPARAR_LINUX_EXPERIMENTAL.sh')],cwd=str(home))
            if run.returncode:raise SystemExit(run.returncode)
    (home/'INSTALACAO_UNIVERSAL_STATUS.txt').write_text('OS='+desired+'\nPATH='+str(home)+'\n'+instructions+'\n',encoding='utf8')
    print(words[2]);print(instructions)
if __name__=='__main__':main()
