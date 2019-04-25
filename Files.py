import os
import json

class Files:
    def __init__(self, BASE_DIR):
        self.BASE_DIR = BASE_DIR
    
    def existsEmailsJSON(self):
        filePathEmails = self.BASE_DIR + '/emails.json'
        if not os.path.exists(filePathEmails):
            raise IOError('File emails.json don\'t exists')
        return filePathEmails

    def fetchEmailsFromJSON(self, fileJSON):
        try:
            with open(fileJSON, "r") as read_file:
                dictEmails = json.load(read_file)
            return dictEmails
        except IOError as e:
            print(e)
    
    def existsCredentialsJSON(self):
        filePathCredentials = self.BASE_DIR + '/credentials.json'
        if not os.path.exists(filePathCredentials):
            raise IOError('File credentials.json don\'t exists!')
        return filePathCredentials

    def fetchCredentialsFromJSON(self, fileJSON):
        try:
            with open(fileJSON, "r") as read_file:
                credentials = json.load(read_file)
            return credentials
        except IOError as e:
            print(e)