import tkinter as tk


def error_popup(root, text):
    def ok():
        error_window.destroy()

    error_window = tk.Toplevel(root)
    error_window.title('Error')
    error_window.geometry('220x80+600+300')
    error_window['padx'] = 10
    error_window['pady'] = 10

    error_window.rowconfigure(0, weight=10)
    error_window.rowconfigure(1, weight=10)
    error_window.columnconfigure(0, weight=10)
    error_window.columnconfigure(1, weight=10)
    error_window.columnconfigure(2, weight=10)

    error_label = tk.Label(error_window, text=text, wraplength=300)
    error_label.grid(row=0, column=0, columnspan=3, sticky='nsw')

    ok_btn = tk.Button(error_window, text="Ok", command=ok)
    ok_btn.grid(row=1, column=1, sticky='nsew')

    error_window.mainloop()


def about_us_popup(root):
    def destroy():
        about_window.destroy()

    about_window = tk.Toplevel(root)
    about_window.title('About')
    about_window.geometry('310x140+600+300')
    about_window['padx'] = 10
    about_window['pady'] = 10

    about_window.rowconfigure(0, weight=10)
    about_window.rowconfigure(1, weight=10)
    about_window.rowconfigure(2, weight=10)
    about_window.columnconfigure(0, weight=10)
    about_window.columnconfigure(1, weight=10)
    about_window.columnconfigure(2, weight=10)

    text = 'Hello, I am Yashas H Majmudar, I developed this program for easy evaluation of attendance for Indus ' \
           'University students. It is very easy to use and the collected data can be used as data science samples' \
           'to evaluate and project the data demographically. Thank you for using this!! 😁😁'
    about_label = tk.Label(about_window, text=text, wraplength=300)
    about_label.grid(row=0, column=0, columnspan=3, sticky='nsw')

    ok_btn = tk.Button(about_window, text="Close", command=destroy)
    ok_btn.grid(row=2, column=1, sticky='nsew')

    about_window.mainloop()


def sorter_recogniser(root, filepath):
    def destroy():
        recogniser.destroy()

    recogniser = tk.Toplevel(root)
    recogniser.title('Recogniser Word')
    recogniser.geometry('310x140+600+300')
    recogniser['padx'] = 10
    recogniser['pady'] = 10

    recogniser.rowconfigure(0, weight=10)
    recogniser.rowconfigure(1, weight=10)
    recogniser.rowconfigure(2, weight=30)
    recogniser.rowconfigure(3, weight=10)
    recogniser.rowconfigure(4, weight=10)
    recogniser.columnconfigure(0, weight=10)
    recogniser.columnconfigure(1, weight=5)
    recogniser.columnconfigure(2, weight=10)

    text = "Enter recogniser text.\nFor eg. IU for IU1941230066"
    hint_label = tk.Label(recogniser, text=text)
    hint_label.grid(row=0, column=0, columnspan=3, stick='nsew')

    input_field = tk.Entry(recogniser)
    input_field.grid(row=2, column=0, columnspan=3, sticky='nsew')

    def submit():
        word = str(input_field.get())
        if word != "":
            file = open(filepath, 'wb')
            binary = bytearray(word.encode('ascii'))
            file.write(binary)
            file.close()
            destroy()
            return word
        else:
            error_popup(recogniser, "Cannot put recogniser word empty")

    ok_btn = tk.Button(recogniser, text='Submit', command=submit)
    ok_btn.grid(row=4, column=1, sticky='nsew')

    recogniser.mainloop()

