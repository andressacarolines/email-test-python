import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do email
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_user = "andyougamers@gmail.com"
email_password = "games2024"  # Use um App Password ou senha específica para o app
email_to = "andressacarolinebh68@gmail.com" # andressa

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
    # Conexão com o servidor SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Segurança TLS
        server.login(email_user, email_password)
        server.sendmail(email_user, email_to, msg.as_string())
        print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o email: {e}")
