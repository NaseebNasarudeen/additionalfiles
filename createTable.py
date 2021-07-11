from tkinter import *
from tkinter import ttk
import os

import csv
from pprint import pprint

# dataFile = r"./hospitalData.csv"
dataFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "hospitalData.csv")


class dataTB:
    def __init__(self, master):
        my_tree = ttk.Treeview(master)
        s = ttk.Style(master)
        scrollBar = ttk.Scrollbar(master, orient=VERTICAL, command=my_tree.yview)
        scrollBar.pack(side=RIGHT, fill=Y)
        my_tree.config(yscrollcommand=scrollBar.set)
        # print(s.theme_names())
        s.theme_use("default")
        s.configure("Treeview", rowheight=70)
        # root.title("View Hospitals")
        # root.geometry("600x300")
        my_tree.pack(fill=BOTH, expand=YES)

        my_tree["show"] = "headings"
        my_tree["columns"] = ("ID", "State", "Hospital", "Vaccine")

        # my_tree.column("#0", width=0,stretch=NO)
        my_tree.column("ID", anchor=W, width=10)
        my_tree.column("State", anchor=CENTER, width=80)
        my_tree.column("Hospital", anchor=W, width=80)
        my_tree.column("Vaccine", anchor=W, width=80)

        # my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID", text="ID", anchor=W)
        my_tree.heading("State", text="State", anchor=CENTER)
        my_tree.heading("Hospital", text="Hospital", anchor=W)
        my_tree.heading("Vaccine", text="Vaccine", anchor=W)

        with open(dataFile, "r") as csvfile:
            # fieldnames = ["S NO", "STATE", "HOSPITALS", "VACCINE"]
            csv_reader = csv.DictReader(csvfile, delimiter=";")
            for i, line in enumerate(csv_reader, start=1):
                # print(line)
                my_tree.insert(
                    parent="",
                    index="end",
                    iid=i,
                    text="",
                    values=(
                        line["S NO"],
                        line["STATE"],
                        line["HOSPITALS"],
                        line["VACCINE"].replace(":", "\n"),
                    ),
                )

        my_tree.pack(pady=20)

        # root.resizable(height = None, width = None)
        # root.grid(column=0, row=0, sticky="ns")


# root.mainloop()
