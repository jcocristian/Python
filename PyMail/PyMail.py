import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class PyMail():
    def __init__(self,  host, port, user, passwd):
        self.host = host
        self.port = int(port)
        self.user = user
        self.passwd = passwd

    def Contas(self, lista):
        x = str(lista).split(',')
        l1 = []
        for i in range(0, len(x)):
            l1.append((x[i]).strip().lower())
        return l1

    def SendMail(self, dest, titulo, msg, caminho, anexo):
        contas = self.Contas(dest)
        for exec in range(0, len(contas)):
            user = self.user
            server = smtplib.SMTP(self.host, self.port)
            server.ehlo()
            server.starttls()
            server.login(self.user, self.passwd)
            message = f'{msg}'
            email_msg = MIMEMultipart()
            email_msg['From'] = self.user
            email_msg['To'] = f'{contas[exec]}'
            email_msg['Subject'] = f'{titulo}'
            if caminho != '' and anexo != '':
                try:
                    email_msg.attach(MIMEText(message, 'plain'))
                    anexo = f'{anexo}'
                    caminho = f'{caminho}'
                    attachment = open(caminho, 'rb')
                    att = MIMEBase('application', 'octet-stream')
                    att.set_payload(attachment.read())
                    encoders.encode_base64(att)
                    att.add_header('Content-Disposition', f'attachment; filename= {anexo}')
                    attachment.close()
                    email_msg.attach(att)
                except FileNotFoundError:
                    print('O arquivo de anexo não foi encontrado.')
            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            server.quit()
PyMail('smtp.server.com', '587', 'meuemail@domain.com', 'minhasenha').SendMail('amigo1@, amigo2@, amigo3@', 'E-mail Python', 'Email enviado da ferramenta Python.\nBy Jonas Oliveira', '', '')  # Sem anexo
PyMail('smtp.server.com', '587', 'meuemail@domain.com', 'minhasenha').SendMail('amigo1@, amigo2@, amigo3@', 'E-mail Python', 'Email enviado da ferramenta Python.\nBy Jonas Oliveira', 'D:\Anexo.txt', 'Anexo.txt')  # Com anexo
# A classe PyMail recebe o "host", "porta", "usuário" e senha. E o método SendMail() os destinos (separados por vírgula), o Título do e-mail, a Mensagem, o caminho (com o arquivo) e o arquivo. Caso o e-mail não tenha anexo, deixa os 2 campos finais vazios.
