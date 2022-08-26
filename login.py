import os,sys,time

while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")

while True:
 try:
   import requests
   break
 except ModuleNotFoundError:
  os.system("pip install requests")

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{color.fin}""")

def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.6                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """ 
 lol_py(texto)
 print()

def cabecera()
 os.system("clear")
 print(f"""{color.cyan}

██╗      █████╗  ██████╗ ██╗███╗  ██╗      ████████╗██╗  ██╗
██║     ██╔══██╗██╔════╝ ██║████╗ ██║      ╚══██╔══╝╚██╗██╔╝
██║     ██║  ██║██║  ██╗ ██║██╔██╗██║█████╗   ██║    ╚███╔╝
██║     ██║  ██║██║  ╚██╗██║██║╚████║╚════╝   ██║    ██╔██╗
███████╗╚█████╔╝╚██████╔╝██║██║ ╚███║         ██║   ██╔╝╚██╗
╚══════╝ ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚══╝         ╚═╝   ╚═╝  ╚═╝""")
def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝
██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    
def login():
 try:
  ubicacion=os.path.abspath(os.getcwd())
  ubicacion1=ubicacion
  ubicacion1 = ubicacion1+"/pass.txt"
  with open(ubicacion1,"r",encoding = 'utf-8') as datos:
   for linea in datos:
    var2= linea
  datos.close()
  var2=var2.rstrip()
  if var2 == "Jwjjwjdlslakansnns":
   with open(ubicacion1,"w",encoding = 'utf-8') as datos:
    datos.write("fenrir")
    datos.close()
   ubicacion=os.path.abspath(os.getcwd())
   var1="/login.py"
   salto = "\n"
   fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
   fd.write(f"{salto}'python '{ubicacion}{var1}")
   fd.close()
  with open(ubicacion1,"r",encoding = 'utf-8') as datos:
   for linea in datos:
    var2= linea
  datos.close()
  var2=var2.rstrip()
  cabecera()
  version()
  print(f"""{color.morado}
QUE TE GUSTARIA HACER{color.verde}
[1]PONER CONTRASEÑA
[2]CAMBIAR CONTRASEÑA
""")
  var5= input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
  if var5 =="1":
   banner()
   var = input(f"{color.verde}INTRODUCE LA CONTRASEÑA >> {color.fin}")
   if var == var2:
    banner()
    print(f"{color.verde}CONTRASEÑA CORRECTA{color.fin}")
    print()
  elif var5 =="2":
   banner()
   var = input(f"{color.verde}INTRODUCE LA CONTRASEÑA >> {color.fin}")
   if var == var2:
    banner()
    var = input(f"{color.verde}INTRODUCE LA NUEVA CONTRASEÑA >> {color.fin}")
    with open(ubicacion1,"w",encoding = 'utf-8') as datos:
     datos.write(var)
     datos.close()
    print(f"{color.amarillo}TU NUEVA CONTRASEÑA ES: {var}{color.fin}")
   else:
    login()
  elif var5 =="99":
   banner()
   r= requests.get("https://raw.githubusercontent.com/Fenrir-00/login-tx/main/version.txt")
   r=r.text
   print(r)
   if r == "version=1.0\n":
    baner()
   else:
    login()
  else:
   incorrecto()
   login()  
 except:
  login()
login()
