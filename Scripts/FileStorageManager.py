import os
import tkinter as tk
from Scripts import PopUpManager


class FileStore:
    def __init__(self, root, label):
        self.desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        self.path = os.path.join(self.desktop_path, 'Attendance Sorter')
        self.filepath = ''
        self.root = root
        self.label = label

    def check_file(self):
        try:
            os.mkdir(self.path, 0o666)
        except FileExistsError:
            print('Already Exists')

        arr = self.get_files()
        if len(arr) == 0:
            self.new_file()
        else:
            self.open_file()

    def change_label(self, text):
        self.label['text'] = text

    def new_file(self):
        new_window = tk.Toplevel(self.root)
        new_window.geometry('280x140+600+300')
        new_window['pady'] = 8
        new_window['padx'] = 8
        new_window.title('New File')

        new_window.rowconfigure(0, weight=2)
        new_window.rowconfigure(1, weight=6)
        new_window.rowconfigure(2, weight=1)
        new_window.columnconfigure(0, weight=10)
        new_window.columnconfigure(1, weight=10)
        new_window.columnconfigure(2, weight=10)

        entry = tk.Entry(new_window)
        entry.grid(row=0, column=0, columnspan=3, sticky='nsew')

        def submit():
            filename = str(entry.get()).strip()
            if filename == '':
                PopUpManager.error_popup(new_window, 'Cannot create file with empty name.')
            else:
                self.filepath = os.path.join(self.path, filename + '.csv')
                try:
                    file = open(self.filepath, 'x')
                    file.close()
                    self.change_label(filename + '.csv')
                    new_window.destroy()
                except FileExistsError:
                    PopUpManager.error_popup(new_window, 'File with same name already exists.')

        button = tk.Button(new_window, text='Create', command=submit)
        button.grid(row=2, column=1, sticky='nsew')

        new_window.mainloop()

    def open_file(self):
        list_window = tk.Toplevel(self.root)

        list_window.geometry('240x280+600+300')
        list_window['pady'] = 8
        list_window['padx'] = 8
        list_window.title('Choose File')

        list_window.rowconfigure(0, weight=10)
        list_window.rowconfigure(1, weight=2)
        list_window.columnconfigure(0, weight=10)
        list_window.columnconfigure(1, weight=10)
        list_window.columnconfigure(2, weight=10)

        list_view = tk.Listbox(list_window)
        list_view.grid(row=0, column=0, columnspan=3, sticky='nsew')
        list_view.config(border=2, relief='sunken')

        files = self.get_files()
        for i in files:
            list_view.insert(tk.END, i)

        def select():
            try:
                self.filepath = os.path.join(self.path, str(list_view.selection_get()))
                self.change_label(str(list_view.selection_get()))
                list_window.destroy()
            except tk.TclError:
                PopUpManager.error_popup(list_view, 'No file selected.')

        button = tk.Button(list_window, text='Open', command=select)
        button.grid(row=1, column=1, sticky='nsew')

        list_window.mainloop()

    def get_files(self):
        arr = []
        for i in os.listdir(self.path):
            if i.endswith('.csv'):
                arr.append(i)
        return arr
