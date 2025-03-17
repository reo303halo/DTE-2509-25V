
def saveToFile(firstname, lastname, email, password):
    userFile = open("userfile.txt", "a")
    userFile.write(f'Firstname: {firstname}\n')
    userFile.write(f'Lastname: {lastname}\n')
    userFile.write(f'Email: {email}\n')
    userFile.write(f'Password: {password}\n\n')
    userFile.close()