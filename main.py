import customtkinter
import tkinter
from customtkinter import *
from tkinter import *
from PIL import Image
import sqlite3
# import dbfunctions
from dbfunctions import OriginDropdown, DestinationNames, GetFarePrice, GetOriginID, GetFareID, InsertSummary, GetRecentOrigin, GetRecentDest

class PageFormat(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resizable(False, False)
        self.geometry("1000x700")
        self.title(" LRT-2")
        self.iconbitmap('images/lrticon.ico')
        customtkinter.set_appearance_mode("dark")

        self.frames = {}

        for F in (IndexPage, SingleJourneyPage, SingleJourneySummary):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(IndexPage)

    def showFrame(self, cont, **kwargs):
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

        self.originID = 0
        self.destinationId = 0
        self.farePrice = 0
        self.fareID = 0

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

        self.configure(fg_color="#242424") #change frame background color
        customFont = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")

        # frame for the bulk of the contents
        mainFrame = CTkFrame(master=self, height=620, width=600, corner_radius=15)
        mainFrame.place(relx=0.665, rely=0.5, anchor="center")

        # single journey title 
        titleFont = customtkinter.CTkFont(family="Century Gothic", size=45, weight="bold")
        titleLabel2 = CTkLabel(mainFrame, text="Single Journey Ticket", font=titleFont)
        titleLabel2.place(relx=0.5, rely=0.1, anchor="center")

        # origin title
        locationFont = customtkinter.CTkFont(family="Century Gothic", size=32, weight="bold")
        locationTitle = customtkinter.CTkLabel(mainFrame, text="You Are Here:", font=locationFont)
        locationTitle.place(relx=0.5, rely=0.24, anchor="center")

        # Labels for station names
        stationLabels = ["Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go",
            "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"]

        # outputs the values of the slider
        DestinationNames(controller)

        # origin drop down list
        # OriginDropdown(mainFrame)
        dropdownFont = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")
        locationDropdown = customtkinter.CTkComboBox(mainFrame, values=stationLabels, width=240, height=30,
                                                     font=dropdownFont, justify="center")
        locationDropdown.place(relx=0.5, rely=0.32, anchor="center")

        # function for when you change the origin station
        def locationChange(event):
            originName = locationDropdown.get()

            self.originID = GetOriginID(originName)
            self.destinationId = int(slider.get())

            self.farePrice = GetFarePrice(self.originID, self.destinationId)

            self.fareID = GetFareID(self.farePrice, self.originID, self.destinationId)

            print(f"Origin ID: {self.originID}")
            print(f"Destination ID: {self.destinationId}")
            print(f"Fare ID: {self.fareID}")
            print(" ")

            if self.farePrice is not None:
                fareCost.configure(text=f"Php {self.farePrice}0")
            else:
                fareCost.configure(text="No fare available")

        locationDropdown.configure(command=locationChange)
        # function for the values of the slider (only for recto station)
        def slideValue(value):
            index = int(value) - 1
            destNames = controller.destNames[index]
            slideLabel.configure(text=destNames)
            originName = locationDropdown.get()

            self.originID = GetOriginID(originName)
            self.destinationId = int(value)

            self.farePrice = GetFarePrice(self.originID, self.destinationId)

            self.fareID = GetFareID(self.farePrice, self.originID, self.destinationId)

            print(f"Origin ID: {self.originID}")
            print(f"Destination ID: {self.destinationId}")
            print(f"Fare ID: {self.fareID}")
            print(" ")


            if self.farePrice is not None:
                fareCost.configure(text=f"Php {self.farePrice}0")
            else:
                fareCost.configure(text="No fare available")

        # frame to put slider into
        sliderFrame = CTkFrame(master=self, height=620, width=270, corner_radius=15)
        sliderFrame.place(relx=0.18, rely=0.5, anchor="center")

        # station slider picker (inside the frame)
        slider = CTkSlider(master=sliderFrame, from_=13, to=1, number_of_steps=12, orientation="vertical",
                           button_color="#9966CC", height=610, width=30, command=slideValue, progress_color="#4a4d50", button_hover_color="#A32CC4")
        slider.place(relx=0.2, rely=0.5, anchor="center")
        slider.set(0) # set slider to 1/bottom

        # destination title 
        destinationFont = customtkinter.CTkFont(family="Century Gothic", size=32, weight="bold")
        destinationTitle = customtkinter.CTkLabel(mainFrame, text="Destination:", font=destinationFont)
        destinationTitle.place(relx=0.5, rely=0.42, anchor="center")

        # frame for the slider
        sliderLabelFrame = CTkFrame(mainFrame, height=50, width=250, corner_radius=15, border_color="#4a4d50")
        sliderLabelFrame.place(relx=0.5, rely=0.5, anchor="center")

        # label of sliders
        slideLabelFont = customtkinter.CTkFont(family="Century Gothic", size=24, weight="bold")
        slideLabel = customtkinter.CTkLabel(sliderLabelFrame, text="", font=slideLabelFont)
        slideLabel.place(relx=0.5, rely=0.5, anchor="center")

        customFont2 = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")

        # Calculate the position of each label
        labelPositions = [(0.035 + i * 0.078) for i in range(13)]

        # set the position of the labels
        for position, label_text in zip(labelPositions, stationLabels):
            stationLabels = customtkinter.CTkLabel(sliderFrame, text=label_text, font=customFont2)
            stationLabels.place(relx=0.5, rely=position, anchor="center")

        # label for the fare price
        costLabel = customtkinter.CTkLabel(mainFrame, text="Fare Cost:", font=destinationFont)
        costLabel.place(relx=0.5, rely=0.61, anchor="center")

        # frame for the fare price
        costFrame = CTkFrame(mainFrame, height=50, width=250, corner_radius=15, border_color="#4a4d50")
        costFrame.place(relx=0.5, rely=0.7, anchor="center")

        fareCost = customtkinter.CTkLabel(costFrame, font=dropdownFont, text="")
        fareCost.place(relx=0.5, rely=0.5, anchor="center")

        # cancel button
        backBtn = CTkButton(master=mainFrame, text="Cancel", fg_color="#9966CC", hover_color="#A32CC4",
                            corner_radius=10, font=customFont, width=150, height=35,
                            command=lambda: controller.showFrame(IndexPage))
        backBtn.place(relx=0.37, rely=0.9, anchor="center")

        def onConfirm(controller):
            InsertSummary(self.fareID, self.originID, self.destinationId)
            controller.showFrame(SingleJourneySummary)

        # confirm button
        confirmBtn = CTkButton(master=mainFrame, text="Confirm", fg_color="#9966CC", hover_color="#A32CC4",
                          corner_radius=10, font=customFont, width=150, height=35,
                          command=lambda: onConfirm(controller))
        confirmBtn.place(relx=0.64, rely=0.9, anchor="center")

class SingleJourneySummary(SingleJourneyPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # originID2 = self.originID
        # destinationId2 = self.destinationId
        # farePrice2 = self.farePrice

        # Labels for station names
        stationLabels = ["Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go",
            "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"]

        stationIndex = GetRecentOrigin() - 1
        destinationIndex = GetRecentDest() - 1

        # stationIndex = originID2 - 1
        # destinationIndex = destinationId2 - 1

        # originStation = stationLabels[stationIndex]
        # destinationStation = stationLabels[destinationIndex]

        if stationIndex & destinationIndex is not None:
            originStation = stationLabels[stationIndex]
            destinationStation = stationLabels[destinationIndex]
        else:
            originStation = "Unknown"
            destinationStation = "Unknown"

        self.configure(fg_color="#242424") #change frame background color
        customFont = customtkinter.CTkFont(family="Century Gothic", size=32, weight="bold")

        mainSummaryFrame = CTkFrame(master=self, height=620, width=900, corner_radius=15)
        mainSummaryFrame.place(relx=0.51, rely=0.5, anchor="center")

        titleFont = customtkinter.CTkFont(family="Century Gothic", size=48, weight="bold")
        summaryTitleLabel = CTkLabel(mainSummaryFrame, text="Confirm Your Trip", font=titleFont)
        summaryTitleLabel.place(relx=0.5, rely=0.1, anchor="center")

        originLabel = CTkLabel(mainSummaryFrame, text="Origin:", font=customFont)
        originLabel.place(relx=0.4, rely=0.3, anchor="center")

        originFrame = CTkFrame(master=mainSummaryFrame, height=50, width=250, corner_radius=15)
        originFrame.place(relx=0.61, rely=0.305, anchor="center")

        originStationLabel = CTkLabel(originFrame, text=originStation, font=customFont)
        originStationLabel.place(relx=0.5, rely=0.5, anchor="center")

        destinationLabel = CTkLabel(mainSummaryFrame, text="Destination:", font=customFont)
        destinationLabel.place(relx=0.4, rely=0.45, anchor="center")

        destinationFrame = CTkFrame(master=mainSummaryFrame, height=50, width=250, corner_radius=15)
        destinationFrame.place(relx=0.65, rely=0.455, anchor="center")

        destStationLabel = CTkLabel(destinationFrame, text=destinationStation, font=customFont)
        destStationLabel.place(relx=0.5, rely=0.5, anchor="center")

        confirmBtn2 = CTkButton(master=mainSummaryFrame, text="Proceed", fg_color="#9966CC", hover_color="#A32CC4",
                          corner_radius=10, font=customFont, width=200, height=40,
                          command=lambda: controller.showFrame(IndexPage))
        confirmBtn2.place(relx=0.5, rely=0.9, anchor="center")

app = PageFormat()
app.mainloop()

