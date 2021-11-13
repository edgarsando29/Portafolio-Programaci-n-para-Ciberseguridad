import subprocess
import os

def perfil_red():
    try:
        command = "powershell -ExecutionPolicy ByPass -File getconnection.ps1"
        print(command)
        print()
        subprocess.run(command)
    except Exception as e:
        print("Error:", e)

def perfil_firewall(perfil):
    try:    
        command = "powershell -ExecutionPolicy ByPass -File getfirewallprofile.ps1 -perfil "+perfil
        print(command)
        print()
        print("- - - - - - Info del Status del Perfil - - - - - -")
        subprocess.run(command)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    os.system("cls")
    menu ="""\t*****MENÚ*****
[1] Ver perfil de red actual
[2] Ver status perfil de Firewall
"""
    print(menu)
    respuesta = input("Seleccione una opción a buscar: ")
    while(respuesta == str() or respuesta.isalpha() or respuesta.isspace() or int(respuesta) < 1 or int(respuesta) > 2):
        print("Opción no válida.")
        respuesta = input("Seleccione una opción a buscar: ")
    if int(respuesta) == 1:
        perfil_red()

    elif int(respuesta) == 2:
        perfil = input("¿Qué Perfil quieres ver? (Public | Private): ")
        while(perfil != "Public" and perfil != "Private" and perfil != "public" and perfil != "private"):
            print("Perfil no encontrado, intente de nuevo.")
            perfil = input("¿Qué Perfil quieres ver? (Public, Private): ")
        perfil_firewall(perfil)
