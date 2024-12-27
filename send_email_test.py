import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do email (para MailSlurper)
smtp_server = "localhost"  # Servidor local
smtp_port = 2500  # Porta padrão do MailSlurper
email_user = "andressagomesrp@gmail.com"  # Esse e-mail não precisa de autenticação com o MailSlurper
email_to = "andressacarolinebh68@gmail.com"  # Destinatário para o teste

# Criação do email
subject = "Teste de Email"
body = "Este é um email de teste enviado por um script Python."

# Configurar a mensagem
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_to
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Conexão com o servidor SMTP (MailSlurper)
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(email_user, email_to, msg.as_string())
        print("Email enviado com sucesso para o MailSlurper!")
except Exception as e:
    print(f"Erro ao enviar o email: {e}")
