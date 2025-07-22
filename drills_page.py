import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import ttk, messagebox
from drills import Drill_manager

class Drills_page(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller
        
        #Load Drill_manager
        self.drill_manager = Drill_manager()

        #Drills Page content
        #Configure main grid
        self.grid_columnconfigure(0, weight=1) #Left column
        self.grid_columnconfigure(1, weight=1) #Right column
        self.grid_rowconfigure(0, weight=0)  #Top navigation bar
        self.grid_rowconfigure(1, weight=1)  #Main page content

        #Navigation bar
        navigation_bar = ctk.CTkFrame(self, height=35, bg_color="#00A29E", fg_color="#00A29E")
        navigation_bar.grid(row=0, column=0, columnspan=2, sticky="ew")
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

        drills_button = ctk.CTkButton(navigation_bar, height=40, text="Drills", font=("ADLaM Display", 20), text_color="light grey", border_width=2, border_color="light grey", fg_color="#16CCCC", hover_color="#00A29E")
        drills_button.grid(row=0, column=5, sticky="e")
        drills_icon= ctk.CTkImage(light_image=Image.open("Images/grey drills icon.png"), dark_image=Image.open("Images/grey drills icon.png"), size=(35, 35))
        drills_icon_button = ctk.CTkButton(navigation_bar, text="", image=drills_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#00A29E")
        drills_icon_button.grid(row=0, column=6, sticky="w")
        #Configure buttons to display the drills page
        drills_button.configure(command=lambda: self.show_frame("Drills_page"))
        drills_icon_button.configure(command=lambda: self.show_frame("Drills_page"))

        previous_plans_button = ctk.CTkButton(navigation_bar, height=40, text="Previous Training Plans", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#c7c7c7")
        previous_plans_button.grid(row=0, column=7, sticky="e")
        file_icon= ctk.CTkImage(light_image=Image.open("Images/white file icon.png"), dark_image=Image.open("Images/white file icon.png"), size=(35, 35))
        file_icon_button = ctk.CTkButton(navigation_bar, text="", image=file_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#c7c7c7")
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

        #Main content of drills_page
        #Function to display drills details once button in scrollframe is clicked
        def show_drill(drill):
            #converts diagram to CTk Image object
            diagram = Image.open(drill.drill_diagram)
            diagram_image = ctk.CTkImage(light_image=diagram, size=(200, 200))
            diagram_label.configure(text="", image=diagram_image)
            #Displays Drill and its features in frame
            row2.configure(border_width=2, border_color="#AEAEAE")
            name_label.configure(text=drill.drill_name)
            duration_label.configure(text=f"{drill.drill_duration} min   |")
            age_label.configure(text=",".join(drill.drill_age))
            tags_label.configure(text=",".join(drill.drill_tags))
            description_label.configure(text=drill.drill_description)


        #Left Column, add new drill button and option to search drills database for particular drill(s)
        left_column = ctk.CTkFrame(self, width=600, bg_color="#F2F2F2", fg_color="#F2F2F2")
        left_column.grid(row=1, column=0, sticky="nsew")
        left_column.grid_columnconfigure(0, weight=1)
        left_column.grid_rowconfigure(0, weight=1)
        left_column.grid_rowconfigure(1, weight=1)
        left_column.grid_rowconfigure(2, weight=1)

        #Function to search through drills based on users entry
        def search_drills(self):
            user_drills_search = drill_search_entry.get().strip().lower()
            relevant_drills = []

            #Validates whether box is empty
            if not user_drills_search:
                self.display_drills()
            #validates user has entered more than just two letters
            if len(user_drills_search) < 2:
                messagebox.showerror("Error", "Please enter more than two characters to search")
            
            for drill in self.drill_manager.drills:
                #Checks for matching name
                if user_drills_search in drill.drill_name.lower():
                    if drill not in relevant_drills:
                        relevant_drills.append(drill)
                #Checks for matching tag, will return true if at least one matches
                if any(user_drills_search in tag.lower() for tag in drill.drill_tags):
                    #Prevents same drill being added to list again
                    if drill not in relevant_drills:
                        relevant_drills.append(drill)

            #validates if a drill has been found and placed into relevant_drills list
            if not relevant_drills:
                messagebox.showerror("Error", "No Drill Found")
                return
            
            #Clears frame, preventing double-ups
            for widget in drills_display.winfo_children():
                widget.destroy()

            #Creates two columns within scrollable frame for buttons to appear side by side
            columns = 2
            #Allows for columns to be given a weight and centered
            for i in range(columns):
                drills_display.grid_columnconfigure(i, weight=1)

            #index(posistion) is needed to determine rows and columns. Enumerate allows this to happen, adding a counter to the list
            for index, drill in enumerate(relevant_drills):
                #Determines the row and column the drill should be placed based on those already filled
                row = index // columns
                column = index % columns

                drill_button = ctk.CTkButton(drills_display, height=50, text=drill.drill_name, font=("Abadi", 20), text_color="black", border_width=2, border_color="#AEAEAE", corner_radius=1, fg_color="#E8E8E8", hover_color="white", command=lambda d=drill: show_drill(d))
                drill_button.grid(row=row, column=column, pady=10, padx=10, sticky="ew")
                
            #Clears entry box
            drill_search_entry.delete(0, ctk.END)

        #User entry box to search for particular drill(s)
        drill_search_entry = ctk.CTkEntry(left_column, corner_radius=1, placeholder_text="Search for Drill(s) using name or tag(s) and clicking enter", font=("Abadi", 18), placeholder_text_color="Black", justify="center")
        drill_search_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        #Runs search_drills function once user clicks enter on their keyboard
        drill_search_entry.bind("<Return>", lambda event: search_drills(self))

        #Scrollable Frame to display all drills
        drills_display = ctk.CTkScrollableFrame(left_column, fg_color="#F2F2F2")
        drills_display.grid(row=2, column=0, sticky="nsew")


        #Method to display drills within drills_display
        def display_drills(self):
            #Clears frame, preventing double-ups
            for widget in drills_display.winfo_children():
                widget.destroy()

            #Creates two columns within scrollable frame for buttons to appear side by side
            columns = 2
            #Allows for columns to be given a weight and centered
            for i in range(columns):
                drills_display.grid_columnconfigure(i, weight=1)

            #index(posistion) is needed to determine rows and columns. Enumerate allows this to happen, adding a counter to the list
            for index, drill in enumerate(self.drill_manager.drills):
                #Determines the row and column the drill should be placed based on those already filled
                row = index // columns
                column = index % columns

                drill_button = ctk.CTkButton(drills_display, height=50, text=drill.drill_name, font=("Abadi", 20), text_color="black", border_width=2, border_color="#AEAEAE", corner_radius=1, fg_color="#E8E8E8", hover_color="white", command=lambda d=drill: show_drill(d))
                drill_button.grid(row=row, column=column, pady=10, padx=10, sticky="ew")

        #Allows display_drills to run automatically when page is opened
        self.display_drills = display_drills.__get__(self)
        self.display_drills()

        
        new_drill_button = ctk.CTkButton(left_column, corner_radius=10, text="Add New Drill", font=("ADLaM Display", 25), text_color="white", height=65, width=100, fg_color="#FF7A53", hover_color="#c7c7c7")
        new_drill_button.grid(row=0, column=0, padx=10, pady=10)


        #Right Column, area to display selected drill or new drill
        right_column = ctk.CTkFrame(self, width=500, bg_color="#F2F2F2", fg_color="#F2F2F2", border_width=2, border_color="#AEAEAE")
        right_column.grid(row=1, column=1, sticky="nsew")
        right_column.grid_columnconfigure(0, weight=1)
        right_column.grid_rowconfigure(0, weight=1)
        right_column.grid_rowconfigure(1, weight=1)
        right_column.grid_rowconfigure(2, weight=1)
        right_column.grid_rowconfigure(3, weight=1)
        right_column.grid_rowconfigure(4, weight=1)

        #Labels to display all details of selected drill
        diagram_label = ctk.CTkLabel(right_column, text="", font=("Abadi", 20), text_color="black")
        diagram_label.grid(row=0, column=0)

        name_label = ctk.CTkLabel(right_column, text="Click on Drill to display it here", font=("Abadi", 25), text_color="black")
        name_label.grid(row=1, column=0)

        tags_label = ctk.CTkLabel(right_column, text="", font=("Abadi", 18), text_color="black")
        tags_label.grid(row=3, column=0, sticky="n")

        description_label = ctk.CTkLabel(right_column, text="", font=("Abadi", 20), text_color="black", wraplength=350, justify="left")
        description_label.grid(row=4, column=0, sticky="n")

        #configure row 2 to have 2 columns
        row2 = ctk.CTkFrame(right_column, fg_color="#F2F2F2")
        row2.grid(row=2, column=0, sticky="n")
        row2.grid_columnconfigure(0, weight=1)
        row2.grid_columnconfigure(1, weight=1)
        row2.grid_rowconfigure(0, weight=1)

        duration_label = ctk.CTkLabel(row2, text="", font=("Abadi", 15), text_color="black")
        duration_label.grid(row=0, column=0, sticky="ne", pady=5, padx=5)
        age_label = ctk.CTkLabel(row2, text="", font=("Abadi", 15), text_color="black")
        age_label.grid(row=0, column=1, padx=5, pady=5, sticky="n")

