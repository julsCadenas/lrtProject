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

        self.showFrame(IndexPage)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class IndexPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.configure(fg_color="#242424") #change frame background color
        customFont = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")

        # train background
        imageBackground = CTkImage(dark_image=Image.open("images/background.jpg"), size=(500,700))
        imageLabel = CTkLabel(self, text="", image=imageBackground)
        imageLabel.grid(row=0, column=0, sticky="nsew")

        # purchase ticket title
        titleFont = CTkFont(family="Helvetica", size=50, weight="bold")
        titleLabel = CTkLabel(self, text="Purchase Ticket", font=titleFont)
        titleLabel.grid(row=0, column=1, columnspan=1, padx=50, pady=(0,170))

        # single journey button
        singleBtn = CTkButton(master=self, text="Single Journey Ticket", fg_color="#9966CC", hover_color="#A32CC4",
                              corner_radius=15, font=customFont, width=300, height=40,
                              command=lambda: controller.showFrame(SingleJourneyPage))
        singleBtn.place(relx=0.75, rely=0.485, anchor="center")

        # stored value button
        storedBtn = CTkButton(master=self, text="Stored Value Ticket", fg_color="#9966CC", hover_color="#A32CC4",
                              corner_radius=15, font=customFont, width=300, height=40)
        storedBtn.place(relx=0.75, rely=0.56, anchor="center")

class SingleJourneyPage(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        stationValues = {
            1: "Antipolo",
            2: "Marikina",
            3: "Santolan",
            4: "Katipunan",
            5: "Anonas",
            6: "Cubao",
            7: "Betty Go",
            8: "Gilmore",
            9: "J. Ruiz",
            10: "V. Mapa",
            11: "Pureza",
            12: "Legarda",
            13: "Recto"
        }

        # Labels for station names
        stationLabels = ["Recto", "Legarda", "Pureza", "V.Mapa", "J.Ruiz", "Gilmore", "Betty Go",
            "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"]

        def slideValue(value):
            slideLabel.configure(text=stationValues[int(value)])

        self.configure(fg_color="#242424") #change frame background color
        customFont = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")

        mainFrame = CTkFrame(master=self, height=620, width=600, corner_radius=15)
        mainFrame.place(relx=0.665, rely=0.5, anchor="center")

        titleFont = customtkinter.CTkFont(family="Century Gothic", size=45, weight="bold")
        titleLabel2 = CTkLabel(mainFrame, text="Single Journey Ticket", font=titleFont)
        titleLabel2.place(relx=0.5, rely=0.1, anchor="center")

        backBtn = CTkButton(master=mainFrame, text="Cancel", fg_color="#9966CC", hover_color="#A32CC4",
                            corner_radius=10, font=customFont, width=150, height=35,
                            command=lambda: controller.showFrame(IndexPage))
        backBtn.place(relx=0.37, rely=0.9, anchor="center")

        confirmBtn = CTkButton(master=mainFrame, text="Confirm", fg_color="#9966CC", hover_color="#A32CC4",
                          corner_radius=10, font=customFont, width=150, height=35,
                          command=lambda: controller.showFrame(IndexPage))
        confirmBtn.place(relx=0.64, rely=0.9, anchor="center")

        locationFont = customtkinter.CTkFont(family="Century Gothic", size=32, weight="bold")
        locationTitle = customtkinter.CTkLabel(mainFrame, text="You Are Here:", font=locationFont)
        locationTitle.place(relx=0.5, rely=0.24, anchor="center")

        dropdownFont = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")
        locationDropdown = customtkinter.CTkComboBox(mainFrame, values=stationLabels, width=240, height=30, font=dropdownFont, justify="center")
        locationDropdown.place(relx=0.5, rely=0.32, anchor="center")

        # frame to put slider into
        sliderFrame = CTkFrame(master=self, height=620, width=270, corner_radius=15)
        sliderFrame.place(relx=0.18, rely=0.5, anchor="center")

        # station slider picker (inside the frame)
        slider = CTkSlider(master=sliderFrame, from_=1, to=13, number_of_steps=12, orientation="vertical",
                           button_color="#9966CC", height=610, width=30, command=slideValue, progress_color="#4a4d50", button_hover_color="#A32CC4")
        slider.place(relx=0.2, rely=0.5, anchor="center")
        slider.set(0) # set slider to 1/bottom

        destinationFont = customtkinter.CTkFont(family="Century Gothic", size=32, weight="bold")
        destinationTitle = customtkinter.CTkLabel(mainFrame, text="Destination:", font=destinationFont)
        destinationTitle.place(relx=0.5, rely=0.42, anchor="center")

        sliderLabelFrame = CTkFrame(mainFrame, height=50, width=250, corner_radius=15, border_color="#4a4d50")
        sliderLabelFrame.place(relx=0.5, rely=0.5, anchor="center")

        slideLabelFont = customtkinter.CTkFont(family="Century Gothic", size=24, weight="bold")
        slideLabel = customtkinter.CTkLabel(sliderLabelFrame, text="", font=slideLabelFont)
        slideLabel.place(relx=0.5, rely=0.5, anchor="center")

        customFont2 = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")

        # Calculate the position of each label
        labelPositions = [(0.035 + i * 0.078) for i in range(13)]

        for position, label_text in zip(labelPositions, stationLabels):
            stationLabels = customtkinter.CTkLabel(sliderFrame, text=label_text, font=customFont2)
            stationLabels.place(relx=0.5, rely=position, anchor="center")

        costLabel = customtkinter.CTkLabel(mainFrame, text="Fare Cost:", font=destinationFont)
        costLabel.place(relx=0.5, rely=0.61, anchor="center")

        costFrame = CTkFrame(mainFrame, height=50, width=250, corner_radius=15, border_color="#4a4d50")
        costFrame.place(relx=0.5, rely=0.7, anchor="center")

app = PageFormat()
app.mainloop()

