import sys
from pyqtwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication ,QFileDialog ,QMessageBox
from AES import aes

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.Encrypt.clicked.connect(self.Encrypt_clicked)
        self.Decrypt.clicked.connect(self.Decrypt_clicked)
        self.Browse.clicked.connect(self.getfiles)
    def passwordVerify(self,password):
        if len(bytes(password,'utf-8'))==16:
            return True
        return False
    def Encrypt_clicked(self):
        filename=self.path.text()
        password=self.password.text()
        if not self.passwordVerify(password):
            alert_msg='Password invalid'
            reply = QMessageBox.critical(self, 'Error', alert_msg, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                return
        print(filename)
        print(password)
        alert_msg = "Are you sure you want to encrypt this folder:\n"+filename
        reply = QMessageBox.question(self, 'Message', alert_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            aes('d',filename,password)
        else:
            pass
    def Decrypt_clicked(self):
        filename=self.path.text()
        password=self.password.text()
        if not self.passwordVerify(password):
            alert_msg='Password invalid'
            reply = QMessageBox.critical(self, 'Error', alert_msg, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                return
        print(filename)
        print(password)
        dec=aes('e',filename,password)
        if dec==1:
            alert_msg='Password check failed'
            reply = QMessageBox.critical(self, 'Error', alert_msg, QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                return
    def getfiles(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName= QFileDialog.getExistingDirectory(self, "Select Directory")
        if fileName:
            self.path.setText(fileName)    
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())