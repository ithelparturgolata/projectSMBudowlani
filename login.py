"""login.py: Opis modułu
__name__ = "Aplikacja SMS SMBudowlani"
__author__ = "Artur Gołata"
__license__ = "MIT"
__version__ = "1.0"
__status__ = "production"
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview
# -*- coding: utf-8 -*-
import mysql.connector
from tkinter import messagebox
from smsapi.client import SmsApiPlClient
from smsapi.exception import SmsApiException
import os
import db.db
import mysql.connector
from tkinter import *
from tkinter import messagebox

class Panel():

    def login(self):
        pass

    def __init__(self):

        self.root = Tk()
        self.root.title("Panel logowania")
        self.root.geometry("370x200")
        self.root.resizable(0,0)
        self.font = ("arial", 10, "bold")

        self.entryuser = StringVar()
        self.entrypass = StringVar()

        self.lbluser = Label(self.root, text = "Użytkownik:", font = self.font)
        self.lbluser.place(x = "30", y = "50")

        self.lblpass = Label(self.root, text = "Hasło:", font = self.font)
        self.lblpass.place(x = "30", y = "100")

        self.lbluserent = Entry(self.root, textvariable = self.entryuser, font = self.font)
        self.lbluserent.place(x = "130", y = "50")

        self.lblpassent = Entry(self.root, textvariable=self.entrypass, font = self.font)
        self.lblpassent.place(x="130", y="100")

        self.btnLogin = Button(self.root, text = "Zaloguj", font = self.font)
        self.btnLogin.place(x = "130", y = "150")

        uname = self.entryuser.get()
        password = self.entrypass.get()

        try:
            if (uname == self.entryuser and password == self.entrypass):
                messagebox.showinfo("", "Zalogowano")
        except:
            messagebox.showinfo("", "Incorrent Username and Password")

        self.root.mainloop()

if __name__ == '__main__':
    Panel()

    #
    #
    # def Ok():
    #     uname = e1.get()
    #     password = e2.get()
    #
    #     if (uname == "" and password == ""):
    #         messagebox.showinfo("", "Blank Not allowed")
    #
    #     elif (uname == "Admin" and password == "123"):
    #         messagebox.showinfo("", "Login Success")
    #         root.destroy()
    #
    #     else:
    #         messagebox.showinfo("", "Incorrent Username and Password")
    #
    #
    # root = Tk()
    # root.title("Login")
    # root.geometry("300x200")
    # global e1
    # global e2
    #
    # Label(root, text="UserName").place(x=10, y=10)
    # Label(root, text="Password").place(x=10, y=40)
    #
    # e1 = Entry(root)
    # e1.place(x=140, y=10)
    #
    # e2 = Entry(root)
    # e2.place(x=140, y=40)
    # e2.config(show="*")
    #
    # Button(root, text="Login", command=Ok, height=3, width=13).place(x=10, y=100)
    #
    # root.mainloop()