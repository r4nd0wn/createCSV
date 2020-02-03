
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QTimer, QSettings, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton

class PersonInfo():
    def __init__(self, first_name, last_name, job_title, department):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.department = department

    def returnArray(self):
        return [self.first_name, self.last_name, self.job_title, self.department]

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.DataSets =[]
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ptextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptextEdit.setObjectName("CSV-Export")
        self.horizontalLayout_2.addWidget(self.ptextEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstname_2 = QtWidgets.QLabel(self.centralwidget)
        self.firstname_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.firstname_2.setObjectName("firstname_2")
        self.verticalLayout.addWidget(self.firstname_2, 0, QtCore.Qt.AlignTop)
        self.firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.firstname.setObjectName("firstname")
        self.verticalLayout.addWidget(self.firstname)
        self.lastname_2 = QtWidgets.QLabel(self.centralwidget)
        self.lastname_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lastname_2.setObjectName("lastname_2")
        self.verticalLayout.addWidget(self.lastname_2)
        self.lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lastname.setObjectName("lastname")
        self.verticalLayout.addWidget(self.lastname, 0, QtCore.Qt.AlignTop)
        self.jobtitle_2 = QtWidgets.QLabel(self.centralwidget)
        self.jobtitle_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.jobtitle_2.setObjectName("jobtitle_2")
        self.verticalLayout.addWidget(self.jobtitle_2)
        self.jobtitle = QtWidgets.QLineEdit(self.centralwidget)
        self.jobtitle.setObjectName("jobtitle")
        self.verticalLayout.addWidget(self.jobtitle)
        self.department_2 = QtWidgets.QLabel(self.centralwidget)
        self.department_2.setObjectName("department_2")
        self.verticalLayout.addWidget(self.department_2)
        self.department = QtWidgets.QLineEdit(self.centralwidget)
        self.department.setObjectName("department")
        self.verticalLayout.addWidget(self.department)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.applyData)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.ptextEdit.setReadOnly(1)

        #self.textBrowser.append("User Name,First Name,Last Name,Display Name,Job Title,Department,Office Number,Office Phone,Mobile Phone,Fax,Address,City,State or Province,ZIP or Postal Code,Country or Region")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.firstname_2.setText(_translate("MainWindow", "First Name"))
        self.lastname_2.setText(_translate("MainWindow", "Last Name"))
        self.jobtitle_2.setText(_translate("MainWindow", "Job Title"))
        self.department_2.setText(_translate("MainWindow", "Department"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_2.setText(_translate("MainWindow", "Apply"))


    def applyData(self):
        self.DataSets.append([self.firstname.text(), self.lastname.text(),self.jobtitle.text(),self.department.text()])
        for sets in self.DataSets:
            self.ptextEdit = (sets[0].lower() + "." + sets[1].lower() + "@ycbl.de" + "," + sets[0] + "," + sets[1] + "," + sets[0] + " " + sets[1] + "," + sets[2] + "," + sets[3] + ",,,,,,,,,")

app = QApplication([])
window = Ui_MainWindow()
window.show()
app.exec()
