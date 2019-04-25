import smtplib, ssl
from email.mime.text import MIMEText
from email.header import Header

class Mail:

    def __init__(self, credentialsSender):
        self.senderEmail = credentialsSender['email']
        self.passwordSender = credentialsSender['password']
    
    def createSession(self):
        smtpServer = 'smtp.gmail.com'
        port = '587'
        try:
            contextSSL = ssl.create_default_context()
            self.smtpObj = smtplib.SMTP(smtpServer, port)
            self.smtpObj.starttls(context=contextSSL)
            self.smtpObj.login(self.senderEmail, self.passwordSender)
        except Exception as e:
            if "Username and Password not accepted" in str(e.args[1]):
                raise ValueError('Credentials Invalid')
            else:
                print(e)
    def createFormatAndSend(self, dictAll, listOfEvenNames, subject):
        for names in listOfEvenNames:
            body = "Jovem Padawan, você tem a honra de participar de um Amigo Oculto Digital\nVocê foi o Escolhido para Presentar uma Pessoa Especial Cujo o Nome é: {}".format(names[0], names[1])
            message = MIMEText(body, 'plain', 'utf-8')
            message['Subject'] = Header(subject, 'utf-8')
            message['From'] = Header('Olá {}'.format(names[0]), 'utf-8')
            message['To'] = Header(dictAll['{}'.format(names[1])], 'utf-8')
            emailDestinationCleaned = cleaned_email(dictAll[names[0]])
            self.sendEmail(emailDestinationCleaned, message.as_string())

    def sendEmail(self, destinationEmail, message):
        try:
            self.smtpObj.sendmail(
                self.senderEmail,
                destinationEmail,
                message
                )
        except Exception as e:
            print(e)
    def closeSession(self):
        try:
            self.smtpObj.quit()
            return True
        except Exception as e:
            print(e)
            return False

    def cleaned_email(self, emailSource):
        if not '@' in emailSource:
            raise ValueError('Invalid Email', emailSource)
        domainEmail = emailSource.split('@')[1]
        if not '.' in domainEmail:
            raise ValueError('Invalid Email', emailSource)
        return emailSource.lower()
   
