import sys

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.ui.zapisz.clicked.connect(self.walidacja)
            self.show()

        def walidacja(self):
            numer = self.ui.nrtel.text()
            pesel = self.ui.pesel.text()
            imie = self.ui.imie.text()
            nazwisko = self.ui.nazwisko.text()
            if(len(numer) == 9):
                try:
                    numer = int(numer)
                except:
                    alert = QMessageBox()
                    alert.setWindowTitle("błąd")
                    alert.setInformativeText("nieprawidłowy numer telefonu")
                    alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                    alert.exec()
                    return False
            else:
                alert = QMessageBox()
                alert.setWindowTitle("błąd")
                alert.setInformativeText("za krótki numer telefonu")
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.exec()
                return False
            if (len(pesel) == 11):
                try:
                    pesel = int(pesel)
                except:
                    alert = QMessageBox()
                    alert.setWindowTitle("błąd")
                    alert.setInformativeText("nieprawidłowy PESEL")
                    alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                    alert.exec()
                    return False
            else:
                alert = QMessageBox()
                alert.setWindowTitle("błąd")
                alert.setInformativeText("za krótki pesel")
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.exec()
                return False

            waga = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            pesel = str(pesel)

            suma = int(pesel[0]) * waga[0] + int(pesel[1]) * waga[1] + int(pesel[2]) * waga[2] + int(pesel[3]) * waga[3] + int(pesel[4]) * waga[4] + int(pesel[5]) * waga[5] + int(pesel[6]) * waga[6] + int(pesel[7]) * waga[7] + int(pesel[8]) * waga[8] + int(pesel[9]) * waga[9]
            if suma >= 10:
                suma = (suma%10)
            if int(pesel[10])==10-suma%10:
                alert = QMessageBox()
                alert.setWindowTitle(":)")
                alert.setInformativeText("dodano")
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.exec()
                self.ui.lista.addItem(imie,nazwisko)
            else:
                alert = QMessageBox()
                alert.setWindowTitle("błąd")
                alert.setInformativeText("zły pesel")
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.exec()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
