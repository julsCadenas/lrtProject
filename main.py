import customtkinter
from customtkinter import *
from tkinter import *
from PIL import Image

class PageFormat(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resizable(False, False)
        self.geometry("1000x700")
        self.title(" LRT-2")
        self.iconbitmap('images/lrticon.ico')
        customtkinter.set_appearance_mode("dark")

        self.frames = {}

        for F in (IndexPage, SingleJourneyPage):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack(side="left", fill="both", expand=True)

        self.showFrame(IndexPage)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class IndexPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.configure(fg_color="#242424") #change frame background color
        customFont = customtkinter.CTkFont(family="Helvetica", size=28, weight="bold")

        # train background
        imageBackground = CTkImage(dark_image=Image.open("images/background.jpg"), size=(500,700))
        imageLabel = CTkLabel(self, text="", image=imageBackground)
        imageLabel.grid(row=0, column=0, sticky="nsew")

        # purchase ticket title
        titleFont = CTkFont(family="Helvetica", size=50, weight="bold")
        titleLabel = CTkLabel(self, text="Purchase Ticket", font=titleFont)
        # titleLabel.place(relx=0.85, rely=0.35, anchor="center")
        titleLabel.grid(row=0, column=1, columnspan=1, padx=50, pady=(0,170))

        # single journey button
        singleBtn = CTkButton(master=self, text="Single Journey Card", fg_color="#9966CC", hover_color="#A32CC4",
                              corner_radius=32, font=customFont, width=300, height=50,
                              command=lambda: controller.showFrame(SingleJourneyPage))
        singleBtn.place(relx=0.75, rely=0.47, anchor="center")
        # singleBtn.grid(row=2, column=0, padx=10, pady=1)

        # stored value button
        storedBtn = CTkButton(master=self, text="Stored Value Card", fg_color="#9966CC", hover_color="#A32CC4",
                              corner_radius=32, font=customFont, width=325, height=50)
        storedBtn.place(relx=0.75, rely=0.56, anchor="center")
        # storedBtn.grid(row=2, column=1, padx=10, pady=10)

class SingleJourneyPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.configure(fg_color="#242424") #change frame background color
        customFont = customtkinter.CTkFont(family="Helvetica", size=28, weight="bold")

        titleFont = customtkinter.CTkFont(family="Helvetica", size=50, weight="bold")
        titleLabel2 = CTkLabel(self, text="Single Journey Card", font=titleFont)
        titleLabel2.place(relx=0.5, rely=0.35, anchor="center")

        backBtn = CTkButton(master=self, text="Back", fg_color="#9966CC", hover_color="#A32CC4",
                              corner_radius=32, font=customFont, width=300, height=50,
                              command=lambda: controller.showFrame(IndexPage))
        backBtn.place(relx=0.5, rely=0.5, anchor="center")


app = PageFormat()
app.mainloop()
