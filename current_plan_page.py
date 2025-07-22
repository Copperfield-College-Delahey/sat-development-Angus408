import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import ttk, messagebox

class Current_Plan_page(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller

        #Current Plan page content
        #Configure main grid
        self.grid_columnconfigure(0, weight=1) #Left column
        self.grid_columnconfigure(1, weight=1) #Right column
        self.grid_rowconfigure(1, weight=1)  #Main page content

        def generate_plan(self, team_age):
            pass


        #Left Column
        left_column = ctk.CTkFrame(self, width=600, bg_color="#F2F2F2", fg_color="#F2F2F2")
        left_column.grid(row=0, column=0, sticky="nsew")
        left_column.grid_columnconfigure(0, weight=1)
        left_column.grid_rowconfigure(0, weight=0)
        left_column.grid_rowconfigure(1, weight=1)
        left_column.grid_rowconfigure(2, weight=1)

        #Navigation bar. Appears only in top of left column allowing more space for training plan to be displayed
        navigation_bar = ctk.CTkFrame(left_column, height=35, bg_color="#00A29E", fg_color="#00A29E")
        navigation_bar.grid(row=0, column=0, sticky="ew")
        navigation_bar.grid_columnconfigure(0, weight=1)
        navigation_bar.grid_columnconfigure(1, weight=1)
        navigation_bar.grid_columnconfigure(2, weight=1)
        navigation_bar.grid_columnconfigure(3, weight=1)
        navigation_bar.grid_columnconfigure(4, weight=1)
        navigation_bar.grid_columnconfigure(5, weight=1)
        navigation_bar.grid_rowconfigure(0, weight=1)

        home_button = ctk.CTkButton(navigation_bar, width=120, height=40, text="Home", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#c7c7c7")
        home_button.grid(row=0, column=0, sticky="e")
        home_icon= ctk.CTkImage(light_image=Image.open("Images/white home icon.png"), dark_image=Image.open("Images/white home icon.png"), size=(35, 35))
        home_icon_button = ctk.CTkButton(navigation_bar, text="", image=home_icon, bg_color="#00A29E", fg_color="#00A29E", height=30, width=35, hover_color="#c7c7c7")
        home_icon_button.grid(row=0, column=1, sticky="w")
        #Configure buttons to display the home page
        home_button.configure(command=lambda: self.show_frame("Home_page"))
        home_icon_button.configure(command=lambda: self.show_frame("Home_page"))

        drills_button = ctk.CTkButton(navigation_bar, height=40, text="Drills", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#00A29E")
        drills_button.grid(row=0, column=2, sticky="e")
        drills_icon= ctk.CTkImage(light_image=Image.open("Images/white drills icon.png"), dark_image=Image.open("Images/white drills icon.png"), size=(35, 35))
        drills_icon_button = ctk.CTkButton(navigation_bar, text="", image=drills_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#00A29E")
        drills_icon_button.grid(row=0, column=3, sticky="w")
        #Configure buttons to display the drills page
        drills_button.configure(command=lambda: self.show_frame("Drills_page"))
        drills_icon_button.configure(command=lambda: self.show_frame("Drills_page"))

        previous_plans_button = ctk.CTkButton(navigation_bar, height=40, text="Previous Training Plans", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#c7c7c7")
        previous_plans_button.grid(row=0, column=4, sticky="e")
        file_icon= ctk.CTkImage(light_image=Image.open("Images/white file icon.png"), dark_image=Image.open("Images/white file icon.png"), size=(35, 35))
        file_icon_button = ctk.CTkButton(navigation_bar, text="", image=file_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#c7c7c7")
        file_icon_button.grid(row=0, column=5, sticky="w")
        #Configure buttons to display the previous plans page
        previous_plans_button.configure(command=lambda: self.show_frame("Previous_plans_page"))
        file_icon_button.configure(command=lambda: self.show_frame("Previous_plans_page"))

        save_icon = ctk.CTkImage(light_image=Image.open("Images/save icon.png"), dark_image=Image.open("Images/save icon.png"), size=(30, 30))
        save_button = ctk.CTkButton(left_column, corner_radius=10, text="Save Training \nPlan", font=("ADLaM Display", 25), text_color="white", height=50, fg_color="#FF7A53", hover_color="#c7c7c7", image=save_icon, compound="right")
        save_button.grid(row=2, column=0, padx=10, pady=10, sticky="")

        #Row 1 - Left Column
        row_1 = ctk.CTkFrame(left_column, bg_color="#F2F2F2", fg_color="#F2F2F2")
        row_1.grid(row=1, column=0, sticky="ew")
        row_1.grid_columnconfigure(0, weight=1)
        row_1.grid_columnconfigure(1, weight=1)
        row_1.grid_rowconfigure(0, weight=1)

        print_icon = ctk.CTkImage(light_image=Image.open("Images/print icon.png"), dark_image=Image.open("Images/print icon.png"), size=(30, 30))
        print_button = ctk.CTkButton(row_1, corner_radius=10, text="Print Training \nPlan", font=("ADLaM Display", 25), text_color="white", height=50, fg_color="#FF7A53", hover_color="#c7c7c7", image=print_icon, compound="right")
        print_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        pencil_icon = ctk.CTkImage(light_image=Image.open("Images/pencil icon.png"), dark_image=Image.open("Images/pencil icon.png"), size=(30, 30))
        edit_button = ctk.CTkButton(row_1, corner_radius=10, text="Edit Training \nPlan", font=("ADLaM Display", 25), text_color="white", height=50, fg_color="#FF7A53", hover_color="#c7c7c7", image=pencil_icon, compound="right")
        edit_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        #Right Column, area to display generated training plan
        right_column = ctk.CTkFrame(self, width=600, bg_color="#F2F2F2", fg_color="#F2F2F2")
        right_column.grid(row=0, column=1, sticky="nsew")
        right_column.grid_columnconfigure(0, weight=1)
        right_column.grid_rowconfigure(0, weight=1)

        #Temporary Label
        temp = ctk.CTkLabel(right_column, text="This space will display the currently generated plan")
        temp.grid(row=0, column=0)