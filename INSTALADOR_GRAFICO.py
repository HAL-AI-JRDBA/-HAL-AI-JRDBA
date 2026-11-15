#!/usr/bin/env python3
"""HALL-AI V44 guided installer: folder selector, no command copying."""
import os, sys, subprocess, threading, platform
from pathlib import Path
try:
 import tkinter as tk
 from tkinter import ttk, filedialog, messagebox
except ImportError:
 print('Graphical interface unavailable. Use INSTALAR_WINDOWS.bat or INSTALAR_LINUX.sh for text-mode installation.')
 raise SystemExit(2)
BASE=Path(__file__).resolve().parent
OS='windows' if os.name=='nt' else 'linux' if sys.platform.startswith('linux') else 'unsupported'
LANGS={'Português':'pt','English':'en','Español':'es','Français':'fr','Deutsch':'de','中文':'zh'}
WORDS={
 'pt':('Escolha o destino','Procurar...','Instalar arquivos da HALL','Instalação concluída','Pasta já contém arquivos. Escolha uma pasta vazia.','Confirme a instalação na pasta selecionada?','Preparando instalação...','Falha na instalação','Sistema detectado','Idioma','Instalar dependências depois','Fechar'),
 'en':('Choose destination','Browse...','Install HALL files','Installation completed','Folder is not empty. Choose an empty folder.','Install into the selected folder?','Preparing installation...','Installation failed','Detected system','Language','Install dependencies afterwards','Close'),
 'es':('Elegir destino','Examinar...','Instalar archivos HALL','Instalación completada','La carpeta no está vacía. Elija una vacía.','¿Instalar en la carpeta seleccionada?','Preparando instalación...','Error de instalación','Sistema detectado','Idioma','Instalar dependencias después','Cerrar'),
 'fr':('Choisir le dossier','Parcourir...','Installer les fichiers HALL','Installation terminée','Le dossier doit être vide.','Installer dans le dossier choisi ?','Préparation...','Échec de l’installation','Système détecté','Langue','Installer les dépendances ensuite','Fermer'),
 'de':('Zielordner wählen','Durchsuchen...','HALL-Dateien installieren','Installation abgeschlossen','Der Zielordner muss leer sein.','In den ausgewählten Ordner installieren?','Installation wird vorbereitet...','Installationsfehler','Erkanntes System','Sprache','Abhängigkeiten danach installieren','Schließen'),
 'zh':('选择安装目录','浏览...','安装 HALL 文件','安装完成','请选择空目录。','确定安装到选定目录吗？','准备安装...','安装失败','检测到的系统','语言','随后安装依赖','关闭')}
root=tk.Tk();root.title('HALL-AI V44 | Installer');root.geometry('675x370');root.minsize(600,330)
frame=ttk.Frame(root,padding=24);frame.pack(fill='both',expand=True)
ttk.Label(frame,text='HALL-AI  V44',font=('Segoe UI',19,'bold')).pack(anchor='w')
ttk.Label(frame,text='Windows / Linux  •  Local Ollama  •  Experimental installer').pack(anchor='w',pady=(1,18))
langvar=tk.StringVar(value='Português');destvar=tk.StringVar(value=str(Path.home()/'HALL_AI'/'HALL_V44_D'))
info=ttk.Label(frame);info.pack(anchor='w',pady=5)
line=ttk.Frame(frame);line.pack(fill='x',pady=5)
langlabel=ttk.Label(line);langlabel.pack(side='left');combo=ttk.Combobox(line,values=list(LANGS),textvariable=langvar,state='readonly',width=17);combo.pack(side='left',padx=12)
label=ttk.Label(frame);label.pack(anchor='w',pady=(12,2))
row=ttk.Frame(frame);row.pack(fill='x')
field=ttk.Entry(row,textvariable=destvar);field.pack(side='left',fill='x',expand=True)
def browse():
 p=filedialog.askdirectory(initialdir=str(Path.home()),mustexist=True)
 if p:destvar.set(p)
choose=ttk.Button(row,command=browse);choose.pack(side='left',padx=(8,0))
status=tk.StringVar(value='');ttk.Label(frame,textvariable=status,wraplength=610).pack(anchor='w',pady=(17,8))
progress=ttk.Progressbar(frame,mode='indeterminate');progress.pack(fill='x',pady=(0,13))
actions=ttk.Frame(frame);actions.pack(fill='x')
start=ttk.Button(actions);start.pack(side='left');close=ttk.Button(actions,command=root.destroy);close.pack(side='right')
def refresh(*_):
 w=WORDS[LANGS[langvar.get()]]
 info.configure(text=f'{w[8]}: {platform.system()} {platform.machine()}')
 langlabel.configure(text=w[9]+':');label.configure(text=w[0]);choose.configure(text=w[1]);start.configure(text=w[2]);close.configure(text=w[11])
langvar.trace_add('write',refresh)
def install():
 language=LANGS[langvar.get()];w=WORDS[language]
 if OS=='unsupported':messagebox.showerror('HALL-AI','This preview only supports Windows or Linux.');return
 dest=Path(destvar.get()).expanduser()
 if not destvar.get().strip():messagebox.showerror('HALL-AI',w[0]);return
 if dest.exists() and any(dest.iterdir()):messagebox.showerror('HALL-AI',w[4]);return
 if not messagebox.askyesno('HALL-AI',w[5]+'\n'+str(dest)):return
 start.configure(state='disabled');progress.start(10);status.set(w[6])
 command=[sys.executable,str(BASE/'install.py'),'--os',OS,'--lang',language,'--dest',str(dest),'--yes']
 def worker():
  try:
   p=subprocess.run(command,cwd=str(BASE),capture_output=True,text=True,errors='replace')
   error=(p.stderr+'\n'+p.stdout)[-2500:]
   def done():
    progress.stop();start.configure(state='normal')
    if p.returncode==0:
     status.set(w[3]+' — '+str(dest))
     after=('Windows: run 01_INSTALAR_HALL_D.bat inside the selected folder to install prerequisites and Ollama. Some original V44 scripts may still require D:.\n\nLinux: compatibility is experimental. Run PREPARAR_LINUX_EXPERIMENTAL.sh only after reviewing dependencies; voice and backend are unverified.' if language!='pt' else 'Windows: execute 01_INSTALAR_HALL_D.bat na pasta escolhida para preparar dependências e Ollama. Alguns scripts da V44 ainda podem depender da unidade D:.\n\nLinux: compatibilidade experimental; backend e voz ainda não validados. Revise as dependências antes de executar PREPARAR_LINUX_EXPERIMENTAL.sh.')
     messagebox.showinfo('HALL-AI',w[3]+'\n'+str(dest)+'\n\n'+after)
    else:
     status.set(w[7]);messagebox.showerror('HALL-AI',w[7]+'\n'+error)
   root.after(0,done)
  except Exception as ex:
   def fail():
    progress.stop();start.configure(state='normal');messagebox.showerror('HALL-AI',str(ex))
   root.after(0,fail)
 threading.Thread(target=worker,daemon=True).start()
start.configure(command=install);refresh()
root.mainloop()
