# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zinc_view_graphics.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class Ui_ZincViewGraphics(object):
    def setupUi(self, ZincViewGraphics):
        if not ZincViewGraphics.objectName():
            ZincViewGraphics.setObjectName(u"ZincViewGraphics")
        ZincViewGraphics.resize(800, 600)
        self.centralwidget = QWidget(ZincViewGraphics)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sceneviewerWidget = SceneviewerWidget(self.centralwidget)
        self.sceneviewerWidget.setObjectName(u"sceneviewerWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.sceneviewerWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.viewAllButton = QPushButton(self.centralwidget)
        self.viewAllButton.setObjectName(u"viewAllButton")

        self.horizontalLayout.addWidget(self.viewAllButton)

        self.customButton = QPushButton(self.centralwidget)
        self.customButton.setObjectName(u"customButton")

        self.horizontalLayout.addWidget(self.customButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        ZincViewGraphics.setCentralWidget(self.centralwidget)

        self.retranslateUi(ZincViewGraphics)

        QMetaObject.connectSlotsByName(ZincViewGraphics)
    # setupUi

    def retranslateUi(self, ZincViewGraphics):
        ZincViewGraphics.setWindowTitle(QCoreApplication.translate("ZincViewGraphics", u"Zinc View Graphics", None))
        self.viewAllButton.setText(QCoreApplication.translate("ZincViewGraphics", u"View All", None))
        self.customButton.setText(QCoreApplication.translate("ZincViewGraphics", u"Custom", None))
    # retranslateUi

