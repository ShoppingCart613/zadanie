import sys

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
        isValid = True
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.ui.zapisz.clicked.connect(self.zapisz_do_listy)
            self.ui.zapiszplik.clicked.connect(self.zapisz_do_pliku)
            self.show()

        def walidacja(self):
            alert = QMessageBox()
            alert.setWindowTitle("błąd")
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            numer = self.ui.nrtel.text()
            pesel = self.ui.pesel.text()
            imie = self.ui.imie.text()
            nazwisko = self.ui.nazwisko.text()
            if(len(numer) == 9):
                try:
                    numer = int(numer)
                except:
                    alert.setInformativeText("nieprawidłowy numer telefonu")
                    alert.exec()
                    self.isValid = False
                    return False
            else:
                alert.setInformativeText("za krótki numer telefonu")
                alert.exec()
                self.isValid = False
                return False
            if (len(pesel) == 11):
                try:
                    int(pesel)
                except:
                    alert.setInformativeText("nieprawidłowy PESEL")
                    alert.exec()
                    self.isValid = False
                    return False
            else:
                alert.setInformativeText("za krótki pesel")
                alert.exec()
                self.isValid = False
                return False

            waga = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            pesel = str(pesel)

            suma = int(pesel[0]) * waga[0] + int(pesel[1]) * waga[1] + int(pesel[2]) * waga[2] + int(pesel[3]) * waga[3] + int(pesel[4]) * waga[4] + int(pesel[5]) * waga[5] + int(pesel[6]) * waga[6] + int(pesel[7]) * waga[7] + int(pesel[8]) * waga[8] + int(pesel[9]) * waga[9]
            if suma >= 10:
                suma = (suma%10)
            if int(pesel[10])!=10-suma%10:
                alert.setInformativeText("zły pesel")
                alert.exec()
                self.isValid = False
                return False

        def zapisz_do_listy(self):
            self.walidacja()
            if self.isValid == True:
                imie = self.ui.imie.text()
                nazwisko = self.ui.nazwisko.text()
                nazwa = imie + " " + nazwisko
                self.ui.lista.addItem(nazwa)

        def zapisz_do_pliku(self):
            self.walidacja()
            if self.isValid == True:
                imie = self.ui.imie.text()
                nazwisko = self.ui.nazwisko.text()
                nazwa = imie + " " + nazwisko + "\n"
                with open("lista.txt","a") as file:
                    file.write(nazwa)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
