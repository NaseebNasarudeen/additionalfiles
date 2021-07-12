from tkinter import *
from tkinter import ttk, messagebox
import tkinter
from tkinter.tix import ComboBox
from tkcalendar import DateEntry
from datetime import date, timedelta
from createDatab import insertData


class registrationForm:
    def __init__(self, master):
        self.master = master
        self.headFrame = Frame(self.master)
        self.mainContentFrame = Frame(self.master)
        self.buttonFrame = Frame(self.master)

        self.headText = Label(
            self.headFrame,
            text="Registration Form",
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
        self.lastName = Label(
            self.mainContentFrame,
            text="Last Name",
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
        self.Age = Label(
            self.mainContentFrame,
            text="Age",
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
        self.state = Label(
            self.mainContentFrame,
            text="State",
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
        self.time = Label(
            self.mainContentFrame,
            text="Select Time",
            width=20,
            font=("bold", 10),
            background="black",
            fg="white",
        )
        self.genderVar = StringVar()
        self.vaccineVar = StringVar()
        self.stateVar = StringVar()
        self.timeVar = StringVar()
        self.firstNameEntry = Entry(self.mainContentFrame)
        self.lastNameEntry = Entry(self.mainContentFrame)
        self.genderCombo = ttk.Combobox(
            self.mainContentFrame, textvariable=self.genderVar
        )
        self.ageEntry = Entry(self.mainContentFrame)
        self.vaccineCombo = ttk.Combobox(
            self.mainContentFrame, textvariable=self.vaccineVar
        )
        self.stateCombo = ttk.Combobox(
            self.mainContentFrame, textvariable=self.stateVar
        )
        self.datecalendar = DateEntry(
            self.mainContentFrame,
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            mindate=date.today(),
            maxdate=date.today() + timedelta(days=45),
        )
        self.timeCombo = ttk.Combobox(self.mainContentFrame, textvariable=self.timeVar)
        self.submitButton = ttk.Button(
            self.buttonFrame, text="Submit", command=lambda: self.saveinDb()
        )
        self.genderCombo["values"] = ("Male", "Female", "Other")
        self.vaccineCombo["values"] = (
            "Vaxzevria",
            "Janssen",
            "Moderna",
            "Pfizer-BioNTech",
        )
        self.stateCombo["values"] = (
            "Bavaria",
            "Baden-Wurttemberg",
            "North Rhine-Westphalia",
            "Lower Saxony",
            "Hessen",
            "Saxony",
            "Schleswig-Holstein",
            "Rhineland-Palatinate",
            "Thuringia",
            "Saarland",
            "Saxony Anhalt",
            "Hamburg",
            "Bremen",
            "Bradenburg",
            "Mecklenburg",
            "Berlin",
        )
        self.timeCombo["values"] = ("Forenoon", "Afternoon")
        self.submitButton.pack(fill="both", expand=True)

        self.headText.pack(fill="both", expand=True)
        self.firstName.grid(row=0, column=0)
        self.firstNameEntry.grid(row=0, column=1)
        self.lastName.grid(row=1, column=0)
        self.lastNameEntry.grid(row=1, column=1)
        self.gender.grid(row=2, column=0)
        self.genderCombo.grid(row=2, column=1)
        self.Age.grid(row=3, column=0)
        self.ageEntry.grid(row=3, column=1)
        self.vaccine.grid(row=4, column=0)
        self.vaccineCombo.grid(row=4, column=1)
        self.state.grid(row=5, column=0)
        self.stateCombo.grid(row=5, column=1)
        self.date.grid(row=6, column=0)
        self.datecalendar.grid(row=6, column=1)
        self.time.grid(row=7, column=0)
        self.timeCombo.grid(row=7, column=1)
        self.headFrame.grid(row=0, column=0)
        self.mainContentFrame.grid(row=1, column=0)
        self.buttonFrame.grid(row=2, column=0, rowspan=2)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.columnconfigure(0, weight=1)
        # self.master.mainloop()

    def saveinDb(self):

        firstNameValue = self.firstNameEntry.get()
        lastNameValue = self.lastNameEntry.get()
        genderValue = self.genderVar.get()
        ageValue = self.ageEntry.get()
        vaccineValue = self.vaccineVar.get()
        stateValue = self.stateVar.get()
        timeValue = self.timeVar.get()
        dateValue = self.datecalendar.get_date()
        if (
            firstNameValue
            and lastNameValue
            and ageValue
            and genderValue
            and vaccineValue
            and stateValue
            and timeValue
            and dateValue
        ):
            insertData(
                firstNameValue,
                lastNameValue,
                genderValue,
                ageValue,
                vaccineValue,
                stateValue,
                dateValue,
                timeValue,
            )
            messagebox.showinfo("Info", "Data Entered")
            self.firstNameEntry.delete(0, "end")
            self.lastNameEntry.delete(0, "end")
            self.genderCombo.set("")
            self.ageEntry.delete(0, "end")
            self.vaccineCombo.set("")
            self.stateCombo.set("")
            self.timeCombo.set("")
            self.datecalendar.delete(0, "end")
        else:
            messagebox.showerror("Invalid Data", "Please fill in all required fields")


# registrationForm()
