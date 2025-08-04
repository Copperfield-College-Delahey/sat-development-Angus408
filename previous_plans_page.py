import customtkinter as ctk
import xml.etree.ElementTree as ET
from tkinter import messagebox
from PIL import Image

class Previous_plans_page(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller

        #Function to save plans onto xml file
        def save_plan_to_xml(self, filepath):
            try:
                root = ET.Element("plans")
                plan_elem = ET.SubElement(root, "plan")

                for row in self.current_plan[1:]:
                    ET.SubElement(plan_elem, "drill_name").text = row[1]
                    ET.SubElement(plan_elem, "drill_duration").text = str(row[0])
                
                tree = ET.ElementTree(root)
                tree.write(filepath, encoding="utf-8", xml_declaration=True)
                messagebox.showinfo("Success", "Training plan has been successfully saved")
            except Exception as e:
                messagebox.showerror("Error", "Failed to save to previous_plans XML file")

        #Function to load plans from xml file onto software
        def load_plan_from_xml(self, filepath):
            try:
                tree = ET.parse(filepath)
                root = tree.getroot()
                #Loops through each drill element 
                for plan_elem in root.findall("plan"):
                    drill_name = plan_elem.find("drill_name").text
                    drill_duration = plan_elem.find("drill_duration").text
    
            except FileNotFoundError:
                messagebox.showerror("Error", "Plans xml file could not be found")
        def display_previous_plans():
            pass
        
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

        #User search entry box
        plan_search_entry = ctk.CTkEntry(left_column, placeholder_text="Search for Previous Training Plan(s)", font=("Abadi", 20), placeholder_text_color="Black", justify="center")
        plan_search_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        #Scrollable Frame to display all previous plans
        plans_display = ctk.CTkScrollableFrame(left_column, fg_color="#F2F2F2")
        plans_display.grid(row=1, column=0, sticky="nsew")

        #Right Column, displays currently selected previous plan
        right_column = ctk.CTkFrame(self, bg_color="#F2F2F2", fg_color="#F2F2F2")
        right_column.grid(row=1, column=1, sticky="nsew")
        right_column.grid_columnconfigure(0, weight=1)
        right_column.grid_rowconfigure(0, weight=1)
        #Temporary Label
        temp = ctk.CTkLabel(right_column, text="This space will display selected previous plan")
        temp.grid(row=0, column=0)