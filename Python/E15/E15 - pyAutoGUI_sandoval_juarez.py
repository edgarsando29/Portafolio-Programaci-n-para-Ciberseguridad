import pyautogui
import time
import os
#input()
os.system("cls")
for c in range(0, 2, 1):

    opcion = int(input("Qué universo de súperheores prefieres? 1)Marvel 2)DC 3)Ambos 4)Ninguno: "))
    mensaje = input("Escribe la frase o dicho: ")
    hora = '''OPCIONES
a)8am
b)9am
c)10am
d)11am
e)12pm
f)1pm
g)2pm
h)3pm
i)4pm
j)5pm
k)6pm
l)Después de las 7
    Cuál es la mejor hora para comer pastel?: '''

    horaop = input(hora)
    correo = input("Escribe una cuenta de correo falsa: ")

# Dependiendo de la preferencia de los radiobutton, se dará clic en
# localización específica
    time.sleep(3)
    if opcion == 1:
        pyautogui.click(x=337, y = 444, clicks = 1)
    elif opcion == 2:
        pyautogui.click(x=337, y = 482, clicks = 1)
    elif opcion == 3:
        pyautogui.click(x=337, y = 523, clicks = 1)
    elif opcion == 4:
        pyautogui.click(x=337, y = 564, clicks = 1)
    else:
        print("Opción no válida para preferencia de universo de súperheores.")
        exit()


    pyautogui.press('tab')
    pyautogui.press('tab')

# Escribir la frase en el formulario
    pyautogui.typewrite(mensaje)
    pyautogui.press('tab')
    pyautogui.press('tab')

# Escoger la hora en la lista, presionando la tecla de flecha hacia abajo
    if horaop == 'a':
        pyautogui.press("Down")
    elif horaop == 'b':
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif horaop == 'c':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif horaop == 'd':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif horaop == 'e':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif horaop == 'f':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    elif horaop == 'g':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif horaop == 'h':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif horaop == 'i':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif horaop == 'j':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif horaop == 'k':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")

    elif horaop == 'l':
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
        pyautogui.press("Down")
    else:
        print("Opción de hora para comer pastel no válida, intente de nuevo")
        exit()
    pyautogui.press('tab')
    pyautogui.press('tab')

# Escribir correo en formulario
# Dividir correo por el arroba    
    correo = correo.split("@")
# EScribir primera parte de correo en formulario
    pyautogui.typewrite(correo[0])

# Escribir arroba con función hotkey
    pyautogui.hotkey('ctrl', 'alt', 'q')#@@

# Escribir segunda parte de correo en formulario
    pyautogui.typewrite(correo[1])
    time.sleep(3)

# Tabulador y enter para enviar la respuesta
    pyautogui.press('tab')
    pyautogui.press('enter')

# Esperar a que cargue la nueva pantalla para enviar otra respuesta
    time.sleep(3)

# Solo se intentará enviar otra respuesta si se ha enviado solo una
    if c < 1:
        pyautogui.click(x=364, y = 456, clicks = 1)
    c = c+1