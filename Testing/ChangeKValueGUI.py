import tkinter as tk
import GuiMenu


class ChangeKValueGUI(GuiMenu.GuiMenu):
    def __init__(self):
        GuiMenu.GuiMenu.__init__(self)
        self.menu = tk.Toplevel()
        self.menu.geometry("500x500")
        self.entry = tk.Entry(self.menu)
        self.entry.place(x=10, y=100)

        self.settings.GetFileLines()

    def SubmitInfo(self):

        new_k = self.entry.get()

        # Making changes to k value.
        self.settings.GetFileLines()
        k_value = self.settings.GetLineNumber("k-value")
        field_end = self.settings.list_of_lines[k_value].rfind(":")
        self.settings.list_of_lines[k_value] = self.settings.list_of_lines[k_value][0:(field_end + 1)] + new_k

        # Committing changes to file.
        self.settings.WriteChangesToFile()
        self.menu.destroy()

    def RunMenu(self):
        label = tk.Label(self.menu, **self.label_properties, text="Enter k value:")
        label.place(x=10, y=40)
        submit = tk.Button(self.menu, **self.button_properties, text="Submit", command=self.SubmitInfo)
        submit.place(x=200, y=100)

        self.menu.mainloop()
