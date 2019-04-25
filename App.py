
from Mail import Mail
from Sort import Sort
from Files import Files
import os

def main():

    print('Searching file emails.json')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    files = Files(BASE_DIR)
    names = files.fetchEmailsFromJSON(files.existsEmailsJSON())
    print('Done...')
    print('Fetching file credentials.json')
    credentialsSender = files.fetchCredentialsFromJSON(files.existsCredentialsJSON())

    print('--------------  Welcome to Amigo Secreto V2 in Python  -----------------')

    sort = Sort()
    listOfNames = sort.createListOfNamesFrom(names)
    evenNames = sort.createEvenNamesFrom(listOfNames)
    mail = Mail(credentialsSender)
    subject = 'Party Digital'
    mail.createSession()
    print('Session created')
    mail.createFormatAndSend(names, evenNames, subject)
    print('Emails Sends')
    mail.closeSession()
    print('Done')


if __name__ == '__main__':
    main()

