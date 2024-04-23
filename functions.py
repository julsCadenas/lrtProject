import customtkinter
# import tkinter
from customtkinter import *
# from tkinter import *
# from PIL import Image
# import sqlite3
# import dbfunctions
# from dbfunctions import OriginDropdown, DestinationNames, GetFarePrice, GetOriginID, GetFareID, InsertSummary, GetRecentOrigin, GetRecentDest

def changeWindow(self, payChange):
    change = CTkToplevel(self)
    change.resizable(False, False)
    change.title(" LRT-2")
    change.iconbitmap('images/lrticon.ico')
    change.attributes("-topmost", True)
    change.grab_set()

    windowWidth = 300
    windowHeight = 150
    screenWidth = 1920
    screenHeight = 1080

    xPosition = (screenWidth - windowWidth) // 2
    yPosition = (screenHeight - windowHeight) // 2

    change.geometry(f"{windowWidth}x{windowHeight}+{xPosition}+{yPosition}")

    btnFont = customtkinter.CTkFont(family="Century Gothic", size=14, weight="bold")
    labelFont = customtkinter.CTkFont(family="Century Gothic", size=16, weight="bold")

    def closeWindow():
        change.destroy()

    okBtn = CTkButton(master=change, text="OK", fg_color="#9966CC", width=100, font=btnFont, command=closeWindow, hover_color="#A32CC4")
    okBtn.place(relx=0.5, rely=0.75, anchor="center")

    changeLabel = CTkLabel(master=change, text=f"Your change is Php {payChange}", font=labelFont)
    changeLabel.place(relx=0.5, rely=0.4, anchor="center")

def calculateChange(pay, totalFare):
    payChange = pay - totalFare
    return payChange

def summaryWindow(self, pursePay, totalPay):
    change = CTkToplevel(self)
    change.resizable(False, False)
    change.title(" LRT-2")
    change.iconbitmap('images/lrticon.ico')
    change.attributes("-topmost", True)
    change.grab_set()

    windowWidth = 300
    windowHeight = 150
    screenWidth = 1920
    screenHeight = 1080

    xPosition = (screenWidth - windowWidth) // 2
    yPosition = (screenHeight - windowHeight) // 2

    change.geometry(f"{windowWidth}x{windowHeight}+{xPosition}+{yPosition}")

    btnFont = customtkinter.CTkFont(family="Century Gothic", size=14, weight="bold")
    labelFont = customtkinter.CTkFont(family="Century Gothic", size=16, weight="bold")

    def closeWindow():
        change.destroy()

    okBtn = CTkButton(master=change, text="OK", fg_color="#9966CC", width=100, font=btnFont, command=closeWindow, hover_color="#A32CC4")
    okBtn.place(relx=0.5, rely=0.75, anchor="center")

    changeLabel = CTkLabel(master=change, text=f"Your card's balance is Php {pursePay}", font=labelFont)
    changeLabel.place(relx=0.5, rely=0.25, anchor="center")

    changeLabel = CTkLabel(master=change, text=f"Your payment is Php {totalPay}", font=labelFont)
    changeLabel.place(relx=0.5, rely=0.45, anchor="center")