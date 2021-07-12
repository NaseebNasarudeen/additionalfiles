from tkinter import *
from tkinter import ttk, messagebox
import tkinter
from tkinter.tix import ComboBox
from tkcalendar import DateEntry
from datetime import date, timedelta
from createDatab import showTable


class viewForm:
    def __init__(self, master):
        self.master = master
        self.headFrame = Frame(self.master)
        self.mainContentFrame = Frame(self.master)
        self.buttonFrame = Frame(self.master)

        self.headText = Label(
            self.headFrame,
            text="View Appointment Form",
            width=20,
            font=("bold", 20),
            background="black",
            fg="yellow",
        )
        self.firstName = Label(
            self.mainContentFrame,
            text="First Name",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.firstNameData = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.lastName = Label(
            self.mainContentFrame,
            text="Last Name",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.lastNameData = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.gender = Label(
            self.mainContentFrame,
            text="Sex",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.genderData = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.Age = Label(
            self.mainContentFrame,
            text="Age",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.AgeData = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.vaccine = Label(
            self.mainContentFrame,
            text="Vaccine Preferred",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.vaccineData = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.state = Label(
            self.mainContentFrame,
            text="State",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.stateData = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.date = Label(
            self.mainContentFrame,
            text="Select Date",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.datecalendar = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.time = Label(
            self.mainContentFrame,
            text="Time Slot",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.timeData = Label(
            self.mainContentFrame,
            text="",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )

        self.nameQuery = Entry(self.buttonFrame)
        self.nameQuery.grid(row=0, column=0)
        self.submitButton = ttk.Button(
            self.buttonFrame, text="Search First Name", command=lambda: self.modifyinDb()
        )
        self.submitButton.grid(row=0, column=1)

        self.headText.pack(fill="both", expand=True)
        self.firstName.grid(row=0, column=0)
        self.firstNameData.grid(row=0, column=1)
        self.lastName.grid(row=1, column=0)
        self.lastNameData.grid(row=1, column=1)
        self.gender.grid(row=2, column=0)
        self.genderData.grid(row=2, column=1)
        self.Age.grid(row=3, column=0)
        self.AgeData.grid(row=3, column=1)
        self.vaccine.grid(row=4, column=0)
        self.vaccineData.grid(row=4, column=1)
        self.state.grid(row=5, column=0)
        self.stateData.grid(row=5, column=1)
        self.date.grid(row=6, column=0)
        self.datecalendar.grid(row=6, column=1)
        self.time.grid(row=7, column=0)
        self.timeData.grid(row=7, column=1)
        self.headFrame.grid(row=0, column=0)
        self.buttonFrame.grid(row=1, column=0)
        self.mainContentFrame.grid(row=2, column=0)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.columnconfigure(0, weight=1)
        # self.master.mainloop()

    def modifyinDb(self):

        firstNameValue = self.nameQuery.get()
        if firstNameValue:
            data = showTable(firstNameValue)
            if data:
                self.firstNameData.config(text=data[0])
                self.lastNameData.config(text=data[1])
                self.genderData.config(text=data[2])
                self.AgeData.config(text=data[3])
                self.vaccineData.config(text=data[4])
                self.stateData.config(text=data[5])
                self.datecalendar.config(text=data[6])
                self.timeData.config(text=data[7])
            else:
                messagebox.showerror("Invalid Data", "No Data Found in Database.")
                return
        else:
            messagebox.showerror("Invalid Name", "No name entered.")
            return
