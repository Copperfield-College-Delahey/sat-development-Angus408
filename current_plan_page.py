import customtkinter as ctk
from CTkTable import *
from PIL import Image
import tkinter as tk
from tkinter import ttk, messagebox
from drills import Drill_manager

class Current_Plan_page(ctk.CTkFrame):
    def generate_plan(self, team_age, analysis):
        plan_contents = [["Time", "Drill", "Description/POE", "Diagram"]]
        #Will keep track of drills added the plan
        added_drill_keys = set()

        for row in analysis[1:]: #Skips header row
            system_drill_search = row[0]  #Focus
            drill_search_number = row[1]  #Amount
            #Ensures system can search for either of the tags preventing error due to analysis having "Shooting & Offence"
            tags = [tag.strip() for tag in system_drill_search.split("&")]

            print(f"\nSearching for drills tagged '{system_drill_search}' for age group '{team_age}' (x{drill_search_number})")
            #Changes value to just integer eg("x3"-> 3)
            amount = int(drill_search_number.strip().lower().replace("x", ""))
            #Will keep track of amount of drills based off drill_search_number 
            added_drills = 0

            #Freethrows is a drill_name not a tage, so this is a special case kept separate from main loop
            if system_drill_search == "Freethrows":
                for drill in self.drill_manager.drills:
                    if drill.drill_name == "Freethrows":
                        drill_key = (drill.drill_name, drill.drill_description)
                        if drill_key not in added_drill_keys:
                            freethrows = [drill.drill_duration, drill.drill_name, drill.drill_description, "N/A"]
                            added_drill_keys.add(drill_key)
                            print("✅ Found Freethrows drill")
                            break

            for drill in self.drill_manager.drills:
                #Checks for matching tag, will return true if at least one matches
                print(f"Checking drill: {drill.drill_name} (tags: {drill.drill_tags}, age: {drill.drill_age})")
                if any(tag in drill.drill_tags for tag in tags):
                    #Checks if drill also matches team_age
                    if team_age in drill.drill_age:
                        #Creates key to check for duplicates
                        drill_key = (drill.drill_name, drill.drill_description)
                        #Prevents same drill being added to list again
                        if drill_key not in added_drill_keys:
                            if drill.drill_diagram != "N/A":   #Turns each drill diagram into a CtkImage allowing it to be placed into the table
                                diagram = ctk.CTkImage(light_image=Image.open(drill.drill_diagram), dark_image=Image.open(drill.drill_diagram), size=(50, 50))
                            else:
                                diagram = "N/A"  #For Drills without a diagram ie. freethrows, they remain as N/A
                            drill_details = [drill.drill_duration, drill.drill_name, drill.drill_description, diagram]
                            print(f"Checking if drill already added: {drill.drill_name} (ID: {drill.drill_id})")
                            plan_contents.append(drill_details)
                            added_drills += 1
                            added_drill_keys.add(drill_key)
                        #Stops getting drills for that focus after specific amount is reached
                        if added_drills >= amount:
                            break
        total_time = 12 #starts at 12 to count offences and freethrows which is added last (after this runs)
        
        #Calulates total time for training plan
        for row in plan_contents[1:]:
            total_time += int(row[0])

        #Most represnetative trainng sessions go for 1hr 30 min, so session must be at least 90 min
        if total_time < 90:
            for drill in self.drill_manager.drills:
                if team_age in drill.drill_age:
                        drill_key = (drill.drill_name, drill.drill_description)
                        #Prevents same drill being added to list again
                        if drill_key not in added_drill_keys:
                            if drill.drill_diagram != "N/A":   #Turns each drill diagram into a CtkImage allowing it to be placed into the table
                                diagram = ctk.CTkImage(light_image=Image.open(drill.drill_diagram), dark_image=Image.open(drill.drill_diagram), size=(50, 50))
                            else:
                                diagram = "N/A"  #For Drills without a diagram ie. freethrows, they remain as N/A
                            drill_details = [drill.drill_duration, drill.drill_name, drill.drill_description, diagram]
                            plan_contents.append(drill_details)
                            added_drill_keys.add(drill_key)
                            total_time += int(drill.drill_duration)
                        #Prevents plan from going too far over timelimit.
                        if 90 <= total_time < 100:
                            break

        #Adds freethrows later in the plan. Players are most tired at this stage so best time to practice, as though in a game
        plan_contents.append(freethrows)
        #Offences always added last. Coaches practice whatever offences their team have, hence this is not a particular drill
        offences = [10, "Offences", "Work on your teams set offensive plays. Inlcuding your baseline and sideline out of bounds", "N/A"]
        plan_contents.append(offences)

        #Table to display analysed stats
        generated_training_plan = CTkTable(master=self.plan_scrollable_frame, row=len(plan_contents), column=4, values=plan_contents, corner_radius=1, header_color="#b0b0b0", colors=["#f5f3f2", "#dedcdc"], border_width=1, border_color="#7a7878", font=("Abadi", 10), text_color="Black", wraplength=250, justify="left")
        generated_training_plan.pack(expand=True, fill="both")

        messagebox.showinfo("Success", "You have successfully generated a training plan")

    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller
        #Load Drill_manager
        self.drill_manager = Drill_manager()

        #Current Plan page content
        #Configure main grid
        self.grid_columnconfigure(0, weight=1) #Left column
        self.grid_columnconfigure(1, weight=1) #Right column
        self.grid_rowconfigure(0, weight=1)  #Main page content

        #Right Column, area to display generated training plan
        self.right_column = ctk.CTkFrame(self, bg_color="#F2F2F2", fg_color="#F2F2F2")
        self.right_column.grid(row=0, column=1, sticky="nsew")
        self.right_column.grid_propagate(True)
        self.right_column.grid_columnconfigure(0, weight=1)
        self.right_column.grid_rowconfigure(0, weight=0)

        #Scrollable frame to display generated plan
        self.plan_scrollable_frame = ctk.CTkScrollableFrame(self.right_column, height=650, width=600, fg_color="#F2F2F2")
        self.plan_scrollable_frame.grid(row=0, column=0, sticky="nsew")

        #Left Column
        left_column = ctk.CTkFrame(self, bg_color="#F2F2F2", fg_color="#F2F2F2")
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
        save_button = ctk.CTkButton(left_column, corner_radius=10, text="Download and Save", font=("ADLaM Display", 25), text_color="white", height=50, fg_color="#FF7A53", hover_color="#c7c7c7", image=save_icon, compound="right")
        save_button.grid(row=2, column=0, padx=10, pady=10, sticky="")

        #Row 1 - Left Column
        row_1 = ctk.CTkFrame(left_column, bg_color="#F2F2F2", fg_color="#F2F2F2")
        row_1.grid(row=1, column=0, sticky="ew")
        row_1.grid_columnconfigure(0, weight=1)
        row_1.grid_columnconfigure(1, weight=1)
        row_1.grid_rowconfigure(0, weight=1)

        print_icon = ctk.CTkImage(light_image=Image.open("Images/print icon.png"), dark_image=Image.open("Images/print icon.png"), size=(30, 30))
        print_button = ctk.CTkButton(row_1, corner_radius=10, text="Print Training \nPlan", font=("ADLaM Display", 25), text_color="white", height=50, fg_color="#FF7A53", hover_color="#c7c7c7", image=print_icon, compound="right")
        print_button.grid(row=0, column=0, padx=10, pady=10)

        pencil_icon = ctk.CTkImage(light_image=Image.open("Images/pencil icon.png"), dark_image=Image.open("Images/pencil icon.png"), size=(30, 30))
        edit_button = ctk.CTkButton(row_1, corner_radius=10, text="Edit Training \nPlan", font=("ADLaM Display", 25), text_color="white", height=50, fg_color="#FF7A53", hover_color="#c7c7c7", image=pencil_icon, compound="right")
        edit_button.grid(row=0, column=1, padx=10, pady=10)