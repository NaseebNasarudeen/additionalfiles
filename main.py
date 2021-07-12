from tkinter import *
from tkinter import messagebox
from tkinter.tix import *
from tkinter import ttk
import os

# from PIL import ImageTk, Image
from viewTable import dataTB
from vaccinRegister import registrationForm
from modifyData import modifyForm
from viewData import viewForm

# from tkinter import PhotoImage


class VaccinationApp:
    def __init__(self, master):
        self.master = master
        self.homeText = """Welcome to Quick Jabs\n\n
The main purpose of this platform is to provide accurate and relevant information regarding COVID-19 vaccines. 
It is a systematic vaccination registration portal for booking your vaccines appointments. 
To get a free COVID-19 vaccine you can book an appointment at associate hospitals.
If you are concerned about potential side-effects of the vaccine or existing health conditions, 
it is advised to consult your family doctor before booking your appointments.
Anyone who holds a valid health insurance and is over 18 years of age can book an appointment in their own state.

Why should you get vaccinated?
As we all know COVID-19 pandemic has ravaged national economies as well as health facilities the world over in the span of a year. 
It is a highly contagious disease that can cause lingering health issues or even death.
If you get vaccinated against COVID-19, you can protect yourself and others from complications caused by the Coronavirus.
It is not mandatory to take the vaccine, but Robert Koch Institute has strongly advised the general public to do so. 

You should delay your COVID-19 vaccine when:
1. Currently infected with COVID-19 and/or until it has been at least 6 months since you have recovered from COVID-19.
2. Have symptoms of COVID-19. 
3. Have a fever (above 38°C), wait until you better.
Note: Change your appointment If you cannot attend your appointment, you can ask for a new one. 
To do this go to modify/cancel appointments.


Personal information and Data Privacy
Your personal information will be processed in line with the General Data Protection Laws of Germany.

Contact: +49 12345678987
Address: Karl Marx Straße 12,
    13347 Berlin
"""
        self.master.protocol("WM_DELETE_WINDOW", self._closeApp)
        master.title("QuickJabs")
        # master.config(bg="gray17")
        master.geometry("850x750")
        filePath = os.path.dirname(os.path.realpath(__file__))
        # Images
        smallHomeImage = PhotoImage(
            file=os.path.join(filePath, "home.png")
        ).subsample(10, 10)
        syringeImage = PhotoImage(file=os.path.join(filePath, "syringe.png")).subsample(
            10, 10
        )
        searchImage = PhotoImage(file=os.path.join(filePath, "search.png")).subsample(
            10, 10
        )
        editImage = PhotoImage(file=os.path.join(filePath, "edit.png")).subsample(
            10, 10
        )
        viewImage = PhotoImage(file=os.path.join(filePath, "view.png")).subsample(
            10, 10
        )
        infoImage = PhotoImage(file=os.path.join(filePath, "info.png")).subsample(
            10, 10
        )
        exitImage = PhotoImage(file=os.path.join(filePath, "logout.png")).subsample(
            10, 10
        )

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
            image=smallHomeImage,
            command=lambda: homeFrame.tkraise(),
        )
        homeButton.image = smallHomeImage

        newButton = Button(
            sidebarTop, image=syringeImage, command=lambda: newFrame.tkraise()
        )
        newButton.image = syringeImage
        searchButton = Button(
            sidebarTop, image=searchImage, command=lambda: searchFrame.tkraise()
        )
        searchButton.image = searchImage
        modifyButton = Button(
            sidebarTop, image=editImage, command=lambda: modifyFrame.tkraise()
        )
        modifyButton.image = editImage
        viewButton = Button(
            sidebarTop, image=viewImage, command=lambda: viewFrame.tkraise()
        )
        viewButton.image = viewImage
        infoButton = Button(sidebarBottom, image=infoImage, command=self._infoMessage)
        infoButton.image = infoImage
        exitButton = Button(sidebarBottom, image=exitImage, command=self._closeApp)
        exitButton.image = exitImage
        self.changeOnHover(sidebarTop, homeButton, "Home Screen")
        self.changeOnHover(sidebarTop, newButton, "New Registration")
        self.changeOnHover(sidebarTop, searchButton, "Search Centers")
        self.changeOnHover(sidebarTop, modifyButton, "Modify Registration")
        self.changeOnHover(sidebarTop, viewButton, "View Appointments")
        self.changeOnHover(sidebarBottom, infoButton, "Info")
        self.changeOnHover(sidebarBottom, exitButton, "Exit")
        homeButton.pack(expand=False, fill="both", side="top")
        newButton.pack(expand=False, fill="both", side="top")
        searchButton.pack(expand=False, fill="both", side="top")
        modifyButton.pack(expand=False, fill="both", side="top")
        viewButton.pack(expand=False, fill="both", side="top")
        exitButton.pack(expand=False, fill="both", side="bottom")
        infoButton.pack(expand=False, fill="both", side="bottom")

        # Home Frame
        homeFrame = Frame(mainarea, width=750, height=750)
        Label(homeFrame, text=self.homeText).pack(
            fill="both", expand=True, anchor="center"
        )
        homeFrame.grid(row=0, column=0, sticky="nsew")

        # New Data Frame
        newFrame = Frame(mainarea)
        registrationForm(newFrame)
        # Label(newFrame, text="This is New Data Frame").pack(
        #     fill="both", expand=True, anchor="center"
        # )
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
        modifyForm(modifyFrame)
        modifyFrame.grid(row=0, column=0, sticky="nsew")

        # View Frame
        viewFrame = Frame(mainarea)
        viewForm(viewFrame)
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

    def changeOnHover(self, parent, myButton, texta):
        tip = Balloon(parent)
        tip.bind_widget(myButton, balloonmsg=texta)

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




