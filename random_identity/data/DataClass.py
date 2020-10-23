from random_identity import identity
from PyQt5.QtWidgets import QMessageBox
from random import choice
import main_window as window
import os


class Data:
    def __init__(self):
        self.name = identity.full_name()
        self.birthday = identity.birthday()
        self.age = identity.age()
        self.number = identity.phone_number()
        self.nationality = identity.nationality
        self.address = identity.address()
        self.workplace = choice(identity.workers)
        self.email = identity.email_address()
        # FILE NAME
        self.file_name = ''

    def setupData(self, name, birth, age, phone, nation, workplace, email, address):
        name.setPlaceholderText(self.name)
        birth.setPlaceholderText(self.birthday)
        age.setPlaceholderText(str(self.age))
        phone.setPlaceholderText(self.number)
        nation.setPlaceholderText(self.nationality)
        workplace.setPlaceholderText(self.workplace)
        email.setPlaceholderText(self.email)
        self.file_name = self.email + '.txt'
        address.setPlaceholderText(self.address.replace("\n", "  "))

    def generateFile(self):
        path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = path_desktop + "\\FakeID\\" + self.file_name
        path = os.path.join(path_desktop + "/FakeID")

        if not os.path.isdir(path):
            os.mkdir(path)

        with open(file_path, "w") as file:
            file.write("[+] Name and surname: " + self.name + "\n")
            file.write("======================================\n")
            file.write("[+] Birthday: " + self.birthday + "\n")
            file.write("======================================\n")
            file.write("[+] Age: " + str(self.age) + "\n")
            file.write("======================================\n")
            file.write("[+] Phone number " + self.number + "\n")
            file.write("======================================\n")
            file.write("[+] Nationality: " + self.nationality + "\n")
            file.write("======================================\n")
            file.write("[+] Address: " + self.address + "\n")
            file.write("======================================\n")
            file.write("[+] Workplace: " + self.workplace + "\n")
            file.write("======================================\n")
            file.write("[+] E-mail: " + self.email + "\n")

        msg = QMessageBox()
        msg.setWindowTitle("File created")
        msg.setText("File has been created! ")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        msg.setInformativeText("The txt file has been created on desktop in directory 'FakeID' ")
        # msg.setDetailedText("")

        # msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()
