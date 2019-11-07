from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import datetime, csv


form1, base1 = uic.loadUiType('assets/main.ui')


class MAIN(base1, form1):
    def __init__(self):
        super(base1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.stats)

    # this method will store the stats

    def save(self):
        # list of items to be checked for True
        exer = None
        stud = None
        cont = None
        dance = None
        focus = None
        book = None
        song = None
        stalk = None
        connect = None
        right = None
        work = None
        suff = None
        sample = None
        saved = None

        # check for checked items
        if self.checkBox.isChecked():
            exer = True
        else:
            exer = False

        if self.checkBox_2.isChecked():
            stud = True
        else:
            stud = False
        if self.checkBox_3.isChecked():
            cont = True
        else:
            cont = False
        if self.checkBox_4.isChecked():
            dance = True
        else:
            dance = False
        if self.checkBox_5.isChecked():
            focus = True
        else:
            focus = False
        if self.checkBox_6.isChecked():
            book = True
        else:
            book = False
        if self.checkBox_7.isChecked():
            song = True
        else:
            song = False
        if self.checkBox_8.isChecked():
            stalk = True
        else:
            stalk = False
        if self.checkBox_9.isChecked():
            connect = True
        else:
            connect = False
        if self.checkBox_10.isChecked():
            right = True
        else:
            right = False
        if self.checkBox_11.isChecked():
            work = True
        else:
            work = False
        if self.checkBox_12.isChecked():
            suff = True
        else:
            suff = False
        if self.checkBox_13.isChecked():
            sample = True
        else:
            sample = False
        if self.checkBox_14.isChecked():
            saved = True
        else:
            saved = False

        # get the date
        date = str(datetime.date.today())

        # list of checked items to get number of True
        # and number of False values

        data_list = [exer, stud, cont, dance, focus, book, song, stalk, connect, right, work, suff, sample, saved]


        '''this method takes one argument i.e., a list of data to process
        and returns a tuple of true and false like this
        (true, false)
        this tuple is further used to write in the data.csv
        '''
        def count(dat):
            true = 0
            false = 0

            for x in dat:
                if x == True:
                    true += 1
                else:
                    false += 1

            return true, false

        coun_t = count(data_list)
        true = coun_t[0]
        false = coun_t[1]

        '''
        below method takes 3 arguments and then writes it to a csv file
        under the directory /assets/data.csv'''

        def write_to_csv(date, true, false):
            file = 'assets/data.csv'
            fields = [date, true, false]

            with open(file, 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(fields)

        write_to_csv(date, true, false)

    # this method will display stats
    def stats(self):
        self.window = PERFOR_STAT()
        self.window.show()
        self.close()

form_2, base_2 = uic.loadUiType('assets/perfrom_stat.ui')


class PERFOR_STAT(base_2, form_2):
    def __init__(self):
        super(base_2, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.quit)

    def quit(self):
        self.close()

if __name__ == '__main__':
    import sys

    ex = QApplication(sys.argv)
    app = MAIN()
    app.show()
    sys.exit(ex.exec_())
