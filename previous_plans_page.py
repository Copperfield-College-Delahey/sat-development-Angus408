import customtkinter as ctk
import xml.etree.ElementTree as ET
import os
from tkinter import messagebox
from PIL import Image
from datetime import datetime
from plans import load_plan_from_xml

class Previous_plans_page(ctk.CTkFrame):
    #Function to display previous plans in searchable and scrollable frame
    def display_previous_plan(self, drills):
        for widget in self.right_column.winfo_children():
            widget.destroy()
        
        for i, drill in enumerate(drills):
            drill_label = ctk.CTkLabel(self.right_column, text=f"   {drill['name']}   -   {drill['duration']} mins   ", font=("Abadi", 20), text_color="black", corner_radius=1, fg_color="#E8E8E8")
            drill_label.grid(row=i, column=0, pady=10, padx=10, sticky="ns")

    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller
        
        #Previous plans Page content
        #Configure main grid
        self.grid_columnconfigure(0, weight=1) #Left column
        self.grid_columnconfigure(1, weight=1) #Right column
        self.grid_rowconfigure(0, weight=0)  #Top navigation bar
        self.grid_rowconfigure(1, weight=1)  #Main page content

        #Navigation bar
        navigation_bar = ctk.CTkFrame(self, height=35, bg_color="#00A29E", fg_color="#00A29E")
        navigation_bar.grid(row=0, column=0, columnspan=2, sticky="new")
        navigation_bar.grid_columnconfigure(0, weight=1)
        navigation_bar.grid_columnconfigure(1, weight=1)
        navigation_bar.grid_columnconfigure(2, weight=1)
        navigation_bar.grid_columnconfigure(3, weight=1)
        navigation_bar.grid_columnconfigure(4, weight=1)
        navigation_bar.grid_columnconfigure(5, weight=1)
        navigation_bar.grid_columnconfigure(6, weight=1)
        navigation_bar.grid_columnconfigure(7, weight=1)
        navigation_bar.grid_columnconfigure(8, weight=1)
        navigation_bar.grid_columnconfigure(9, weight=1)
        navigation_bar.grid_columnconfigure(10, weight=1)
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

        current_plan_button = ctk.CTkButton(navigation_bar, height=40, text="Current Plan", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#00A29E")
        current_plan_button.grid(row=0, column=9, sticky="e")
        pencil_icon= ctk.CTkImage(light_image=Image.open("Images/pencil icon.png"), dark_image=Image.open("Images/pencil icon.png"), size=(35, 35))
        pencil_icon_button = ctk.CTkButton(navigation_bar, text="", image=pencil_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#00A29E")
        pencil_icon_button.grid(row=0, column=10, sticky="w")
        #Configure buttons to display current plan page
        current_plan_button.configure(command=lambda: self.show_frame("Current_Plan_page"))
        pencil_icon_button.configure(command=lambda: self.show_frame("Current_Plan_page"))


        #Left Column, displays previous plans with entry box to search for previous plans
        left_column = ctk.CTkFrame(self, width=600, bg_color="#F2F2F2", fg_color="#F2F2F2")
        left_column.grid(row=1, column=0, sticky="nsew")
        left_column.grid_columnconfigure(0, weight=1)
        left_column.grid_rowconfigure(0, weight=1)
        left_column.grid_rowconfigure(1, weight=1)

        '''Due to time constraints the search feature has not been constructed.This is a minor 
        feature and coaches still have the ability to mannually scroll through previous plans.
        This function will be completed should the software be scaled further'''

        #User search entry box
        self.plan_search_entry = ctk.CTkEntry(left_column, placeholder_text="Search for Previous Training Plan(s)", font=("Abadi", 20), placeholder_text_color="Black", justify="center")
        self.plan_search_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        #Scrollable Frame to display all previous plans
        self.plans_display = ctk.CTkScrollableFrame(left_column, fg_color="#F2F2F2")
        self.plans_display.grid(row=1, column=0, sticky="nsew")

        #Right Column, displays currently selected previous plan
        self.right_column = ctk.CTkFrame(self, bg_color="#F2F2F2", fg_color="#F2F2F2")
        self.right_column.grid(row=1, column=1, sticky="nsew")
        self.right_column.grid_columnconfigure(0, weight=1)
        self.right_column.grid_rowconfigure(0, weight=0)

        #Loads and displays previous plans
        plans = load_plan_from_xml("previous_plans.xml")
        #print("loaded plans:", plans)

        for i, plan in enumerate(plans):
            #Button for each previous plan which displays in scrollable frame
            plan_button = ctk.CTkButton(self.plans_display, height=50, text=plan["plan_date"], font=("Abadi", 20), text_color="black", border_width=2, border_color="#AEAEAE", corner_radius=1, fg_color="#E8E8E8", hover_color="white", command=lambda p=plan: self.display_previous_plan(p.get("drills", p.get("drill", []))))
            plan_button.grid(row=i, column=0, pady=10, padx=10, sticky="ew")

        #Description label, tells users that drills within selected plan will display here
        description_label = ctk.CTkLabel(self.right_column, text="Click on plan to display its consisting drills here", font=("Abadi", 20))
        description_label.grid(pady=50, padx=10, sticky="sew")