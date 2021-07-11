from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# from PIL import ImageTk, Image
from viewTable import dataTB

# from tkinter import PhotoImage


class VaccinationApp:
    def __init__(self, master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self._closeApp)
        master.title("Vaccination Buddy")
        # master.config(bg="gray17")
        master.geometry("850x750")

        # Images
        homeImage = PhotoImage(
            file=r"G:\naseeb\PDFextract_text-main\PDFextract_text-main\starterFiles\finalFolder\home-icon-silhouette.gif"
        )
        smallHomeImage = homeImage.subsample(5, 5)

        sidebar = Frame(master, width=100, bg="#00ADB5", height=750, borderwidth=2)
        sidebarTop = Frame(sidebar, width=100, bg="#00ADB5", height=325)
        sidebarBottom = Frame(sidebar, width=100, bg="#00ADB5", height=325)
        sidebar.pack(expand=False, fill="both", side="left", anchor="nw")
        sidebarTop.pack(expand=True, fill="both", side="top", anchor="nw")
        sidebarBottom.pack(expand=True, fill="both", side="bottom", anchor="sw")
        mainarea = Frame(master, bg="gray17", width=750, height=750)
        mainarea.pack(expand=True, fill="both", side="right")
        mainarea.rowconfigure(0, weight=1)
        mainarea.columnconfigure(0, weight=1)

        # Buttons
        homeButton = Button(
            sidebarTop,
            text="Home",
            image=smallHomeImage,
            command=lambda: homeFrame.tkraise(),
        )

        newButton = Button(sidebarTop, text="New", command=lambda: newFrame.tkraise())
        searchButton = Button(
            sidebarTop, text="search", command=lambda: searchFrame.tkraise()
        )
        modifyButton = Button(
            sidebarTop, text="Modify", command=lambda: modifyFrame.tkraise()
        )
        viewButton = Button(
            sidebarTop, text="View", command=lambda: viewFrame.tkraise()
        )
        infoButton = Button(sidebarBottom, text="Info", command=self._infoMessage)
        exitButton = Button(sidebarBottom, text="Exit", command=self._closeApp)
        homeButton.pack(expand=True, fill="both", side="top")
        newButton.pack(expand=False, fill="both", side="top")
        searchButton.pack(expand=False, fill="both", side="top")
        modifyButton.pack(expand=False, fill="both", side="top")
        viewButton.pack(expand=False, fill="both", side="top")
        exitButton.pack(expand=False, fill="both", side="bottom")
        infoButton.pack(expand=False, fill="both", side="bottom")

        # Home Frame
        homeFrame = Frame(mainarea, width=750, height=750)
        Label(homeFrame, text="This is Home Frame").pack(
            fill="both", expand=True, anchor="center"
        )
        homeFrame.grid(row=0, column=0, sticky="nsew")

        # New Data Frame
        newFrame = Frame(mainarea)
        Label(newFrame, text="This is New Data Frame").pack(
            fill="both", expand=True, anchor="center"
        )
        newFrame.grid(row=0, column=0, sticky="nsew")

        # Search Frame
        searchFrame = Frame(mainarea)
        dataTB(searchFrame)
        # Label(searchFrame, text="This is Search Frame").pack(
        #     fill="both", expand=True, anchor="center"
        # )
        searchFrame.grid(row=0, column=0, sticky="nsew")

        # Modify Frame
        modifyFrame = Frame(mainarea)
        Label(modifyFrame, text="This is Modify Frame").pack(
            fill="both", expand=True, anchor="center"
        )
        modifyFrame.grid(row=0, column=0, sticky="nsew")

        # View Frame
        viewFrame = Frame(mainarea)
        Label(viewFrame, text="This is View Frame").pack(
            fill="both", expand=True, anchor="center"
        )
        viewFrame.grid(row=0, column=0, sticky="nsew")

        homeFrame.tkraise()

    def _closeApp(self):
        op = messagebox.askquestion(
            title="Close Vaccination Buddy Application",
            message="Are you sure you want to close application?",
            icon="warning",
        )
        # print(op)
        if op == "yes":
            self.master.destroy()

    def _infoMessage(self):
        messagebox.showinfo(
            title="Information",
            message="""Version 1.0.0\n
This application has been developed as a group project for Python FWP at Technische Hochschule Deggendorf.\n
All the icons and vectors are downloaded from www.flaticon.com and www.freepik.com.\nThe image credits belong to the respective owners.
For further information, please contact the developers. Refer to the Documentation notes.""",
        )


def main():
    root = Tk()
    vApp = VaccinationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# root = tk.Tk()


# root.title("Vaccination Buddy")
# root.config(bg="gray17")
# root.geometry("800x600")
# sideFrame = tk.Frame(root, bg="#00ADB5")
# mainFrame = tk.Frame(root)

# homeButton = tk.Button(sideFrame, text="HM", command=lambda: print("Hello World"))
# newButton = tk.Button(sideFrame, text="NEW", command=lambda: print("NEW DATA"))
# searchButton = tk.Button(sideFrame, text="HM", command=lambda: print("search "))
# modifyButton = tk.Button(sideFrame, text="HM", command=lambda: print("modify"))
# viewButton = tk.Button(sideFrame, text="HM", command=lambda: print("view"))
# infoButton = tk.Button(sideFrame, text="HM", command=lambda: print("info"))
# exitButton = tk.Button(sideFrame, text="HM", command=lambda: print("exit"))
# homeButton.grid(row=0, column=0)
# newButton.grid(row=1, column=0)
# searchButton.grid(row=2, column=0)
# modifyButton.grid(row=3, column=0)
# viewButton.grid(row=4, column=0)
# infoButton.grid(row=7, column=0)
# exitButton.grid(row=8, column=0)
# # homeButton.place(x=0, y=0)
# sideFrame.pack(side="left")
# mainFrame.pack(side="right")


# root.mainloop()
