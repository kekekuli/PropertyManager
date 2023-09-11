# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signinUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        Form.setAccessibleName("")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 70, 241, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.Label.setFont(font)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.house_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house_id.sizePolicy().hasHeightForWidth())
        self.house_id.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.house_id.setFont(font)
        self.house_id.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.house_id.setObjectName("house_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.house_id)
        self.Label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.Label_2.setFont(font)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(100, 190, 91, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.ensure = QtWidgets.QPushButton(Form)
        self.ensure.setGeometry(QtCore.QRect(230, 190, 100, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ensure.setFont(font)
        self.ensure.setObjectName("ensure")
        self.userCheck = QtWidgets.QCheckBox(Form)
        self.userCheck.setGeometry(QtCore.QRect(110, 160, 85, 20))
        self.userCheck.setObjectName("userCheck")
        self.adminCheck = QtWidgets.QCheckBox(Form)
        self.adminCheck.setGeometry(QtCore.QRect(230, 160, 101, 20))
        self.adminCheck.setObjectName("adminCheck")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "signin"))
        self.Label.setText(_translate("Form", "编号"))
        self.Label_2.setText(_translate("Form", "密码"))
        self.label.setText(_translate("Form", "请登录："))
        self.cancel.setText(_translate("Form", "返回"))
        self.ensure.setText(_translate("Form", "登陆"))
        self.userCheck.setText(_translate("Form", "用户登录"))
        self.adminCheck.setText(_translate("Form", "管理员登录"))
