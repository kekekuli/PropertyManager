# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(150, 100)
        Form.setMinimumSize(QtCore.QSize(150, 100))
        Form.setMaximumSize(QtCore.QSize(150, 100))
        self.message = QtWidgets.QLabel(Form)
        self.message.setGeometry(QtCore.QRect(20, 10, 101, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setStyleSheet("")
        self.message.setScaledContents(False)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.ensure = QtWidgets.QPushButton(Form)
        self.ensure.setGeometry(QtCore.QRect(20, 60, 100, 32))
        self.ensure.setObjectName("ensure")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.message.setText(_translate("Form", "错误！"))
        self.ensure.setText(_translate("Form", "确认"))
