import os
import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.prompt = tk.Label(self, text="To stop iterate and stop app press button", anchor="w")
        self.submit = tk.Button(self, text="stop app", command = self.__exit_command)
        self.output = tk.Label(self, text="")

        # lay the widgets out on the screen.
        self.prompt.pack(side="top", fill="x")
        self.output.pack(side="top", fill="x", expand=True)
        self.submit.pack(side="right")

    def __exit_command(self):
        os._exit(0)


def show_first_window():
       root = tk.Tk()
       Example(root).pack(fill="both", expand=True)
       root.mainloop()