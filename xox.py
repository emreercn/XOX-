import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import random

class XOX(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("xox_tasarim.ui",self)
        self.mn_cikis.triggered.connect(self.cikis)
        self.btn_0.clicked.connect(self.oyun)
        self.btn_1.clicked.connect(self.oyun)
        self.btn_2.clicked.connect(self.oyun)
        self.btn_3.clicked.connect(self.oyun)
        self.btn_4.clicked.connect(self.oyun)
        self.btn_5.clicked.connect(self.oyun)
        self.btn_6.clicked.connect(self.oyun)
        self.btn_7.clicked.connect(self.oyun)
        self.btn_8.clicked.connect(self.oyun)
        X = QInputDialog.getText(self,"İsim","X oyuncusu ismi: ")[0]
        self.lbl_isim_X.setText("X-"+X)
        O = QInputDialog.getText(self,"İsim","O oyuncusu ismi: ")[0]
        self.lbl_isim_O.setText("O-"+O)
        self.statusBar().showMessage("Oyuna X oyuncusu başlar", 3000)
        self.lbl_skor_X.setText("0")
        self.lbl_skor_O.setText("0")
        self.sıra = "X"
        self.t = ["" for i in range(9)]
        self.buton = [self.btn_0,self.btn_1,self.btn_2,
                      self.btn_3,self.btn_4,self.btn_5,
                      self.btn_6,self.btn_7,self.btn_8]
        for i in range(9):
            self.buton[i].setText("")

    def oyun(self):
        self.klik = int(self.sender().objectName()[4])
        if self.sıra == "X":
            if self.t[self.klik] != "":
                QMessageBox.information(self,"Uyarı","Burası oynandı!")
            else:
                self.t[self.klik] = "X"
                self.buton[self.klik].setText("X")
                self.kontrol()
        else:
            if self.t[self.klik] != "":
                QMessageBox.information(self,"Uyarı","Burası oynandı!")
            else:
                self.t[self.klik] = "O"
                self.buton[self.klik].setText("O")
                self.kontrol()

    def kontrol(self):
        if self.t[0]==self.t[1]==self.t[2] and self.t[1]!="":
            self.kazanan()
        elif self.t[3]==self.t[4]==self.t[5] and self.t[4]!="":
            self.kazanan()
        elif self.t[6]==self.t[7]==self.t[8] and self.t[7]!="":
            self.kazanan()
        elif self.t[0]==self.t[3]==self.t[6] and self.t[3]!="":
            self.kazanan()
        elif self.t[1]==self.t[4]==self.t[7] and self.t[4]!="":
            self.kazanan()
        elif self.t[2]==self.t[5]==self.t[8] and self.t[5]!="":
            self.kazanan()
        elif self.t[0]==self.t[4]==self.t[8] and self.t[4]!="":
            self.kazanan()
        elif self.t[2]==self.t[4]==self.t[6] and self.t[4]!="":
            self.kazanan()
        elif "" not in self.t:
            QMessageBox.information(self,"Sonuc","Berabere bitti!")
            self.karar()
        else:
            if self.sıra == "X":
                self.sıra = "O"
            else:
                self.sıra = "X"
            
    def kazanan(self):
        if self.sıra == "X":
            QMessageBox.information(self,"Sonuc",f"{self.lbl_isim_X.text()} kazandı!")
            self.lbl_skor_X.setText(str(int(self.lbl_skor_X.text())+1))
        else:
            QMessageBox.information(self,"Sonuc",f"{self.lbl_isim_O.text()} kazandı!")
            self.lbl_skor_O.setText(str(int(self.lbl_skor_O.text())+1))
        self.karar()

    def karar(self):
        yanıt = QMessageBox.question(self,"Devam","Devam etmek ister misiniz?",QMessageBox.Yes|QMessageBox.No)
        if yanıt == QMessageBox.Yes:
            for i in range(9):
                self.buton[i].setText("")
            if self.sıra == "X":
                self.sıra = "O"
            else:
                self.sıra = "X"
            self.t = ["" for i in range(9)]
            self.statusBar().showMessage(f"Oyuna {self.sıra} oyuncusu başlar", 3000)
        else:
            self.cikis()
    def cikis(self):
        yanıt = QMessageBox.question(self,"Çıkış","Çıkmak istediğinize emin misiniz?",QMessageBox.Yes|QMessageBox.No)
        if yanıt == QMessageBox.Yes:
            sys.exit()
        else:
            self.karar()

        

def main():
    uygulama = QApplication(sys.argv)
    pencere = XOX()
    pencere.show()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    main()