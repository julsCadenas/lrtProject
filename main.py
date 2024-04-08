import customtkinter
import tkinter
from customtkinter import *
from tkinter import *
from PIL import Image

# app settings
customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.resizable(False,False)
app.geometry("1000x700")
app.title(" LRT-2")
app.iconbitmap('images/lrticon.ico')
customFont = customtkinter.CTkFont(family="Helvetica", size=28, weight="bold")

# train background
imageBackground = customtkinter.CTkImage(dark_image=Image.open("images/background.jpg"), size=(500,700))
imageLabel = customtkinter.CTkLabel(app, text="", image=imageBackground)
imageLabel.grid(row=0, column=0)

# purchase ticket title
titleFont = customtkinter.CTkFont(family="Helvetica", size=50, weight="bold")
titleLabel = customtkinter.CTkLabel(app, text="Purchase Ticket", font=titleFont)
titleLabel.place(relx=0.75, rely=0.35, anchor="center")

# single journey button
singleBtn = CTkButton(master=app, text="Single Journey Card", fg_color="#9966CC", hover_color="#5E5A80", corner_radius=32, font=customFont, width=300, height=50)
singleBtn.place(relx=0.75, rely=0.47, anchor="center")

# stored value button
storedBtn = CTkButton(master=app, text="Stored Value Card", fg_color="#9966CC", hover_color="#5E5A80", corner_radius=32, font=customFont, width=325, height=50)
storedBtn.place(relx=0.75, rely=0.56, anchor="center")

app.mainloop()
