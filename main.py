from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import datetime, csv
import numpy as np


form1, base1 = uic.loadUiType('assets/main.ui')
date = "Today's date is"+"\n"+str(datetime.date.today())

class MAIN(base1, form1):
    def __init__(self):
        super(base1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.stats)
        self.label_2.setText(date)

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
        
        report = self.report_gen()
        self.label_2.setText(report)

    
    def report_gen(self):
        path = '/home/shreesh/Project/Performance-Stat/assets/data.csv'

        file = open(path, 'r')
        csv_file = csv.reader(file)


        date = []
        true = []
        false = []

        for row in csv_file:
            date.append(row[0])
            true.append(int(row[1]))
            false.append(int(row[2]))
            

        date = np.array(date)
        true = np.array(true)
        false = np.array(false)

        number_of_days = len(date)
        true_avg = int(np.mean(true))
        false_avg = int(np.mean(false))
        max_true = np.max(true)
        max_false = np.max(false)
        max_true_day = date[np.argmax(true, axis=0)]
        max_false_day = date[np.argmax(false, axis=0)]

        report = f'''
        Average task performed during the period of {number_of_days} days is {true_avg}.
        Average task's not performed during the period of {number_of_days} days is {false_avg}.
        Maximum performing day was {max_true_day} with {max_true} task's performed.
        Least performing day was {max_false_day} with {max_false} task's not performed.

        Day 1 of observation is {date[0]}, Last day of observation is {date[-1]}.
        '''
        return report

    def quit(self):
        self.close()

if __name__ == '__main__':
    import sys

    ex = QApplication(sys.argv)
    app = MAIN()
    app.show()
    sys.exit(ex.exec_())
