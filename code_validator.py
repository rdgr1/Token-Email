import random
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

# Gerar código de ativação
code = "".join(str(random.randint(0, 9)) for _ in range(6))

# Configuração do servidor SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
from_mail = 'testeovaldo1@gmail.com'
server.login(from_mail, 'pjcp qklj xrah oqpp')

# Solicitar e-mail do destinatário
to_mail = input("Enter your best email: ")

# Definir o conteúdo HTML
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Código de Verificação</title>
</head>
<body style="font-family: Helvetica; margin: 0; padding: 0; background-color: white; color: #000;">
    <p style=" font-size: 20px; text-align: center; padding-right: 45%;color: black;"><strong>Olá ,</strong></p>
    <p style="text-align: center; padding-bottom: 2px; font-size: 16px;color: black;">
        Recebemos uma solicitação para gerar um código de verificação vinculado a este endereço de e-mail.</p>
    <table role="presentation" style="width: 100%; height: 100%; border-spacing: 0; border-collapse: collapse;">
        <tr>
            <td align="center" style="padding: 20px;">
                <table role="presentation" style="max-width: 400px; width: 100%; background-image: url('https://dev.luger-academia.com.br/imagens/fundo.png'); background-size: cover; background-position: center; background-repeat: no-repeat; padding: 30px; border-radius: 15px; box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);">
                    <tr>
                        <td align="center" style="padding-bottom: 20px;">
                            <img src="https://dev.luger-academia.com.br/imagens/brasfort-logo-01.png" alt="Brasfort Logo" style="width: 140px; margin-bottom: 7px;">
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="font-family: 'Roboto', sans-serif; font-size: 23px; font-weight: bold; color: #ffffff;">
                            Código de Ativação
                            <img src="https://dev.luger-academia.com.br/imagens/secure-svgrepo-com.svg" alt="" style="width: 40px; margin-bottom: -10px; filter: invert(120%)">
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding-top: 20px; padding-bottom: 10px; font-family: Helvetica; font-weight: 400; font-size: 16px; color: #ffffff;">
                            Seu código de verificação é:
                        </td>
                    </tr>
                    <tr>
                        <td align="center" style="padding-bottom: 20px;">
                            <table role="presentation" style="border-spacing: 12px; border-collapse: separate;">
                                <tr>
                                    <td style="background-color: #ffffff; padding: 10px; font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; font-size: 25px; border-radius: 15px; text-align: center;">{code[0]}</td>
                                    <td style="background-color: #ffffff; padding: 10px; font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; font-size: 25px; border-radius: 15px; text-align: center;">{code[1]}</td>
                                    <td style="background-color: #ffffff; padding: 10px; font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; font-size: 25px; border-radius: 15px; text-align: center;">{code[2]}</td>
                                    <td style="background-color: #ffffff; padding: 10px; font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; font-size: 25px; border-radius: 15px; text-align: center;">{code[3]}</td>
                                    <td style="background-color: #ffffff; padding: 10px; font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; font-size: 25px; border-radius: 15px; text-align: center;">{code[4]}</td>
                                    <td style="background-color: #ffffff; padding: 10px; font-family: Verdana, Geneva, Tahoma, sans-serif, sans-serif; font-size: 25px; border-radius: 15px; text-align: center;">{code[5]}</td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    <p style="text-align: center; margin-top: -10px; font-size: 14px; color: black;">Se você não fez essa <strong>solicitação</strong>, por favor, <strong>ignore este e-mail.</strong><br><br>Seu acesso permanece <strong>seguro </strong>e nenhuma ação adicional é <strong>necessária.</strong><br><br>
     Caso tenha sido <strong>você</strong>, utilize o <strong>código</strong> acima para continuar o <strong>processo de verificação.</strong><br><br>
        Agradecemos por sua <strong>atenção!</strong><br><br>
    <br> Atenciosamente, <strong>Brasfort</strong><br ><br></p>
    <p style="text-align: center;">
        <img src="https://dev.luger-academia.com.br/imagens/brasfort-logo-01.png" alt="Brasfort Logo" style="width: 140px; margin-left: 10%;margin-bottom: 7px;filter:invert(85%) sepia(90%) saturate(400%) hue-rotate(200deg) brightness(80%) contrast(105%); ">
    </p>
</body>
</html>
"""

# Configurar a mensagem
msg = EmailMessage()
msg['Subject'] = "Código de Ativação"
msg['From'] = from_mail
msg['To'] = to_mail
msg.set_content(html_content, subtype='html')

# Enviar o e-mail
server.send_message(msg)
server.quit()
