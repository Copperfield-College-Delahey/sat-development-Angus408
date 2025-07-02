import customtkinter as ctk
from PIL import Image

class Previous_plans_page(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller
        
        #Drills Page content
        #Configure main grid
        self.grid_columnconfigure(0, weight=1) #Left column
        self.grid_columnconfigure(1, weight=1) #Right column
        self.grid_rowconfigure(0, weight=1)  #Top navigation bar
        self.grid_rowconfigure(1, weight=1)  #Main page content

        #Navigation bar
        navigation_bar = ctk.CTkFrame(self, height=35, bg_color="#00A29E", fg_color="#00A29E")
        navigation_bar.grid(row=0, column=0, columnspan=2, sticky="nsew")
        navigation_bar.grid_columnconfigure(0, weight=1)
        navigation_bar.grid_columnconfigure(1, weight=1)
        navigation_bar.grid_columnconfigure(2, weight=1)
        navigation_bar.grid_columnconfigure(3, weight=1)
        navigation_bar.grid_columnconfigure(4, weight=1)
        navigation_bar.grid_columnconfigure(5, weight=1)
        navigation_bar.grid_columnconfigure(6, weight=1)
        navigation_bar.grid_columnconfigure(7, weight=1)
        navigation_bar.grid_columnconfigure(8, weight=1)
        navigation_bar.grid_rowconfigure(0, weight=1)

        logo = ctk.CTkImage(light_image=Image.open("Images/Stats Logo.png"), size=(75, 75))
        logo_label = ctk.CTkLabel(navigation_bar, text="", image=logo)
        logo_label.grid(row=0, column=0, sticky="nsew")

        title_label = ctk.CTkLabel(navigation_bar, text="Stats2Drills", font=("ADLaM Display", 40), text_color="White")
        title_label.grid(row=0, column=1, columnspan=2, sticky="nsew")

        home_button = ctk.CTkButton(navigation_bar, width=120, height=40, text="Home", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#c7c7c7")
        home_button.grid(row=0, column=3, sticky="e")
        home_icon= ctk.CTkImage(light_image=Image.open("Images/white home icon.png"), dark_image=Image.open("Images/white home icon.png"), size=(35, 35))
        home_icon_button = ctk.CTkButton(navigation_bar, text="", image=home_icon, bg_color="#00A29E", fg_color="#00A29E", height=30, width=35, hover_color="#c7c7c7")
        home_icon_button.grid(row=0, column=4, sticky="w")
        #Configure home_button to display the home page
        home_button.configure(command=lambda: self.show_frame("Home_page"))
        home_icon_button.configure(command=lambda: self.show_frame("Home_page"))

        drills_button = ctk.CTkButton(navigation_bar, height=40, text="Drills", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#c7c7c7")
        drills_button.grid(row=0, column=5, sticky="e")
        drills_icon= ctk.CTkImage(light_image=Image.open("Images/white drills icon.png"), dark_image=Image.open("Images/white drills icon.png"), size=(35, 35))
        drills_icon_button = ctk.CTkButton(navigation_bar, text="", image=drills_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#c7c7c7")
        drills_icon_button.grid(row=0, column=6, sticky="w")
        #Configure buttons to display the drills page
        drills_button.configure(command=lambda: self.show_frame("Drills_page"))
        drills_icon_button.configure(command=lambda: self.show_frame("Drills_page"))

        previous_plans_button = ctk.CTkButton(navigation_bar, height=40, text="Previous Training Plans", font=("ADLaM Display", 20), text_color="light grey", border_width=2, border_color="light grey", fg_color="#16CCCC", hover_color="#00A29E")
        previous_plans_button.grid(row=0, column=7, sticky="e")
        file_icon= ctk.CTkImage(light_image=Image.open("Images/grey file icon.png"), dark_image=Image.open("Images/grey file icon.png"), size=(35, 35))
        file_icon_button = ctk.CTkButton(navigation_bar, text="", image=file_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#00A29E")
        file_icon_button.grid(row=0, column=8, sticky="w")
        #Configure buttons to display the previous plans page
        previous_plans_button.configure(command=lambda: self.show_frame("Previous_plans_page"))
        file_icon_button.configure(command=lambda: self.show_frame("Previous_plans_page"))