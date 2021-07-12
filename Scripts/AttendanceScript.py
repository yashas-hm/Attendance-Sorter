import os
import pandas as pd
from datetime import datetime
import pandas.errors


class AttendanceEvaluation:
    def __init__(self, data, filepath):
        self.roll_no = []
        self.filepath = filepath
        try:
            self.df = pd.read_csv(filepath)
        except (FileNotFoundError, pandas.errors.EmptyDataError):
            self.df = pd.DataFrame()
        self.data = data
        self.updater = {}
        self.get_attendance()

    def update(self, rno):
        list_col = self.df.columns

        self.updater['Enrollment Number'] = rno

        for i in range(1, len(list_col)):
            self.updater[i] = 'A'

    def get_attendance(self):
        array = self.data.split('\n')
        for i in array:
            i = str(i)
            i = i.upper()
            if i.startswith('IU'):
                if not self.roll_no.__contains__(i):
                    self.roll_no.append(i)

    def start_evaluation(self):
        if not self.df.empty:
            self.df = self.df.sort_values(by=['Enrollment Number'])
        else:
            self.df['Enrollment Number'] = self.roll_no
            self.df = self.df.sort_values(by=['Enrollment Number'])

        self.df = self.df.set_index(['Enrollment Number'])

        curr_rno = list(self.df.index)
        for i in self.roll_no:
            if not curr_rno.__contains__(i):
                self.update(i)
                self.df.append(self.updater)
                self.updater.clear()

        today = datetime.now().strftime('%d.%m.%Y')
        self.df[today] = self.set_attendance_today()

        os.remove(self.filepath)
        self.df.to_csv(self.filepath)
        return 'Evaluation Complete'

    def set_attendance_today(self):
        present = []
        class_rno = self.df.index
        for i in class_rno:
            if self.roll_no.__contains__(i):
                present.append('P')
            else:
                present.append('A')
        return present
