import tkinter as tk

from AttendanceScript import AttendanceEvaluation
import FileStorageManager
import PopUpManager


class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.data = tk.StringVar()
        self.entry = tk.Text(self.window)
        self.label = tk.Label(self.window, text='None Selected')
        self.file_store = FileStorageManager.FileStore(root=self.window, label=self.label)

    def setup(self):
        self.create_window()
        self.configure_window()
        self.create_menu()
        self.create_entry()
        self.create_label()
        self.create_button()
        self.file_store.check_file()

    def mainloop(self):
        self.window.mainloop()

    def create_window(self):
        self.window.title('Attendance Sorter')
        self.window.geometry('640x480+400+200')
        self.window['padx'] = 8
        self.window['pady'] = 8

    def configure_window(self):
        self.window.rowconfigure(0, weight=40)
        self.window.rowconfigure(1, weight=40)
        self.window.rowconfigure(2, weight=40)
        self.window.rowconfigure(3, weight=40)
        self.window.columnconfigure(0, weight=40)
        self.window.columnconfigure(1, weight=40)
        self.window.columnconfigure(2, weight=40)

    def create_menu(self):

        def destroy():
            self.window.destroy()

        def open_about():
            PopUpManager.about_us_popup(self.window)

        menu = tk.Menu(self.window)

        file_menu = tk.Menu(self.window, tearoff=0)
        file_menu.add_command(label='New', command=self.file_store.new_file)
        file_menu.add_command(label='Open', command=self.file_store.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=destroy)

        help_menu = tk.Menu(self.window, tearoff=0)
        help_menu.add_command(label='How To Use')
        help_menu.add_command(label='About', command=open_about)

        menu.add_cascade(label='File', menu=file_menu)
        menu.add_cascade(label='Help', menu=help_menu)
        menu.add_command(label='Exit', command=destroy)

        self.window.config(menu=menu)

    def create_entry(self):
        self.entry.grid(row=0, column=0, columnspan=3, rowspan=2, sticky='new')

    def create_label(self):
        self.label.grid(row=2, column=1, sticky='nsew')

    def create_button(self):
        button = tk.Button(self.window, text='Evaluate Attendance', command=self.submit)
        button.grid(row=3, column=1, sticky='nsew')

    def submit(self):
        text = self.entry.get(1.0, 'end-1c')
        complete = AttendanceEvaluation(text, self.file_store.filepath).start_evaluation()
        self.label['text'] = complete
        self.entry.delete(1.0, 'end')
