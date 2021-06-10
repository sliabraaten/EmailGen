#todo handle file not matching
#todo handle edge cases
#todo check file for security
#todo auto lookup passwords and generate links
#todo auto send emails
#todo document code
#todo add cross platform support with file structure
import os.path


class User(object):
    firstname = ""
    lastname = ""
    username = ""
    password = ""
    passwordUrl = ""

    def __init__(self, name):
        temparr = name.split(" ")
        if len(temparr) == 3:
            self.firstname = temparr[0]
            self.lastname = temparr[1]
            self.username = self.firstname[0] + self.lastname
            self.passwordUrl = temparr[2]


def make_user(name):
    user = User(name)
    return user


users = []

#EXPECTING FIRSTNAME LASTNAME PASSWORD URL
userPath = input("Enter path for user file")
userPath = os.path.dirname(__file__) + "/" + userPath + ".txt"
#EXPECTING FULL NAME WITH %FIRSTNAME, %LASTNAME, %USERNAME, %PASSLINK AS KEYS
emailPath = os.path.dirname(__file__) + "/" + input("Enter path for text file") + ".txt"
destinationPath = os.path.dirname(__file__) + "/" + input("Enter destination file path") + ".txt"

with open(userPath) as file:
    Users = file.readlines()
file.close()

repWords = ("%FIRSTNAME%", "%LASTNAME%", "%USERNAME%", "%PASSWORD%", "%PASSLINK%")

with open(destinationPath, 'w') as dest:
    for userName in Users:
        tempUser = make_user(userName)
        newWords = \
            (tempUser.firstname, tempUser.lastname, tempUser.username, tempUser.password, tempUser.passwordUrl)
        lastLine = ""
        with open(emailPath) as email:
            for emailLine in email:
                for rep, new in zip(repWords, newWords):
                    destTempLine = emailLine.replace(rep, new)
                    if not("%" in destTempLine) and lastLine != destTempLine:
                        dest.write(destTempLine)
                    lastLine = destTempLine
        email.close()

        dest.write("\n\n\n")

dest.close()

