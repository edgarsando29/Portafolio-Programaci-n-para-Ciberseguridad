# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)
import argparse
from Func_cifrado_encrypt import crackeo, cifrado, descifrado
if __name__ == '__main__':
    
    description = """Selección de tarea:
    "cr" o "CR": Crackeo César
    "des" o "DES": Descifrado César
    "cif" o "CIF": Cifrado César

    Ejemplos de uso:
        + Mensaje ingresado por usuario:
            -msg [mensaje] -mod cr
            -msg [mensaje] -mod des -key [palabra llave]
            -msg [mensaje] -mod cif -key [palabra llave]"""
    parser = argparse.ArgumentParser(description='Crackeo de mensajes cifrado Cesar', epilog=description,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-msg', dest='msg', type=str,
                        help='Mensaje que se va a manipular (cifrar, descifrar o crackear)',
                        required=True)
    parser.add_argument('-mod', dest='mod', type=str,
                        help='Tipo de acción que hará, cifrar, descifrar o crackear',
                        required=True)
    parser.add_argument('-key', dest='key',
                        help='Palabra clave para cifrar o descifrar, según sea el caso')
    args = parser.parse_args()

mensaje = args.msg
tipo = args.mod
if args.key:
    llave = args.key

resultado = 0

if tipo == "cr" or tipo == "CR":
    try:
        print('Hacking...')
        crackeo(mensaje)
    except Exception as e:
        print("Error:", e)
elif tipo == "cif" or tipo == "CIF":
    try:
        cifrado(mensaje, llave)
    except Exception as e:
        print("Error:", e)
elif tipo == "des" or tipo == "DES":
    try:
        descifrado(mensaje, llave)
    except Exception as e:
        print("Error:", e)
else:
    print("Acción no existente")