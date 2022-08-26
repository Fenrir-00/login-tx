import os,sys,time,subprocess

while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")

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
  ubicacion=os.path.abspath(os.getcwd)
  ubicacion1=ubicacion
   ubicacion1=ubicacion1+"/pass.txt"
  with open("ubicacion1","r",encoding = 'utf-8') as datos:
   for linea in datos:
    var2= linea
  datos.close()
  var2=var2.rstrip()
  if var2 == "Jwjjwjdlslakansnns":
   with open("pass.txt","w",encoding = 'utf-8') as datos:
    datos.write("fenrir")
    datos.close()
   ubicacion=os.path.abspath(os.getcwd())
 # var1(f"echo python {ubicacion}/login.py")
 # salto = "\n"
 # fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
 # fd.write(f"{salto}{var1}")
 #fd.close()
  with open("pass.txt","r",encoding = 'utf-8') as datos:
   for linea in datos:
    var2= linea
  datos.close()
  var2=var2.rstrip()
  banner()
  version()
 # var3("echo python /data/data/com.termux/files/home/login/login.py")
 # salto = "\n"
 # fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
 # fd.write(f"{salto}{var3}")
 # fd.close()
  var = input(f"{color.verde}INTRODUCE LA CONTRADEÑA >> {color.fin}")
  if var == var2:
   banner()
   print(f"{color.verde}CONTRASEÑA CORRECTA{color.fin}")
  else:
   incorrecto()
   login()  
 except:
     login()
login()
