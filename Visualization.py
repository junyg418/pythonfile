'''
인터페이스 제작하게 될 때 도움받았던 귀한자료
코드 분석해서 인터페이스 제작에 매우 큰 도움받았음
'''
# -*- coding: utf-8 -*-
# 교수님 리뷰 이후
# 적용 전/후 비교 그래프 가능한가?
# 구성부 라고 검색하면 각각 부분 별로 볼 수 있음
import os, subprocess, webbrowser
from shutil import copyfile
from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

global YR_compare, Q_compare, QN_compare
version = '1.7'
'''
version history
1.1 = 경작지 정보를 확인할 수 있는 메뉴를 추가
1.2 = 계단식 밭, 우회수로, 경사저감시설 BMP 메뉴 업데이트
1.3 = 초생대, 우회수로 BMP 기능 업데이트
1.4 = 각종 BMP의 효율 증진을 위한 parameter 업데이트 (1)
1.5 = TN 산정시 변수 변경 (직접유출 + 부유사 함유 N)
1.6 = 각종 BMP의 효율 증진을 위한 parameter 업데이트 (2)
1.7 = 졸업논문 대비로 bmp1~3, 6~7 에 대한 변수를 업데이트함.
'''


# TODO 현재 활용 중인 게비온 옹벽의 효율의 파악 필요, 변수변경 방법 파악 필요


class Ui_MainWindow(object):
    '''
    Frame shape and frequently used variables are declared here
    '''
    global selected_area, selected_field, main_font, sub_font, help_font, status_font, sizePolicy1, init_dir, \
        YR_compare, Q_compare, QN_compare, graph_window
    main_font = QtGui.QFont(QtGui.QFont('arial', 10))
    sub_font = QtGui.QFont('arial', 10)
    help_font = QtGui.QFont('arial', 10)
    status_font = QtGui.QFont('arial', 10)

    sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)

    init_dir = os.getcwd()

    '''
    Main window design start
    Physical program out look
    '''

    def setupUi(self, MainWindow):

        #   Main frame design start
        def Mainwindow_part(self):
            MainWindow.setObjectName("MainWindow")
            MainWindow.setFixedSize(610, 670)
            MainWindow.setFont(main_font)
            MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
            MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.centralwidget = QtWidgets.QWidget(MainWindow)

        #   Main frame design finish

        #   Help guide design start
        #   Help guide shows guide text on  the top of the program window
        def helpline_part(self):
            global helpline
            #   Helpline box
            self.helpline = QtWidgets.QLabel(self.centralwidget)
            self.helpline.setGeometry(QtCore.QRect(5, 5, 600, 50))
            self.helpline.setFont(help_font)
            #   Helpline box design
            self.helpline.setFrameShape(QtWidgets.QFrame.Box)
            self.helpline.setFrameShadow(QtWidgets.QFrame.Raised)
            self.helpline.setLineWidth(2)
            self.helpline.setAlignment(QtCore.Qt.AlignCenter)

        #   Help guide design finish

        #   Area select menu design start
        #   Supports selection from the drop down menu and button for current field
        def area_selection_part(self):
            #   Names over the combo box or button
            self.area_frame = QtWidgets.QFrame(self.centralwidget)
            self.area_frame.setGeometry(QtCore.QRect(5, 65, 600, 50))
            self.area_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.area_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.area_frame.setLineWidth(3)

            self.area_grid = QtWidgets.QGridLayout(self.area_frame)
            self.area_grid.setGeometry(QtCore.QRect(0, 0, 600, 50))
            self.area_grid.setContentsMargins(2, 2, 2, 2)

            self.label1 = QtWidgets.QLabel()
            self.label1.setFont(main_font)
            self.label1.setAlignment(QtCore.Qt.AlignCenter)
            self.area_grid.addWidget(self.label1, 0, 0, 1, 1)

            self.label2 = QtWidgets.QLabel()
            self.label2.setFont(main_font)
            self.label2.setAlignment(QtCore.Qt.AlignCenter)
            self.area_grid.addWidget(self.label2, 0, 1, 1, 1)

            self.label3 = QtWidgets.QLabel()
            self.label3.setFont(main_font)
            self.label3.setAlignment(QtCore.Qt.AlignCenter)
            self.area_grid.addWidget(self.label3, 0, 2, 1, 1)

            #   Combo box for area select
            #   Select area with "_sub"
            self.comboBox_area = QtWidgets.QComboBox(self.centralwidget)
            self.area_grid.addWidget(self.comboBox_area, 1, 0, 1, 1)
            self.comboBox_area.setSizePolicy(sizePolicy1)
            self.comboBox_area.setFont(main_font)
            self.comboBox_area.setMouseTracking(True)
            self.comboBox_area.setAcceptDrops(True)
            self.comboBox_area.setStyleSheet("")
            self.comboBox_area.setCurrentText("")
            self.comboBox_area.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
            self.comboBox_area.setIconSize(QtCore.QSize(20, 20))
            self.comboBox_area.setFrame(True)
            self.comboBox_area.setObjectName("comboBox_area")
            self.comboBox_area.setEnabled(False)
            areas = []
            for i in os.listdir():
                if i.endswith('_sub'):
                    areas.append(i)
            for i in areas:
                self.comboBox_area.addItem(i)
            self.comboBox_area.setCurrentIndex(-1)
            self.comboBox_area.currentTextChanged.connect(self.area_selected)

            #   Combo box for field select
            #   Select by number
            self.comboBox_field = QtWidgets.QComboBox(self.centralwidget)
            self.area_grid.addWidget(self.comboBox_field, 1, 1, 1, 1)
            self.comboBox_field.setSizePolicy(sizePolicy1)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.comboBox_field.setFont(font)
            self.comboBox_field.setAcceptDrops(True)
            self.comboBox_field.setObjectName("comboBox_field")
            self.comboBox_field.setEnabled(False)
            self.comboBox_field.setCurrentIndex(-1)
            self.comboBox_field.currentTextChanged.connect(self.field_selected)

            #   Button for current field select
            #   field in APEX run folder
            self.btn_current = QtWidgets.QPushButton(self.centralwidget)
            self.area_grid.addWidget(self.btn_current, 1, 2, 1, 1)
            self.btn_current.setSizePolicy(sizePolicy1)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.btn_current.setFont(font)
            self.btn_current.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.btn_current.setObjectName("btn_current")
            MainWindow.setCentralWidget(self.centralwidget)
            self.btn_current.setEnabled(False)
            self.btn_current.clicked.connect(self.action_btn_current)

        #   Area select menu design finish

        #   BMPs menu design start
        #   Tabs for Structural BMP and Non structural BMP
        def bmpstab_part(self):
            self.tabs = QtWidgets.QTabWidget(self.centralwidget)
            self.tabs.setFont(sub_font)
            self.tabs.setGeometry(QtCore.QRect(6, 120, 600, 350))
            self.st_tab = QtWidgets.QWidget()
            self.tabs.addTab(self.st_tab, "구조적")
            self.nst_tab = QtWidgets.QWidget()
            self.tabs.addTab(self.nst_tab, "비구조적")
            self.etc_tab = QtWidgets.QWidget()
            self.tabs.addTab(self.etc_tab, "기타")

            #   Strutural BMPs
            def bmptab1_part(self):
                #   Outer frame
                self.st_bmp_frame = QtWidgets.QFrame(self.st_tab)
                self.st_bmp_frame.setGeometry(QtCore.QRect(4, 4, 586, 310))
                self.st_bmp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.st_bmp_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.st_bmp_frame.setLineWidth(3)

                #   BMPs picture grid inside  3*2
                #   BMPs picture in the grid is sized by 200*170
                #   BMPs picture is located in ./resources/***.jpg
                self.st_gridLayoutWidget = QtWidgets.QWidget(self.st_bmp_frame)
                self.st_gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 575, 300))
                self.st_bmplayout = QtWidgets.QGridLayout(self.st_gridLayoutWidget)
                self.st_bmplayout.setContentsMargins(0, 0, 0, 0)

                def bmps_btn_setting_1(self):
                    #   BMPs picture icon design
                    self.bmp1 = QtWidgets.QPushButton(self.st_gridLayoutWidget)
                    self.bmp2 = QtWidgets.QPushButton(self.st_gridLayoutWidget)
                    self.bmp3 = QtWidgets.QPushButton(self.st_gridLayoutWidget)
                    self.bmp4 = QtWidgets.QPushButton(self.st_gridLayoutWidget)
                    self.bmp5 = QtWidgets.QPushButton(self.st_gridLayoutWidget)
                    self.bmp6 = QtWidgets.QPushButton(self.st_gridLayoutWidget)
                    bmps = [self.bmp1, self.bmp2, self.bmp3, self.bmp4, self.bmp5, self.bmp6]

                    #   BMPs picture icon policy
                    for i in bmps:
                        i.setSizePolicy(sizePolicy1)
                        i.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        i.setFocusPolicy(QtCore.Qt.ClickFocus)
                        i.setFlat(True)

                    #   Button in grid
                    self.st_bmplayout.addWidget(self.bmp1, 0, 0, 1, 1)
                    self.st_bmplayout.addWidget(self.bmp2, 0, 1, 1, 1)
                    self.st_bmplayout.addWidget(self.bmp3, 0, 2, 1, 1)
                    self.st_bmplayout.addWidget(self.bmp4, 1, 0, 1, 1)
                    self.st_bmplayout.addWidget(self.bmp5, 1, 1, 1, 1)
                    self.st_bmplayout.addWidget(self.bmp6, 1, 2, 1, 1)

                    #   Button click action
                    self.bmp1.clicked.connect(self.apply_bmp1)
                    self.bmp2.clicked.connect(self.apply_bmp2)
                    self.bmp3.clicked.connect(self.apply_bmp3)
                    self.bmp4.clicked.connect(self.apply_bmp4)
                    self.bmp5.clicked.connect(self.apply_bmp5)
                    # self.bmp6.clicked.connect(self.apply_bmp6)

                def bmps_icon_setting_1(self):
                    #   Icon declare
                    #   Image save in "./resources" directory
                    icon1 = QtGui.QIcon()
                    icon2 = QtGui.QIcon()
                    icon3 = QtGui.QIcon()
                    icon4 = QtGui.QIcon()
                    icon5 = QtGui.QIcon()
                    icon6 = QtGui.QIcon()

                    #   Icon image and size extend policy
                    icons = [icon1, icon2, icon3, icon4, icon5, icon6]
                    bmps = [self.bmp1, self.bmp2, self.bmp3, self.bmp4, self.bmp5, self.bmp6]
                    bmps_names = ['grassedwaterway', 'terrace', 'filterstrip', 'diversiondike', 'gradestabilization',
                                  'no']
                    for i in range(len(bmps)):
                        icons[i] = QtGui.QIcon()
                        icons[i].addPixmap(QtGui.QPixmap("./resources/%s.jpg" % bmps_names[i]), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
                        bmps[i].setIcon(icons[i])
                        bmps[i].setIconSize(QtCore.QSize(170, 170))
                        bmps[i].setEnabled(False)

                #   Function implementation
                bmps_btn_setting_1(self)
                bmps_icon_setting_1(self)

            #   Non structural BMPs
            def bmptab2_part(self):
                #   Outer frame
                self.nst_bmp_frame = QtWidgets.QFrame(self.nst_tab)
                self.nst_bmp_frame.setGeometry(QtCore.QRect(4, 4, 586, 310))
                self.nst_bmp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.nst_bmp_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.nst_bmp_frame.setLineWidth(3)

                #   BMPs picture grid inside 3*2
                #   BMPs picture in the grid is sized by 200*170
                #   BMPs picture is located in ./resources/**.jpg
                self.nst_gridLayoutWidget = QtWidgets.QWidget(self.nst_bmp_frame)
                self.nst_gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 575, 300))
                self.nst_bmplayout = QtWidgets.QGridLayout(self.nst_gridLayoutWidget)
                self.nst_bmplayout.setContentsMargins(0, 0, 0, 0)

                def bmps_btn_setting_2(self):
                    #   BMPs picture icon design
                    self.bmp7 = QtWidgets.QPushButton(self.nst_gridLayoutWidget)
                    self.bmp8 = QtWidgets.QPushButton(self.nst_gridLayoutWidget)
                    self.bmp9 = QtWidgets.QPushButton(self.nst_gridLayoutWidget)
                    bmps = [self.bmp7, self.bmp8, self.bmp9]

                    #   BMPs picture icon policy
                    for i in bmps:
                        i.setSizePolicy(sizePolicy1)
                        i.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        i.setFocusPolicy(QtCore.Qt.ClickFocus)
                        i.setFlat(True)

                    #   Button in grid
                    self.nst_bmplayout.addWidget(self.bmp7, 0, 0, 1, 1)
                    self.nst_bmplayout.addWidget(self.bmp8, 0, 1, 1, 1)
                    self.nst_bmplayout.addWidget(self.bmp9, 0, 2, 1, 1)

                    #   Button click action
                    self.bmp7.clicked.connect(self.apply_bmp7)
                    self.bmp8.clicked.connect(self.apply_bmp8)
                    self.bmp9.clicked.connect(self.apply_bmp9)

                def bmps_icon_setting_2(self):
                    # BMP 별 이미지 한번에 설정하기
                    # ./resources 폴더에 이미지 저장하기
                    icon7 = QtGui.QIcon()
                    icon8 = QtGui.QIcon()
                    icon9 = QtGui.QIcon()
                    # 아이콘 이미지 크기 및 확장 설정
                    icons = [icon7, icon8, icon9]
                    bmps = [self.bmp7, self.bmp8, self.bmp9]
                    bmps_names = ['50fert', '70fert', 'notill']
                    for i in range(len(bmps)):
                        icons[i] = QtGui.QIcon()
                        icons[i].addPixmap(QtGui.QPixmap("./resources/%s.jpg" % bmps_names[i]), QtGui.QIcon.Normal,
                                           QtGui.QIcon.Off)
                        bmps[i].setIcon(icons[i])
                        bmps[i].setIconSize(QtCore.QSize(170, 170))
                        bmps[i].setEnabled(False)

                bmps_btn_setting_2(self)
                bmps_icon_setting_2(self)

            #   ETC BMPs
            def bmptab3_part(self):
                #   Outer frame
                self.etc_bmp_frame = QtWidgets.QFrame(self.etc_tab)
                self.etc_bmp_frame.setGeometry(QtCore.QRect(4, 4, 586, 310))
                self.etc_bmp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.etc_bmp_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.etc_bmp_frame.setLineWidth(3)

                #   BMPs picture grid inside 3*2
                #   BMPs picture in the grid is sized by 200*170
                #   BMPs picture is located in ./resources/***.jpg
                self.etc_gridLayoutWidget = QtWidgets.QWidget(self.etc_bmp_frame)
                self.etc_gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 575, 300))
                self.etc_bmplayout = QtWidgets.QGridLayout(self.etc_gridLayoutWidget)
                self.etc_bmplayout.setContentsMargins(0, 0, 0, 0)

                #   This tab is not activated
                self.etc_tab_label = QtWidgets.QLabel(self.nst_gridLayoutWidget)
                self.etc_tab_label.setText("THIS TAB IS GETTING READY")
                self.etc_tab_label.setAlignment(QtCore.Qt.AlignCenter)
                self.etc_tab_label.setFont(QtGui.QFont('Arial', 15))
                self.etc_bmplayout.addWidget(self.etc_tab_label)

            #   BMP TAB implementation
            bmptab1_part(self)
            bmptab2_part(self)
            bmptab3_part(self)

        #   BMPs menu design Finished

        #   Control part of the middle part design start
        #   Control menu includes 3 functions
        #   dir, compare, reset
        def control_part(self):

            #   Directory control part
            #   Includes :  Field information pop-up function
            #               Field directory open function
            def dir_control(self):
                #   Frame of the buttons
                self.dir_frame = QtWidgets.QFrame(self.centralwidget)
                self.dir_frame.setGeometry(QtCore.QRect(5, 480, 100, 80))
                self.dir_frame.setFont(main_font)
                self.dir_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.dir_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
                #   VBOX layout setting
                self.dir_layout = QtWidgets.QVBoxLayout(self.dir_frame)
                self.dir_layout.setGeometry(QtCore.QRect(0, 0, 100, 60))
                self.dir_layout.setContentsMargins(3, 3, 3, 3)
                #   Button design
                self.btn_field_check = QtWidgets.QPushButton(self.dir_frame)
                self.btn_input_dir = QtWidgets.QPushButton(self.dir_frame)
                for i in [self.btn_field_check, self.btn_input_dir]:
                    i.setSizePolicy(sizePolicy1)
                    i.setFont(main_font)
                    i.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    i.setEnabled(False)
                    self.dir_layout.addWidget(i)
                #   Button click action
                self.btn_field_check.clicked.connect(self.field_check)
                self.btn_input_dir.clicked.connect(self.action_input_dir)

            #   Directory control part done

            #   Compare and run control part
            #   Includes :  Compare function (runoff and T-N)
            #               Field run function
            #               Area run function (Getting prepared)
            def compare_control(self):
                #   Outer frame
                self.compare_frame = QtWidgets.QFrame(self.centralwidget)
                self.compare_frame.setGeometry(QtCore.QRect(110, 480, 400, 80))
                self.compare_frame.setFont(main_font)
                self.compare_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.compare_frame.setFrameShadow(QtWidgets.QFrame.Sunken)

                #   Grid design
                self.gridLayoutWidget1 = QtWidgets.QWidget(self.compare_frame)
                self.gridLayoutWidget1.setGeometry(QtCore.QRect(0, 0, 400, 80))
                self.compare_layout = QtWidgets.QGridLayout(self.gridLayoutWidget1)
                self.compare_layout.setContentsMargins(3, 3, 3, 3)

                #   Button declare
                self.btn_compare = QtWidgets.QPushButton(self.compare_frame)
                self.btn_extra1 = QtWidgets.QPushButton(self.compare_frame)
                #   TODO 기존 APEX 구동하던 코드 복사해서 input_dir 과 apex_dir의 경로가
                #    일치하지 않을 경우 대상지역을 모의하는 코드로 변경하여 구동
                self.btn_APEX_area_run = QtWidgets.QPushButton(self.compare_frame)
                self.btn_APEX_field_run = QtWidgets.QPushButton(self.compare_frame)

                #   Button policy
                btns = [self.btn_compare, self.btn_extra1, self.btn_APEX_field_run, self.btn_APEX_area_run]
                for i in btns:
                    i.setSizePolicy(sizePolicy1)
                    i.setFont(main_font)
                    i.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    i.setEnabled(False)

                #   Button layout in grid
                self.compare_layout.addWidget(self.btn_compare, 0, 0, 1, 1)
                self.compare_layout.addWidget(self.btn_extra1, 0, 1, 1, 1)
                self.compare_layout.addWidget(self.btn_APEX_field_run, 1, 0, 1, 1)
                self.compare_layout.addWidget(self.btn_APEX_area_run, 1, 1, 1, 1)

                #   Button click action
                self.btn_APEX_field_run.clicked.connect(self.action_field_run)
                self.btn_compare.clicked.connect(self.action_compare)

            #   Compare and run control part done

            #   Reset control part
            #   Includes :  Reset the field before BMP application
            def reset_control(self):
                self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
                self.btn_reset.setGeometry(QtCore.QRect(515, 480, 80, 35))
                self.btn_reset.setSizePolicy(sizePolicy1)
                self.btn_reset.setFont(main_font)
                self.btn_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn_reset.setObjectName("btn_reset")
                MainWindow.setCentralWidget(self.centralwidget)
                self.btn_reset.setEnabled(False)
                self.btn_reset.clicked.connect(self.action_reset)

            #   Function implementation
            dir_control(self)
            compare_control(self)
            reset_control(self)

        #   Control part of the middle part design finish

        #   Logo of the bottom part design start
        def logo_part(self):
            self.logoline = QtWidgets.QLabel(self.centralwidget)
            self.logoline.setGeometry(5, 565, 600, 60)
            self.logoline.setAlignment(QtCore.Qt.AlignCenter)
            #   Logo img file location
            self.knu_logo = QtGui.QPixmap("./resources/knu_logo.png")
            self.logoline.setPixmap(self.knu_logo.scaled(self.logoline.size(), QtCore.Qt.KeepAspectRatio))

        #   Logo of the bottom part design finish

        #   Upper menu bar design start
        #   Upper menu includes menu and setting and status bar below
        def menu_part(self):
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 30))

            #   Menu for programs
            self.menu = QtWidgets.QMenu(self.menubar)

            self.send_mail = QtWidgets.QAction(MainWindow)
            self.send_mail.triggered.connect(self.action_send_mail)

            self.visit_web = QtWidgets.QAction(MainWindow)
            self.visit_web.triggered.connect(self.action_visit_web)

            self.visit_APEX = QtWidgets.QAction(MainWindow)
            self.visit_APEX.triggered.connect(self.action_visit_APEX)

            #   Setting menu
            self.menu_2 = QtWidgets.QMenu(self.menubar)
            MainWindow.setMenuBar(self.menubar)

            self.APEX_dir = QtWidgets.QAction(MainWindow)
            self.APEX_dir.triggered.connect(self.action_APEX_dir)

            #   Menu location
            self.menu.addAction(self.send_mail)
            self.menu.addAction(self.visit_web)
            self.menu.addAction(self.visit_APEX)
            self.menu_2.addAction(self.APEX_dir)
            self.menubar.addAction(self.menu.menuAction())
            self.menubar.addAction(self.menu_2.menuAction())

            #   Status bar below
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.resize(700, 20)
            self.statusbar.setFont(status_font)
            MainWindow.setStatusBar(self.statusbar)

        #   Upper menu bar design start

        #   Full GUI functions implementation
        #   This part includes all design functions
        Mainwindow_part(self)
        helpline_part(self)
        area_selection_part(self)
        bmpstab_part(self)
        control_part(self)
        menu_part(self)
        logo_part(self)
        #   All function implementation done

        self.retranslateUi(MainWindow)

    #   Declare names and tooltips for buttons
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BMP APPLICATION for APEX by KNU RDA"))
        self.label1.setText(_translate("MainWindow", "대상지역 선택"))
        self.label2.setText(_translate("MainWindow", "경작지 번호 선택"))
        self.label3.setText(_translate("MainWindow", "현재 모의 지역 적용"))
        self.helpline.setStatusTip(_translate("MainWindow", "도움말 입니다."))
        self.helpline.setText(_translate("MainWindow", "설정 - APEX 경로 설정에서 APEX 모형의 경로 설정을 먼저 해주세요!"))

        self.st_tab.setStatusTip(_translate("MainWindow", "구조적 BMP는 경작지 주변에 추가적인 구조물을 설치하는 것입니다."))
        self.st_tab.setStatusTip(_translate("MainWindow", "구조적 BMP는 경작지 주변에 추가적인 구조물을 설치하는 것입니다."))
        self.bmp1.setStatusTip(_translate("MainWindow", "식생수로"))
        self.bmp2.setStatusTip(_translate("MainWindow", "계단식 밭"))
        self.bmp3.setStatusTip(_translate("MainWindow", "초생대"))
        self.bmp4.setStatusTip(_translate("MainWindow", "우회수로"))
        self.bmp5.setStatusTip(_translate("MainWindow", "경사저감시설"))
        self.bmp6.setStatusTip(_translate("MainWindow", "게비온 옹벽"))

        self.bmp7.setStatusTip(_translate("MainWindow", "비료줄이기 50%"))
        self.bmp8.setStatusTip(_translate("MainWindow", "비료줄이기 70%"))
        self.bmp9.setStatusTip(_translate("MainWindow", "무경운"))

        self.btn_current.setText(_translate("MainWindow", "Current Field"))
        self.btn_field_check.setText(_translate("MainWindow", "경작지 정보"))
        self.btn_field_check.setStatusTip(_translate("MainWindow", "모의 대상 경작지의 정보를 확인합니다."))
        self.btn_input_dir.setText(_translate("MainWindow", "입력자료 폴더"))
        self.btn_input_dir.setStatusTip(_translate("MainWindow", "입력자료 폴더를 엽니다."))

        self.menu.setTitle(_translate("MainWindow", "메뉴"))
        self.menu_2.setTitle(_translate("MainWindow", "설정"))
        self.send_mail.setText(_translate("MainWindow", "Email 문의하기"))
        self.visit_web.setText(_translate("MainWindow", "홈페이지 방문"))
        self.visit_APEX.setText(_translate("MainWindow", "APEX 모형 설명"))
        self.APEX_dir.setText(_translate("MainWindow", "APEX 경로설정"))
        self.APEX_dir.setStatusTip(_translate("MainWindow", "APEX 모형의 경로를 설정합니다. (필수)"))

        self.btn_compare.setText(_translate("MainWindow", "BMP 적용 전/후 비교"))
        self.btn_compare.setStatusTip(_translate("MainWindow", "최적관리기법의 적용 전/후 APEX 모의 결과를 비교합니다."))
        self.btn_reset.setText(_translate("MainWindow", "초기화"))
        self.btn_reset.setStatusTip(_translate("MainWindow", "BMP 적용 전 상태로 되돌립니다."))
        self.btn_extra1.setText(_translate("MainWindow", "Extra1"))
        self.btn_extra1.setStatusTip(_translate("MainWindow", "Explain"))
        self.btn_APEX_field_run.setText(_translate("MainWindow", "경작지 모의"))
        self.btn_APEX_field_run.setStatusTip(_translate("MainWindow", "선택된 경작지에 대한 APEX 모의를 진행합니다."))
        self.btn_APEX_area_run.setText(_translate("MainWindow", "대상지역 모의"))
        self.btn_APEX_area_run.setStatusTip(_translate("MainWindow", "선택된 대상지역에 대한 APEX 모의를 진행합니다."))

    '''
    Main window design finish
    Physical program out look
    '''

    '''
    Full functions for buttons
    Software functions are built from this line
    '''

    #   Extra functions (upper menu) design start
    #   APEX running directory set

    #   APEX run diretory setting function
    def action_APEX_dir(self):
        global apex_dir
        apex_dir = QtWidgets.QFileDialog.getExistingDirectory()
        if apex_dir != '':
            self.helpline.setText(apex_dir + "\n위의 경로로 APEX 경로가 설정되었습니다. 대상지역과 경작지를 선택하세요.")
            self.comboBox_area.setEnabled(True)
            self.comboBox_field.setEnabled(True)
            self.btn_current.setEnabled(True)
            return apex_dir
        else:
            self.helpline.setText('APEX 경로를 다시 설정해주세요.')

    #   Area selection combo box function
    def area_selected(self):
        global selected_area
        selected_area = self.comboBox_area.currentText()
        # EDIT
        try:
            fields = os.listdir(os.getcwd() + '/' + selected_area)
            for i in range(len(fields)):
                fields[i] = int(fields[i])
            fields.sort()
            for i in range(len(fields)):
                fields[i] = str(fields[i])

            self.comboBox_field.clear()
            for i in fields:
                self.comboBox_field.addItem(i)

        except:
            self.helpline.setText("대상 지역이 올바르지 않습니다. 다시 선택해주세요")

    #   Field selection combo box function
    def field_selected(self):
        global selected_field, seleted_area, input_dir
        selected_field = self.comboBox_field.currentText()
        input_dir = os.getcwd() + '/' + selected_area + '/' + selected_field
        in_files = os.listdir(input_dir)
        need_files = ['WINAPEX.SUB', 'APEXCONT.DAT', 'WINAPEX.SIT', 'APEXRUN.DAT']
        check_files = all(elem in in_files for elem in need_files)
        if check_files:
            self.helpline.setText(selected_area + '/' + selected_field + ' 경작지가 선택되었습니다.\n 최적관리기법을 선택하세요.')
            self.btn_field_check.setEnabled(True)
            self.btn_input_dir.setEnabled(True)
            self.btn_APEX_field_run.setEnabled(True)
            self.bmp1.setEnabled(True)
            self.bmp2.setEnabled(True)
            self.bmp3.setEnabled(True)
            self.bmp4.setEnabled(True)
            self.bmp5.setEnabled(True)
            self.bmp6.setEnabled(True)
            self.bmp7.setEnabled(True)
            self.bmp8.setEnabled(True)
            self.bmp9.setEnabled(True)
        else:
            self.helpline.setText(selected_area + '/' + selected_field + ' 경로 내 APEX 모형 입력자료가 없습니다.\nWINAPEX.SUB   '
                                                                         'APEXCONT.DAT   WINAPEX.SIT   APEXRUN.DAT')
            self.btn_field_check.setEnabled(False)
            self.btn_input_dir.setEnabled(False)
            self.btn_APEX_field_run.setEnabled(False)
            self.bmp1.setEnabled(False)
            self.bmp2.setEnabled(False)
            self.bmp3.setEnabled(False)
            self.bmp4.setEnabled(False)
            self.bmp5.setEnabled(False)
            self.bmp6.setEnabled(False)
            self.bmp7.setEnabled(False)
            self.bmp8.setEnabled(False)
            self.bmp9.setEnabled(False)

        self.btn_reset.setEnabled(True) if "WINAPEX_origin.SUB" in os.listdir(input_dir) else self.btn_reset.setEnabled(
            False)
        self.btn_compare.setEnabled(True) if "WINAPEX_origin.SUB" in os.listdir(
            input_dir) else self.btn_reset.setEnabled(False)

    #   Current field button function
    def action_btn_current(self):
        global input_dir
        input_dir = apex_dir
        in_files = os.listdir(input_dir)
        need_files = ['WINAPEX.SUB', 'APEXCONT.DAT', 'WINAPEX.SIT', 'APEXRUN.DAT']
        check_files = all(elem in in_files for elem in need_files)
        if check_files:
            self.helpline.setText('현재 모의 중인 경작지에 BMP를 적용합니다.')
            self.btn_field_check.setEnabled(True)
            self.btn_input_dir.setEnabled(True)
            self.bmp1.setEnabled(True)
            self.bmp2.setEnabled(True)
            self.bmp3.setEnabled(True)
            self.bmp4.setEnabled(True)
            self.bmp5.setEnabled(True)
            self.bmp6.setEnabled(True)
            self.bmp7.setEnabled(True)
            self.bmp8.setEnabled(True)
            self.bmp9.setEnabled(True)
            self.btn_compare.setEnabled(False)

        else:
            self.helpline.setText('경로 내 APEX 모형 입력자료가 없습니다.\n"WINAPEX.SUB, APEXCONT.DAT, WINAPEX.SIT, APEXRUN.DAT"')

        self.btn_reset.setEnabled(True) if "WINAPEX_origin.SUB" in os.listdir(input_dir) else self.btn_reset.setEnabled(
            False)
        self.btn_compare.setEnabled(True) if "WINAPEX_origin.SUB" in os.listdir(
            input_dir) else self.btn_reset.setEnabled(False)

    #   Field information check function
    def field_check(self):
        #   Popup design
        d = QtWidgets.QDialog()
        d.setFixedSize(300, 270)
        #   Grid design for contents
        form = QtWidgets.QFormLayout()

        #   Extract data from the input data

        #   Run period
        cont_f = open(input_dir + '/APEXCONT.DAT', 'r')
        r_cont_f = cont_f.readlines()
        styear = int(float(r_cont_f[0][10:20]))
        dur = int(float(r_cont_f[0][0:10]))
        period = str(styear) + "년 ~ " + str(styear + dur - 1) + "년"

        #   Weather station code
        sub_f = open(input_dir + '/WINAPEX.SUB', 'r')
        r_sub_f = sub_f.readlines()
        wstation = int(r_sub_f[1][56:65])
        wstation_dics = {90: '속초', 93: '북춘천', 95: '철원', 96: '독도', 98: '동두천', 99: '파주', 100: '대관령',
                         101: '춘천', 102: '백령도', 104: '북강릉', 105: '강릉', 106: '동해', 108: '서울', 112: '인천',
                         114: '원주', 115: '울릉도', 116: '관악(레)', 119: '수원', 121: '영월', 127: '충주', 129: '서산',
                         130: '울진', 131: '청주', 133: '대전', 135: '추풍령', 136: '안동', 137: '상주', 138: '포항',
                         140: '군산', 143: '대구', 146: '전주', 152: '울산', 155: '창원', 156: '광주', 159: '부산',
                         160: '부산(레)', 162: '통영', 165: '목포', 168: '여수', 169: '흑산도', 170: '완도', 172: '고창',
                         174: '순천', 175: '진도(첨찰산)', 184: '제주', 185: '고산', 188: '성산', 189: '서귀포',
                         192: '진주', 201: '강화', 202: '양평', 203: '이천', 211: '인제', 212: '홍천', 216: '태백',
                         217: '정선군', 221: '제천', 226: '보은', 229: '격렬', 232: '천안', 235: '보령', 236: '부여',
                         238: '금산', 243: '부안', 244: '임실', 245: '정읍', 247: '남원', 248: '장수', 251: '고창군',
                         252: '영광군', 253: '김해시', 254: '순창군', 255: '북창원', 257: '양산시', 258: '보성군',
                         259: '강진군', 260: '장흥', 261: '해남', 262: '고흥', 263: '의령군', 264: '함양군', 266: '광양시',
                         268: '진도군', 271: '봉화', 272: '영주', 273: '문경', 276: '청송군', 277: '영덕', 278: '의성',
                         279: '구미', 281: '영천', 283: '경주시', 284: '거창', 285: '합천', 288: '밀양', 289: '산청',
                         294: '거제', 295: '남해'}

        #   Annual average precipitation
        try:
            dlyf = open(apex_dir + '/KR0' + str(wstation).zfill(3) + '.dly', 'r')
            r_dlyf = dlyf.readlines()
            d_dlyf = []
            temp = []
            for i in range(len(r_dlyf)):
                temp = []
                r_dlyf[i] = r_dlyf[i].replace("\n", '')
                r_dlyf[i] = r_dlyf[i].split(' ')
                for r in range(len(r_dlyf[i])):
                    if r_dlyf[i][r] != '':
                        temp.append(r_dlyf[i][r])
                d_dlyf.append(temp)
            sum = 0
            annual = {}
            for i in range(len(d_dlyf)):
                if d_dlyf[i] != d_dlyf[-1]:
                    if d_dlyf[i][0] == d_dlyf[i + 1][0]:
                        sum = sum + float(d_dlyf[i][6])
                    else:
                        sum = sum + float(d_dlyf[i][6])
                        annual[int(d_dlyf[i][0])] = sum
                        sum = 0
                else:
                    sum = sum + float(d_dlyf[i][6])
                    annual[int(d_dlyf[i][0])] = sum
            annu_pcp = 0
            for i in range(styear, styear + dur):
                annu_pcp = annu_pcp + annual[i]
            annu_pcp = round(annu_pcp / dur, 2)
        except:
            #   if .dly file is not found or has problem, error text will be shown in the popup
            annu_pcp = 'ERROR'

        #   Field area
        area = float(r_sub_f[3][0:10])
        area = int(area * 10000)

        #   Field slope
        slope = float(r_sub_f[3][50:60])
        slope = round(slope, 3)

        #   Field coordinates
        xcoord = float(r_sub_f[2][30:40])
        ycoord = float(r_sub_f[2][20:30])
        xcoord = round(xcoord, 3)
        ycoord = round(ycoord, 3)

        #   Grid location of the contents start
        tip = QtWidgets.QLabel()
        tip.setFrameShape(QtWidgets.QFrame.Box)
        tip.setFrameShadow(QtWidgets.QFrame.Raised)
        tip.setLineWidth(1)
        tip.setAlignment(QtCore.Qt.AlignCenter)
        tip.setMargin(5)
        tip.setText("APEX 모형 구동이 가능합니다.")

        p1 = QtWidgets.QLineEdit('')
        p1.setFont(sub_font)
        p1.setReadOnly(True)
        p1.setAlignment(QtCore.Qt.AlignCenter)
        p1.setText(period)
        form.addRow("구동기간 :", p1)

        p2 = QtWidgets.QLineEdit('')
        p2.setFont(sub_font)
        p2.setReadOnly(True)
        p2.setAlignment(QtCore.Qt.AlignCenter)
        p2.setText(wstation_dics[wstation] + ' 관측소 (' + str(wstation) + ')')
        form.addRow("기상관측소 :", p2)

        p3 = QtWidgets.QLineEdit('')
        p3.setFont(sub_font)
        p3.setReadOnly(True)
        p3.setAlignment(QtCore.Qt.AlignCenter)
        p3.setText(str(annu_pcp) + " mm")
        if annu_pcp == 'ERROR':
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
            p3.setPalette(palette)
            p3.setStyleSheet("border: 1px solid red;")
            tip.setText("강수데이터에 문제가 있습니다.\n기상데이터 보유기간과 모의기간을 확인해주세요.")
        form.addRow("연평균강수 :", p3)

        p4 = QtWidgets.QLineEdit('')
        p4.setFont(sub_font)
        p4.setReadOnly(True)
        p4.setAlignment(QtCore.Qt.AlignCenter)
        p4.setText(str(area) + " sq.m")
        form.addRow("경작지면적 :", p4)

        p5 = QtWidgets.QLineEdit('')
        p5.setFont(sub_font)
        p5.setReadOnly(True)
        p5.setAlignment(QtCore.Qt.AlignCenter)
        p5.setText(str(slope) + ' m/m')
        form.addRow("경작지경사도 :", p5)

        p6 = QtWidgets.QLineEdit('')
        p6.setFont(sub_font)
        p6.setReadOnly(True)
        p6.setAlignment(QtCore.Qt.AlignCenter)
        p6.setText(str(xcoord) + ' , ' + str(ycoord))
        form.addRow("경작지좌표 :", p6)

        form.addRow(tip)
        #   Grid location of the contents finish

        b1 = QtWidgets.QPushButton('ok', d)
        form.addRow(b1)
        d.setLayout(form)
        d.setWindowTitle('경작지 정보')
        b1.clicked.connect(d.close)
        d.exec_()

    #   APEX run for field scale
    def action_field_run(self):
        need_files = ['WINAPEX.SUB', 'APEXCONT.DAT', 'WINAPEX.SIT', 'APEXRUN.DAT']
        if input_dir == apex_dir:
            os.chdir(apex_dir)
            subprocess.call(apex_dir + '/APEX1501debug64.exe')
            webbrowser.open(apex_dir)
        else:
            for i in need_files:
                copyfile(input_dir + '/' + i, apex_dir + '/' + i)
            os.chdir(apex_dir)
            subprocess.call(apex_dir + '/APEX1501debug64.exe')
            webbrowser.open(apex_dir)
            os.chdir(init_dir)

    #   Open input directory
    def action_input_dir(self):
        import webbrowser
        webbrowser.open(input_dir)

    #   Reset function
    #   Delete all .sub files and call back the backup .sub file
    def action_reset(self):
        if "WINAPEX.SUB" in os.listdir(input_dir):
            print ("Editted .SUB files checked")
            os.remove(input_dir + "/WINAPEX.SUB")
        else:
            print("Editted .SUB files not checked")
        os.rename(input_dir + "/WINAPEX_origin.SUB", input_dir + "/WINAPEX.SUB")
        #   Delete all .sub files
        all_list = os.listdir(input_dir)
        sub_list = []
        for i in all_list:
            if i.endswith('.SUB'):
                sub_list.append(i)
        sub_list.remove('WINAPEX.SUB')
        if sub_list == []:
            print ("APEX files reset done")
        for i in sub_list:
            os.remove(input_dir + '/' + i)
        d = QtWidgets.QDialog()
        t1 = QtWidgets.QLabel('경작지가 초기상태로\n변경되었습니다.', d)
        vbox = QtWidgets.QVBoxLayout()
        b1 = QtWidgets.QPushButton('ok', d)
        vbox.addWidget(t1)
        vbox.addWidget(b1)
        vbox.addStretch()
        d.setLayout(vbox)
        d.setWindowTitle('Message')
        b1.clicked.connect(d.close)
        d.exec_()
        self.btn_reset.setEnabled(False)
        self.btn_compare.setEnabled(False)

    #   Compare function
    #   Compare APEX results between pre-BMP and post-BMP
    #   Compare result will be shown through "PlotCanvas class" Line 1322
    def action_compare(self):
        global YR_compare, Q_compare, TN_compare, graph_window
        from matplotlib.pyplot import rcParams
        #   make temporary folder for pre & post BMP
        if not os.path.isdir(input_dir + '/temp'):
            os.makedirs(input_dir + '/temp')
        #   Run APEX 2 times for pre & post BMP
        if input_dir != apex_dir:
            fix_files = ['APEXCONT.DAT', 'WINAPEX.SIT', 'APEXRUN.DAT']
            for i in fix_files:
                copyfile(input_dir + '/' + i, apex_dir + '/' + i)

            compare_files = ['WINAPEX.SUB', 'WINAPEX_origin.SUB']
            for i in compare_files:
                copyfile(input_dir + '/' + i, apex_dir + '/WINAPEX.SUB')
                os.chdir(apex_dir)
                subprocess.call(apex_dir + '/APEX1501debug64.exe')
                copyfile('Winapex.ASA', input_dir + '/temp/' + i + '.ASA')
                os.chdir(init_dir)
        elif input_dir == apex_dir:
            compare_files = ['WINAPEX.SUB', 'WINAPEX_origin.SUB']
            for i in compare_files:
                os.rename(input_dir + '/' + i, input_dir + '/WINAPEX.SUB')
                os.chdir(apex_dir)
                subprocess.call(apex_dir + '/APEX1501debug64.exe')
                copyfile('Winapex.ASA', input_dir + '/temp/' + i + '.ASA')
                if i == 'WINAPEX.SUB':
                    os.remove('WINAPEX.SUB')
                os.chdir(init_dir)
        #   Organize APEX Results (pre & post BMP)
        f1 = open(input_dir + '/temp/WINAPEX_origin.SUB.ASA', 'r')
        f2 = open(input_dir + '/temp/WINAPEX.SUB.ASA', 'r')
        for i in [f1, f2]:
            temp_lines = i.readlines()[8:]
            temp_lines2 = []
            temp_lines3 = []
            for r in range(len(temp_lines)):
                temp_lines[r] = temp_lines[r].replace('\n', '')
                temp_lines[r] = temp_lines[r].split(' ')
            for r in range(len(temp_lines)):
                for k in range(len(temp_lines[r])):
                    if temp_lines[r][k] != '':
                        temp_lines2.append(temp_lines[r][k])
                temp_lines3.append(temp_lines2)
                temp_lines2 = []
            #   Save results as list
            if i == f1:
                origin_sce = temp_lines3
            else:
                bmp_sce = temp_lines3

        #   List data for plotting
        #   Temporal organization
        YR = origin_sce[0].index('YR')
        YR_compare = []
        for i in range(len(origin_sce) - 1):
            YR_compare.append(int(origin_sce[i + 1][YR]))

        #   Direct runoff (Q)
        Q = origin_sce[0].index('Q')
        Q_compare = []
        for i in [origin_sce, bmp_sce]:
            Qtemp = []
            for r in range(len(i) - 1):
                i[r + 1][Q].replace('E', 'e')
                i[r + 1][Q].replace('+0', '')
                i[r + 1][Q].replace('+', '')
                Qtemp.append(float(i[r + 1][Q]))
            Q_compare.append(Qtemp)

        #   Total Nitrogen (TN)
        QN = origin_sce[0].index('QN')
        YN = origin_sce[0].index('YN')
        RSFN = origin_sce[0].index('RSFN')

        TN_compare = []
        for i in [origin_sce, bmp_sce]:
            TNtemp = []
            for r in range(len(i) - 1):
                i[r + 1][QN].replace('E', 'e')
                i[r + 1][QN].replace('+0', '+')
                i[r + 1][QN].replace('-0', '-')

                i[r + 1][RSFN].replace('E', 'e')
                i[r + 1][RSFN].replace('+0', '+')
                i[r + 1][RSFN].replace('-0', '-')
                
                i[r + 1][YN].replace('E', 'e')
                i[r + 1][YN].replace('+0', '+')
                i[r + 1][YN].replace('-0', '-')

                TNtemp.append(float(i[r + 1][QN]) + float(i[r + 1][YN]) + float(i[r + 1][RSFN]))
            TN_compare.append(TNtemp)

        #   Graph plot
        rcParams["font.family"] = 'malgun gothic'
        graph_window = QtWidgets.QDialog()
        graph_window.setWindowTitle('BMP 적용 전후 비교 그래프')
        m = PlotCanvas(graph_window)
        m.move(0, 0)
        graph_window.exec_()

    #   Menu - Send email function
    def action_send_mail(self):
        recipient = 'dsyang1024@kangwon.ac.kr'
        subject = '최적관리기법 앱 이메일 문의'
        body_file = open('mailsource.txt', 'w')
        body_file.write('앱 버전 = {}//\n'.format(version))
        body_file.write('앱 구동경로 = {}//\n'.format(os.getcwd()))
        body_file.write('문의 내용을 아래에 적어주세요\n-------------------------')
        body_file.close()
        with open('mailsource.txt', 'r') as b:
            body = b.read()
        webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + body, new=1)
        os.remove('mailsource.txt')

    #   Menu - Visit KNU home-page
    def action_visit_web(self):
        webbrowser.open('http://envsys.co.kr')

    #   Menu - Visit APEX home-page
    def action_visit_APEX(self):
        webbrowser.open('https://epicapex.tamu.edu/apex/')

    '''
    BMP application functions starts from here
    From BMP 1 to 6 : Structural BMPs
    From BMP 7 to 9 : Non structural BMPs

    === Mechanism explaination ===
    1. Read WINAPEX.SUB file
    2. Organize variables in the WINAPEX.SUB
    3. Backup WINAPEX.SUB as different name with time-step
    4. Change variables for BMP application
    5. Save updated .SUB as WINAPEX.SUB
    '''


    #   BMP 1  **Reach 관련 변수를 보정해야 하므로 즉각적인 효율을 평가하기가 어려움.
    def apply_bmp1(self):
        #   Grassed waterway
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']

        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters
        #   sub_data[4][1] = 0.5 #RCHDchannel 깊이 0.2로 변경
        #   sub_data[4][2] = 2  # RCBW channel 하단 너비 *모르니 0 입력값*
        #   sub_data[4][3] = 2  # RCTW channel 상단 너비 *모르니 0 입력값*
        sub_data[3][7] = 0.75  # UPN
        sub_data[3][4] = 0.1 #float(sub_data[3][4]) * 0.1  # CHN
        #sub_data[3][1] = float(sub_data[3][1])*2   #CHL Channel length
        sub_data[4][4] = float(sub_data[4][4]) * 0.3  # RCHS channel 경사도 m/m *DEM base이니 입력값*
        sub_data[4][5] = 0.4  # RCHN Manning 계수 0.4로 변경
        sub_data[4][6] = 0.0001  # RCHC USLE C factor 값 *식생수로는 침식이 어려우니 0.001*
        sub_data[4][7] = 0.3  # RCHK USLE K factor 값 *식생수로는 침식이 어려우니 0.001*

        #   writing new sub file.
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP 2
    def apply_bmp2(self):
        #   Terrace
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters
        sub_data[3][1] = float(sub_data[3][1]) * 2  # CHL Channel length
        # CHS is Mainstream channel slope 이 변수는 모의 결과에 민감한 영향을 주지 않음
        sub_data[3][4] = 0.75  # CHN
        sub_data[3][5] = 0.001  # SLP=STP
        # SPLG 하천길이를 변화하였으므로 추가 수정없음
        sub_data[3][7] = 0.75  # UPN
        sub_data[4][0] = sub_data[3][1]  # RCHL
        sub_data[4][4] = float(sub_data[4][4]) * 0.3  # RCHS channel 경사도 m/m *DEM base이니 입력값*
        sub_data[4][5] = 0.4  # RCHN Manning 계수 0.75로 변경
        sub_data[4][6] = 0.0001  # RCHC USLE C factor 값 *식생수로는 침식이 어려우니 0.001*
        sub_data[4][7] = 0.0001  # RCHK USLE K factor 값 *식생수로는 침식이 어려우니 0.001*

        #   Writing new .sub file
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP 3 web-update
    def apply_bmp3(self):
        #   Filter strips
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters
        #sub_data[3][3] = float(sub_data[3][5]) * 0.1  # CHS (Channel Slope)
        #sub_data[4][4] = float(sub_data[4][4]) * 0.3  # Set the Reach Channel Slope (RCHS) at 0.1*slope of the field.
        sub_data[3][4] = 0.2  # CHN
        #sub_data[3][5] = float(sub_data[3][5]) * 0.1  # SLP=STP
        sub_data[3][6] = 30 # SPLG
        sub_data[3][7] = 0.2  # UPN
        sub_data[4][1] = 0.1 # Set the Routing Reach Channel Depth (RCHD) to 0.1 meters.
        sub_data[6][4] = 0.99  # BCOF buffer 마찰 계수 0.99
        sub_data[6][5] = 2 * float(sub_data[3][6])  # BFFL buffer 영향 길이 2배 조정
        sub_data[9][0] = float(sub_data[9][0]) * 0.4 # erosion control factor

        #   Writing new .sub file
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")
        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP 4 **web-update
    def apply_bmp4(self):
        #   Diversion dike
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters
        sub_data[3][6] = float(sub_data[3][6]) * 3 # SPLG
        sub_data[9][0] = float(sub_data[9][0]) * 0.3  # PEC : erosion control factor
        sub_data[3][3] = float(sub_data[3][3]) * 0.5

        #   Writing new .sub file
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")
        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP 5
    def apply_bmp5(self):
        #   Grade stabilization structure
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters
        sub_data[4][0] = float(sub_data[3][1]) * 1.5  # RCHL ==> 건들지 않는 변수....
        sub_data[3][1] = float(sub_data[3][1]) * 1.5  # CHL
        sub_data[3][3] = float(sub_data[3][3]) * 0.5  # CHS (Channel Slope)
        # note: CHL과 RCHL을 변경할때는 둘다 동일한 값으로 변경해줘야 모의 가능
        print("sub_data[4][4] = " + str(float(sub_data[4][4]) * 0.1))

        #   Writing new .sub file
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")
        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP 6 is not available now (2019-05-23)
    '''
    #   BMP 6
    def apply_bmp5(self):
        #   "BMP NAME"
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir+"/WINAPEX.SUB",'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',input_dir +'/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB',input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB',input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters
        #   Empty as of now === === === ===

        #   Writing new .sub file
        newsub = open(input_dir+"/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")
        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)
    '''


    #   BMP 7
    def apply_bmp7(self):
        #   Fertilizer 50%
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters => Below is source code for decreased fertilizer data (50%)
        #   Opening file
        ops = sub_data[1][1]
        print (ops+" : 작물 번호 입력값")
        opsf = open(apex_dir+'/'+ops+'.ops','r')
        ops_data = opsf.readlines()

        #   Split and organize data for writing down new .OPS file
        for i in range(len(ops_data)):
            ops_data[i] = ops_data[i].replace('\n','')
            ops_data[i] = ops_data[i].replace('\t',' ')
            ops_data[i] = ops_data[i].split(' ')
        for i in range(len(ops_data)):
            for r in range(len(ops_data[i])):
                ops_data[i] = [x for x in ops_data[i] if x != '']

        for i in range(2,len(ops_data)):
            if int(ops_data[i][6]) >= 52 and int(ops_data[i][6])<= 54:
                ops_data[i][7] = str(round(float(ops_data[i][7])*0.5,1))

        #   NEW .OPS file 600.OPS made below
        new_opsf = open(apex_dir+'/600.ops','w')
        new_opsf.write('   ')
        for i in range(len(ops_data[0])):
            new_opsf.write(ops_data[0][i]+' ')    
        new_opsf.write('\n')  
        [new_opsf.write("{:>4}".format(i)) for i in ops_data[1]]
        new_opsf.write('\n')
        for i in range(2,len(ops_data)):
            for r in range(0,3):
                new_opsf.write("{:>3}".format(ops_data[i][r]))
            for r in range(3,7):
                new_opsf.write("{:>5}".format(ops_data[i][r]))
            for r in range(7,14):
                new_opsf.write("{:>8}".format(ops_data[i][r]))
            new_opsf.write('    ')
            for r in range(14,len(ops_data[i])):
                new_opsf.write(' '+(ops_data[i][r]))
            new_opsf.write('\n')

        #   Writing new .sub file
        sub_data[1][1] = 600
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")
        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP 8
    def apply_bmp8(self):
        #   Fertilizer 70%
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters => Below is source code for decreased fertilizer data (50%)
        #   Opening file
        ops = sub_data[1][1]
        print (ops+" : 작물 번호 입력값")
        opsf = open(apex_dir+'/'+ops+'.ops','r')
        ops_data = opsf.readlines()

        #   Split and organize data for writing down new .OPS file
        for i in range(len(ops_data)):
            ops_data[i] = ops_data[i].replace('\n','')
            ops_data[i] = ops_data[i].replace('\t',' ')
            ops_data[i] = ops_data[i].split(' ')
        for i in range(len(ops_data)):
            for r in range(len(ops_data[i])):
                ops_data[i] = [x for x in ops_data[i] if x != '']

        for i in range(2,len(ops_data)):
            if int(ops_data[i][6]) >= 52 and int(ops_data[i][6])<= 54:
                ops_data[i][7] = str(round(float(ops_data[i][7])*0.7,1))

        #   NEW .OPS file 600.OPS made below
        new_opsf = open(apex_dir+'/600.ops','w')
        new_opsf.write('   ')
        for i in range(len(ops_data[0])):
            new_opsf.write(ops_data[0][i]+' ')    
        new_opsf.write('\n') 
        [new_opsf.write("{:>4}".format(i)) for i in ops_data[1]]
        new_opsf.write('\n')
        for i in range(2,len(ops_data)):
            for r in range(0,3):
                new_opsf.write("{:>3}".format(ops_data[i][r]))
            for r in range(3,7):
                new_opsf.write("{:>5}".format(ops_data[i][r]))
            for r in range(7,14):
                new_opsf.write("{:>8}".format(ops_data[i][r]))
            new_opsf.write('    ')
            for r in range(14,len(ops_data[i])):
                new_opsf.write(' '+(ops_data[i][r]))
            new_opsf.write('\n')

        #   Writing new .sub file
        sub_data[1][1] = 600
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")
        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP 9
    def apply_bmp9(self):
        #   No till
        from time import strftime
        global input_dir
        #   Organize variables and backup WINAPEX.SUB
        sub = open(input_dir + "/WINAPEX.SUB", 'r')
        sub_data = sub.readlines()
        sub.close()
        for i in range(len(sub_data)):
            sub_data[i] = sub_data[i].replace('\n', '')
            sub_data[i] = sub_data[i].split(' ')
        for i in range(len(sub_data)):
            for r in range(len(sub_data[i])):
                sub_data[i] = [x for x in sub_data[i] if x != '']
        #   Make new .sub file
        sub_files = os.listdir(input_dir)
        sub_files = [x for x in sub_files if x.startswith("WINAPEX") and x.endswith(".SUB")]
        if len(sub_files) > 1:
            if 'WINAPEX_origin.SUB' in sub_files:
                os.rename(input_dir + '/WINAPEX.SUB',
                          input_dir + '/WINAPEX_{}.SUB'.format(strftime('%H_%M_%S')))  # subfile backup
            else:
                os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup
        else:
            os.rename(input_dir + '/WINAPEX.SUB', input_dir + '/WINAPEX_origin.SUB')  # subfile backup

        #   Update parameters => Below is source code for decreased fertilizer data (50%)
        #   Opening file
        ops = sub_data[1][1]
        print (ops+" : 작물 번호 입력값")
        opsf = open(apex_dir+'/'+ops+'.ops','r')
        ops_data = opsf.readlines()

        #   Split and organize data for writing down new .OPS file
        for i in range(len(ops_data)):
            ops_data[i] = ops_data[i].replace('\n','')
            ops_data[i] = ops_data[i].replace('\t',' ')
            ops_data[i] = ops_data[i].split(' ')
        for i in range(len(ops_data)):
            for r in range(len(ops_data[i])):
                ops_data[i] = [x for x in ops_data[i] if x != '']

        new_ops_data = []
        for i in range(2,len(ops_data)):
            if ops_data[i][-1] != "Tillage":
                new_ops_data.append(ops_data[i])
        #   NEW .OPS file 600.OPS made below
        new_opsf = open(apex_dir+'/600.ops','w')
        new_opsf.write('   ')
        for i in range(len(ops_data[0])):
            new_opsf.write(ops_data[0][i]+' ')    
        new_opsf.write('\n') 
        [new_opsf.write("{:>4}".format(i)) for i in ops_data[1]]
        new_opsf.write('\n')
        for i in range(len(new_ops_data)):
            for r in range(0,3):
                new_opsf.write("{:>3}".format(new_ops_data[i][r]))
            for r in range(3,7):
                new_opsf.write("{:>5}".format(new_ops_data[i][r]))
            for r in range(7,14):
                new_opsf.write("{:>8}".format(new_ops_data[i][r]))
            new_opsf.write('    ')
            for r in range(14,len(new_ops_data[i])):
                new_opsf.write(' '+(new_ops_data[i][r]))
            new_opsf.write('\n')

        #   Writing new .sub file
        sub_data[1][1] = 600
        newsub = open(input_dir + "/WINAPEX.SUB", 'w')
        for r in sub_data[:2]:
            for i in range(len(r)):
                newsub.write("{:>8}".format(int(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")

        for r in sub_data[2:]:
            for i in range(len(r)):
                newsub.write("{:>10.4f}".format(float(r[i])))
                if i == len(r) - 1:
                    newsub.write("\n")
        newsub.close()
        self.bmp_applied_window()
        self.btn_field_check.setEnabled(True)
        self.btn_reset.setEnabled(True)


    #   BMP confirm Popup
    def bmp_applied_window(self):
        d = QtWidgets.QDialog()
        t1 = QtWidgets.QLabel('SUCCESS!\nBMP APPLIED!', d)
        vbox = QtWidgets.QVBoxLayout()
        b1 = QtWidgets.QPushButton('ok', d)
        vbox.addWidget(t1)
        vbox.addWidget(b1)
        vbox.addStretch()
        d.setLayout(vbox)
        d.setWindowTitle('Message')
        b1.clicked.connect(d.close)
        d.exec_()
        self.btn_compare.setEnabled(True)


#   This class is for graph plot for pre & post BMP compare
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=6, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        #   Graph plot function
        #   Flow Graph
        ax1 = self.figure.add_subplot(211)
        ax1.set_title("최적관리기법 적용 전후 비교")
        ax1.plot(YR_compare, Q_compare[0], 'r--', label='BMP 적용 전')
        ax1.plot(YR_compare, Q_compare[1], 'b-', label='BMP 적용 후')
        ax1.set_ylabel("직접유출량 (mm/yr)")
        ax1.legend(loc='upper right', fontsize=8)

        #   TN Graph
        ax2 = self.figure.add_subplot(212)
        ax2.plot(YR_compare, TN_compare[0], 'r--', label='BMP 적용 전')
        ax2.plot(YR_compare, TN_compare[1], 'b-', label='BMP 적용 후')
        ax2.set_xlabel("연도")
        ax2.set_ylabel("N부하량 (kg/ha/yr)")
        self.draw()


'''
Systemical Part
Do not Edit below
'''
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())