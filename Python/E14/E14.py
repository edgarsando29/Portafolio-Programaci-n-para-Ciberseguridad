import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
from email.mime.multipart import MIMEMultipart

sender_email = input("Ingrese su correo electronico: ")
password = getpass.getpass("Ingrese la contraseña: ")
receiver_email = input("Ingrese el correo de destino: ")
subject = input("Ingresa el asunto de tu mensaje: ")
text = input("Ingresa el Mensaje: ")
ruta = input("Ingresa la ruta de la imagen: ")

try: 
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    message["body"] = text

    message.attach(MIMEText(text, "plain"))

    with open(ruta,'rb') as attachment:
        part = MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {ruta}")
    message.attach(part)
    text = message.as_string()

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("outlook.office365.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    
except Exception as e:
    print("Error", e)
