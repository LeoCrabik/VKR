# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/examUnitWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_examUnitWidget(object):
    def setupUi(self, examUnitWidget):
        examUnitWidget.setObjectName("examUnitWidget")
        examUnitWidget.resize(546, 170)
        examUnitWidget.setMinimumSize(QtCore.QSize(0, 50))
        examUnitWidget.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(examUnitWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(examUnitWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.examName = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.examName.sizePolicy().hasHeightForWidth())
        self.examName.setSizePolicy(sizePolicy)
        self.examName.setMinimumSize(QtCore.QSize(0, 25))
        self.examName.setMaximumSize(QtCore.QSize(450, 16777215))
        self.examName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.examName.setTextFormat(QtCore.Qt.AutoText)
        self.examName.setScaledContents(True)
        self.examName.setWordWrap(True)
        self.examName.setIndent(-1)
        self.examName.setObjectName("examName")
        self.horizontalLayout.addWidget(self.examName)
        self.examUnit = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.examUnit.sizePolicy().hasHeightForWidth())
        self.examUnit.setSizePolicy(sizePolicy)
        self.examUnit.setMinimumSize(QtCore.QSize(50, 30))
        self.examUnit.setMaximumSize(QtCore.QSize(50, 30))
        self.examUnit.setObjectName("examUnit")
        self.horizontalLayout.addWidget(self.examUnit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(examUnitWidget)
        QtCore.QMetaObject.connectSlotsByName(examUnitWidget)

    def retranslateUi(self, examUnitWidget):
        _translate = QtCore.QCoreApplication.translate
        examUnitWidget.setWindowTitle(_translate("examUnitWidget", "Form"))
        self.examName.setText(_translate("examUnitWidget", "fasasfasssssssssssssasfasasfasssssssssssssasfasasfasssssssssssssasfasasfsssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfasssssssssssasfasasfasssssssssssssasfasasfassasssssssssssssasfasasfa sssssssssssssasfasasfasssssssssssssas"))
