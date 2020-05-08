# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'draw_memory.ui'

#

# Created by: PyQt5 UI code generator 5.14.1

#

# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from tkinter import *
from tkinter import messagebox

componects = dict()

canvas = Canvas(width=600, height=800, bg='white')


def draw_mem(x, y, z):
    canvas.delete("all")
    canvas.pack(expand=YES, fill=BOTH)

    canvas.create_rectangle(100, 50, 300, 50 + 600, width=5, outline='#DC143C', fill='#DC143C')

    canvas.create_rectangle(450, 75, 490, 100 + 50, width=5, outline='#000000', fill='#DC143C')
    canvas.create_rectangle(450, 125, 490, 150 + 50, width=5, outline='#000000', fill='#ffe873')
    canvas.create_rectangle(450, 175, 490, 175 + 50, width=5, outline='#000000', fill='#ebebeb')

    canvas.create_text(548, 100, text='Memory Allocation')
    canvas.create_text(545, 150, text='Process Allocation')
    canvas.create_text(508, 200, text='Hole')

    canvas.create_text(80, 50, text='0')

    canvas.create_text(80, 600 + 50, text=z)

    for i in range(len(x)):
        x[i] = int(x[i])

        y[i] = int(y[i])

        canvas.create_rectangle(100, (((x[i] / z) * 600) + 50), 300, ((((x[i] + y[i]) / z) * 600) + 50), width=5,
                                outline='#ebebeb', fill='#ebebeb')

        canvas.create_text(80, (((x[i] / z) * 600) + 50), text=x[i], font=("Purisa", 8))

        canvas.create_text(80, ((((x[i] + y[i]) / z) * 600) + 50), text=x[i] + y[i], font=("Purisa", 8))


def draw_segment(base, size, name, z):
    rect = canvas.create_rectangle(100, ((base / z) * 600) + 50, 300, (((base + size) / z) * 600) + 50, width=5,
                                   outline='#ffe873', fill='#ffe873')

    l1 = canvas.create_line(98, ((base / z) * 600) + 50 - 2, 303, ((base / z) * 600) + 50 - 2)
    l2 = canvas.create_line(98, (((base + size) / z) * 600) + 50 + 2, 303, (((base + size) / z) * 600) + 50 + 2)

    t1 = canvas.create_text(320, ((base / z) * 600) + 50, text=str(base), font=("Purisa", 8))

    t2 = canvas.create_text(320, (((base + size) / z) * 600) + 50, text=base + size, font=("Purisa", 8))

    t3 = canvas.create_text(180, (((((base + size) / z) * 600) + ((base / z) * 600)) / 2) + 50, text=name,
                            font=("Purisa", 8))

    rect_list = [rect, t1, t2, t3, l1, l2]

    componects[base] = rect_list


def clear_segement(base):
    canvas.delete(componects[base][0])
    canvas.delete(componects[base][1])
    canvas.delete(componects[base][2])
    canvas.delete(componects[base][3])
    canvas.delete(componects[base][4])
    canvas.delete(componects[base][5])


def clear_rect(base, size,z):
    canvas.create_rectangle(100, ((base / z) * 600) + 50, 300, (((base + size) / z) * 600) + 50, width=5,
                                   outline='#ebebeb', fill='#ebebeb')



    canvas.create_text(320, ((base / z) * 600) + 50, text=str(base), font=("Purisa", 8))

    canvas.create_text(320, (((base + size) / z) * 600) + 50, text=base + size, font=("Purisa", 8))

    # canvas.create_text(180, (((((base + size) / z) * 600) + ((base / z) * 600)) / 2) + 50, text=name,
    #                         font=("Purisa", 8))



class first(object):
    holes_base = None

    holes_size = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(860, 714)

        MainWindow.setFixedSize(860, 714)

        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(260, 560, 301, 81))

        self.pushButton.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                      "background:red;\n"

                                      "color:white;\n"

                                      "border-radius:12px;")

        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit.setGeometry(QtCore.QRect(60, 210, 301, 311))

        self.textEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_2.setGeometry(QtCore.QRect(450, 210, 281, 311))

        self.textEdit_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit_2.setObjectName("textEdit_2")

        self.label = QtWidgets.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(40, 150, 341, 61))

        self.label.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                 "background:red;\n"

                                 "color:white;\n"

                                 "border-radius:12px;")

        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)

        self.label_2.setGeometry(QtCore.QRect(420, 150, 341, 61))

        self.label_2.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                   "background:red;\n"

                                   "color:white;\n"

                                   "border-radius:12px;")

        self.label_2.setObjectName("label_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_3.setGeometry(QtCore.QRect(450, 30, 181, 61))

        self.textEdit_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit_3.setObjectName("textEdit_3")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)

        self.label_3.setGeometry(QtCore.QRect(60, 30, 341, 61))

        self.label_3.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                   "background: red;\n"

                                   "color:white;\n"

                                   "border-radius:12px;")

        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.click)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):
        value_of_textedit_1 = self.textEdit.toPlainText()

        self.holes_size = value_of_textedit_1.splitlines()

        value_of_textedit_2 = self.textEdit_2.toPlainText()

        z = int(self.textEdit_3.toPlainText())

        self.holes_base = value_of_textedit_2.splitlines()

        draw_mem(self.holes_base, self.holes_size, z)

        self.window = QtWidgets.QMainWindow()

        self.ui = last(self.holes_base, self.holes_size, z)

        self.ui.setupUi(self.window)

        self.window.show()

    def get_att(self):
        return self.holes_size, self.holes_base

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "Draw"))

        self.label.setText(_translate("MainWindow", "    Enter holes Area"))

        self.label_2.setText(_translate("MainWindow", "  Enter holes postion"))

        self.label_3.setText(_translate("MainWindow", " Enter Memoy Size"))


class last(object):

    def __init__(self, h_b, h_s, mem_size, Process_Dict=None):
        self.H_base = h_b
        self.H_size = h_s
        self.p = 1
        self.Mem_size = mem_size
        if Process_Dict == None:
            self.Process_Dict = dict()
        else:
            self.Process_Dict = dict(Process_Dict)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 795)
        MainWindow.setStyleSheet("\n"

                                 "\n"

                                 "")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(40, 150, 171, 41))
        self.radioButton.setStyleSheet("font: 20pt \"MV Boli\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 150, 171, 41))

        self.radioButton_2.setStyleSheet("font: 20pt \"MV Boli\";")

        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(80, 640, 211, 61))

        self.pushButton.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                      "background:red;\n"

                                      "color:white;\n"

                                      "border-radius:12px;")

        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)

        self.label_2.setGeometry(QtCore.QRect(30, 60, 431, 61))

        self.label_2.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                   "background:red;\n"

                                   "color:white;\n"

                                   "border-radius:12px;")

        self.label_2.setObjectName("label_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_3.setGeometry(QtCore.QRect(270, 350, 151, 181))

        self.textEdit_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_4.setGeometry(QtCore.QRect(70, 350, 161, 181))

        self.textEdit_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit_4.setObjectName("textEdit_4")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)

        self.label_3.setGeometry(QtCore.QRect(30, 290, 461, 61))

        self.label_3.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                   "background:red;\n"

                                   "color:white;\n"

                                   "border-radius:12px;")

        self.label_3.setObjectName("label_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton_2.setGeometry(QtCore.QRect(830, 640, 191, 61))

        self.pushButton_2.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                        "background:red;\n"

                                        "color:white;\n"

                                        "\n"

                                        "border-radius:12px;")

        self.pushButton_2.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)

        self.label_4.setGeometry(QtCore.QRect(590, 480, 461, 61))

        self.label_4.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                   "background:red;\n"

                                   "color:white;\n"

                                   "border-radius:12px;")

        self.label_4.setObjectName("label_4")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)

        self.radioButton_3.setGeometry(QtCore.QRect(640, 150, 171, 41))

        self.radioButton_3.setStyleSheet("font: 20pt \"MV Boli\";")

        self.radioButton_3.setObjectName("radioButton_3")

        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_6.setGeometry(QtCore.QRect(680, 540, 271, 61))

        self.textEdit_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit_6.setObjectName("textEdit_6")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)

        self.radioButton_4.setGeometry(QtCore.QRect(840, 150, 171, 41))

        self.radioButton_4.setStyleSheet("font: 20pt \"MV Boli\";")

        self.radioButton_4.setObjectName("radioButton_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)

        self.label_5.setGeometry(QtCore.QRect(610, 60, 451, 61))

        self.label_5.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                   "background:red;\n"

                                   "color:white;\n"

                                   "border-radius:12px;")

        self.label_5.setObjectName("label_5")

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_5.setGeometry(QtCore.QRect(800, 340, 151, 61))

        self.textEdit_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit_5.setObjectName("textEdit_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)

        self.label_6.setGeometry(QtCore.QRect(580, 280, 461, 61))

        self.label_6.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                   "background:red;\n"

                                   "color:white;\n"

                                   "border-radius:12px;")

        self.label_6.setObjectName("label_6")

        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)

        self.textEdit_7.setGeometry(QtCore.QRect(610, 340, 161, 61))

        self.textEdit_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")

        self.textEdit_7.setObjectName("textEdit_7")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton_3.setGeometry(QtCore.QRect(400, 640, 301, 61))

        self.pushButton_3.setStyleSheet("font: 20pt \"MV Boli\";\n"

                                        "background:red;\n"

                                        "color:white;\n"

                                        "\n"

                                        "border-radius:12px;")

        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setFixedSize(1125, 795)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.deallocate)

        self.pushButton_3.clicked.connect(self.draw_tabel)

        self.pushButton.clicked.connect(self.allocate)

    def draw_tabel(self):

        process_name = self.textEdit_6.toPlainText()
        val = """Segment Name\tBase Address\tSize\n{}  \t\t{}  \t\t{}\n{}  \t\t{}  \t\t{}\n{}  \t\t{}  \t\t{}""".format(
            self.Process_Dict[process_name][0][0],
            self.Process_Dict[process_name][1][0], self.Process_Dict[process_name][2][0],
            self.Process_Dict[process_name][0][1],
            self.Process_Dict[process_name][1][1], self.Process_Dict[process_name][2][1],
            self.Process_Dict[process_name][0][2],
            self.Process_Dict[process_name][1][2], self.Process_Dict[process_name][2][2])
        messagebox.showinfo("Address Table For " + process_name, val)

    def deallocate(self):

        by_postion = radioButton_4.isChecked()

        by_name = radioButton_3.isChecked()

        address = int(self.textEdit_7.toPlainText())

        area = int(self.textEdit_5.toPlainText())

        process_name = int(self.textEdit_6.toPlainText())

        # variables are by_postion ,by_name these are the values of radio buttons

        # address, area ,process_name values in text boxes

    def allocate(self):

        first_fit = self.radioButton.isChecked()

        best_fit = self.radioButton_2.isChecked()

        value_of_textedit_4 = self.textEdit_4.toPlainText()

        segments_name = value_of_textedit_4.splitlines()

        value_of_textedit_3 = self.textEdit_3.toPlainText()

        seg_s = value_of_textedit_3.splitlines()

        segments_size = [float(i) for i in seg_s]
        ##sort by bigger
        for i in range(len(segments_size)):
            swapped=False
            for j in range(len(segments_size)-(i+1)):
                if(segments_size[j] < segments_size[j+1]):
                    segments_size[j],segments_size[j+1] = segments_size[j+1],segments_size[j]
                    segments_name[j],segments_name[j+1] = segments_name[j+1],segments_name[j]
                    swapped=True
            if(swapped==False):
                break
        ###THOSE ARE THE BASE & SIZE OF THE HOLES

        ###BE CAREFUL WITH THE """""""""""""self""""""""" WORD DON'T FORGET TO USE IT

        # self.H_base

        # self.H_size

        # this is the dictionary of processes and their segment names and base addresses and sizes any segment located

        ##please but the data in process dict with the key as process name with P1 or P2 ...etc and the

        # value is list of 3 lists [[segment names list],[segments base addresses list],[segment size list]]

        # self.Process_Dict

        # variables are first_fit , best_fit these are the values of radio buttons

        # segments_name, segments_size are 2 lists of segments data you need to complete drawing

        if (best_fit):

            if (sum(self.H_size) >= sum(segments_size)):

                indeces = []

                H_s = list(self.H_size)

                for i in range(len(segments_size)):

                    min_value = 10000000000

                    min_index = -1

                    for j in range(len(H_s)):

                        if ((H_s[j] - segments_size[i]) < min_value and (H_s[j] - segments_size[i]) >= 0):
                            min_value = H_s[j] - segments_size[i]

                            min_index = j

                    if (min_index >= 0):
                        indeces.append(min_index)

                        H_s[min_index] -= segments_size[i]

                if (len(indeces) == len(segments_size)):

                    seg_name = []

                    seg_size = []

                    seg_base = []

                    i = 0

                    for index in indeces:
                        seg_name.append(segments_name[i])

                        seg_size.append(segments_size[i])

                        seg_base.append(self.H_base[index])

                        draw_segment(self.H_base[index], segments_size[i], 'P{}-'.format(self.p) + segments_name[i],
                                     self.Mem_size)

                        self.H_base[index] += segments_size[i]

                        i += 1

                    self.H_size = list(H_s)

                    p_name = 'P{}'.format(self.p)

                    self.p += 1
                    self.Process_Dict[p_name] = [seg_name, seg_base, seg_size]
                else:
                    messagebox.showerror("Space Error", 'No Enough Memory to allocate')

            else:
                messagebox.showerror("Space Error", 'No Enough Memory to allocate')




        # elif (first_fit):
        #     if (sum(self.H_size) >= sum(segments_size)):
        #
        #         indeces = []
        #
        #         H_s = list(self.H_size)
        #
        #         for i in range(len(segments_size)):
        #
        #             index = -1
        #
        #             for j in range(len(H_s)):
        #
        #                 if (H_s[j] >= segments_size[i]):
        #                     index = j
        #
        #                     break
        #
        #             if (index >= 0):
        #                 indeces.append(index)
        #
        #                 H_s[index] -= segments_size[i]
        #
        #         if (len(indeces) == len(segments_size)):
        #
        #             seg_name = []
        #
        #             seg_size = []
        #
        #             seg_base = []
        #
        #             i = 0
        #
        #             for index in indeces:
        #                 seg_name.append(segments_name[i])
        #
        #                 seg_size.append(segments_size[i])
        #
        #                 seg_base.append(self.H_base[index])
        #
        #                 draw_segment(self.H_base[index], segments_size[i], 'P{}-'.format(self.p) + segments_name[i],
        #                              self.Mem_size)
        #
        #                 self.H_base[index] += segments_size[i]
        #
        #                 i += 1
        #
        #             self.H_size = list(H_s)
        #
        #             p_name = 'P{}'.format(self.p)
        #
        #             self.p += 1
        #
        #             self.Process_Dict[p_name] = [seg_name, seg_base, seg_size]
        elif (first_fit):
                if sum(self.H_size) >= sum(segments_size) and max(self.H_size) >= max(segments_size):
                    hole_size = self.H_size.copy()
                    hole_base = self.H_base.copy()
                    is_valid = 0
                    seg_name = []
                    seg_base = []
                    seg_size = []

                    for x in range(len(segments_size)):
                        for y in range(len(segments_size)):
                            if hole_size[y] >= segments_size[x]:
                                seg_name.append(segments_name[x])
                                seg_size.append(segments_size[x])
                                seg_base.append(hole_base[y])
                                hole_size[y] = hole_size[y] - segments_size[x]
                                hole_base[y] = hole_base[y] + segments_size[x]
                                is_valid += 1
                                break

                    if (is_valid == len(segments_size)):
                        for i in range(len(segments_size)):
                            draw_segment(seg_base[i], seg_size[i], 'P{}-'.format(self.p) + seg_name[i],
                                         self.Mem_size)
                        self.H_size = hole_size.copy()
                        self.H_base = hole_base.copy()
                        p_name = 'P{}'.format(self.p)
                        self.p += 1
                        self.Process_Dict[p_name] = [seg_name, seg_base, seg_size]
                    else:
                        messagebox.showerror("Space Error", 'No Enough Memory to allocate')
                else:
                    messagebox.showerror("Space Error", 'No Enough Memory to allocate')


        else:
            messagebox.showerror('Error', 'Please Choose Best-fit or First-fit algorithim')

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.radioButton.setText(_translate("MainWindow", " First-fit"))

        self.radioButton_2.setText(_translate("MainWindow", "Best-fit"))

        self.pushButton.setText(_translate("MainWindow", "Allocate"))

        self.label_2.setText(_translate("MainWindow", "  Choose the type of allocation"))

        self.label_3.setText(_translate("MainWindow", "  Enter Segements Name & Area"))

        self.pushButton_2.setText(_translate("MainWindow", "deallocate"))

        self.label_4.setText(_translate("MainWindow", "  Enter process name"))

        self.radioButton_3.setText(_translate("MainWindow", "By_Name"))

        self.radioButton_4.setText(_translate("MainWindow", "By_postion"))

        self.label_5.setText(_translate("MainWindow", "  Choose the type of deallocation"))

        self.label_6.setText(_translate("MainWindow", "  Enter Base address & Area"))

        self.pushButton_3.setText(_translate("MainWindow", " draw tabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = first()

    ui.setupUi(MainWindow)

    MainWindow.show()

    mainloop()

    sys.exit(app.exec_())
