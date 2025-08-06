import customtkinter as ctk
from PIL import Image
import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from drills import Drill_manager
from drills import Drill

class Drills_page(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller
        #Load Drill_manager
        self.drill_manager = Drill_manager()
        #Call function to load drills from xml file
        self.drill_manager.load_from_xml("drills.xml")

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
            if len(user_drills_search) <= 2:
                messagebox.showerror("Error", "Please enter more than two characters to search")
                self.display_drills()
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

        #Function to display new window with entry fields for users to add new drill
        def add_new_drill():
            #Function allows user to select a png image to set as their added drills diagram
            def select_diagram():
                self.file_path = filedialog.askopenfilename(title="Select Drill Diagram", filetypes=[("Image Files", "*.png")])

                if self.file_path:
                    try:
                        print("Diagram:", self.file_path)
                        diagram_button.configure(text=os.path.basename(self.file_path))
                    except Exception as e:
                        messagebox.showerror("Error", "Failed to load diagram. Please ensure you select a png file")
                else:
                    messagebox.showerror("Error", "No diagram selected")

            #Function runs once user clicks save on window, adding drill to system. Nested here to access all entry widgets.
            def save_new_drill():
                new_drill_name = name_entry.get().strip().title()
                #Validation confirms user has entered a drill name, and that the drill name doesn't already exist
                if not new_drill_name:
                    messagebox.showerror("Error", "Please enter a Drill Name")
                    return
                if any(drill.drill_name == new_drill_name for drill in self.drill_manager.drills):
                    messagebox.showerror("Error", "A drill with this name already exists")
                    return
                
                valid_tags = ["Shooting", "Passing", "Rebounding", "Defence", "Offence", "Dribbling"]
                new_drill_tags = tags_entry.get().strip().capitalize()
                #Validates user has entered a drill tag or tags and that they are acceptable tags
                if not new_drill_tags:
                    messagebox.showerror("Error", "Please enter a tag or tags")
                    return
                new_tag_list = [tag.strip().capitalize() for tag in new_drill_tags.split(",")]
                if not all(tag in valid_tags for tag in new_tag_list):
                    messagebox.showerror("Error", "Please enter a valid drill tag or tags seperated by commas.\nEtiher or multiple of Shooting, Passing, Rebounding, Defence, Offence, Dribbling")
                    return

                valid_ages = ["U8s", "U10s", "U12s", "U14s", "U16s", "U18s", "U20s"] #List of valid ages to refer to in validation
                new_drill_age = age_entry.get().strip()
                #Validates user has entered a drill age, and that it is an acceptable correct age
                if not new_drill_age:
                    messagebox.showerror("Error", "Please enter a Drill Age")
                    return
                new_drill_age_list = [age.strip().capitalize() for age in new_drill_age.split(",")]
                if not all(age in valid_ages for age in new_drill_age_list):
                    messagebox.showerror("Error", "Please enter a valid drill age or ages seperated by commas.\nEtiher or multiple of U8s, U10s, U12s, U14s, U16s, U18s, U20s")
                    return
                #Validates drill duration isn't blank and is between 1 and 40
                try: 
                    new_drill_duration = int(duration_entry.get().strip())
                    if not (1 <= new_drill_duration <= 40):
                        messagebox.showerror("Error", "Please enter a drill duration between 1 and 40")
                        return
                except ValueError:
                    messagebox.showerror("Error", "Drill duration must be a number")
                    return
                
                new_drill_description = description_entry.get("1.0", "end-1c").strip()
                #validates drill description has been entered and is between 10 and 90 words (around 50 and 630 character)
                if len(new_drill_description) < 50 or len(new_drill_description) > 630:
                    messagebox.showerror("Error", "Please enter a valid description betweem 50 and 630 characters")
                    return
                
                #Saves the selected drill diagram into the drill_diagrams folder
                #Done with assitance of ChatGPT
                if not hasattr(self, "file_path") or not self.file_path:
                    messagebox.showerror("Error", "Please select a drill diagram")
                    return
                try:
                    os.makedirs("drill_diagrams", exist_ok=True)
                    filename = os.path.basename(self.file_path).replace(" ", "_").lower()
                    target_path = os.path.join("drill_diagrams", filename)
                    shutil.copy(self.file_path, target_path)
                    new_drill_diagram = os.path.splitext(filename)[0]
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to copy image: {e}")
                    return
                
                #Generating new id, done with assistance of Chat GPT
                last_drill_id = int(self.drill_manager.drills[-1].drill_id) #Gets the id of the last drill within the list of drills and coverts to integer
                new_drill_id = str(last_drill_id + 1).zfill(4)  #Adds one to the value and converts back to a string, with 4 digits eg:"0004"

                new_drill = Drill(new_drill_id, new_drill_name, new_drill_tags, new_drill_age, new_drill_description, new_drill_duration, new_drill_diagram)
                self.drill_manager.drills.append(new_drill)
                self.drill_manager.save_to_xml("drills.xml") #Permanently saves new drill to xml file
                self.display_drills() #Updates drills display
                messagebox.showinfo("Success", f"{new_drill_name} has been added!")
                new_drill_popup.destroy()
            
            new_drill_popup = ctk.CTkToplevel(fg_color="#F2F2F2")
            new_drill_popup.title("Add new Drill")
            new_drill_popup.geometry("600x500")
            new_drill_popup.transient(parent)  #Ensures the window opens up and remains above parent
            new_drill_popup.grab_set()  #Prevents users from interacting with other windows
            new_drill_popup.grid_columnconfigure(0, weight=1)
            new_drill_popup.grid_columnconfigure(1, weight=1)
            new_drill_popup.grid_rowconfigure(0, weight=1)
            new_drill_popup.grid_rowconfigure(1, weight=1)
            new_drill_popup.grid_rowconfigure(2, weight=1)
            new_drill_popup.grid_rowconfigure(3, weight=1)

            #User input fields
            name_entry = ctk.CTkEntry(new_drill_popup, placeholder_text="Enter Drill Name", font=("Abadi", 14), placeholder_text_color="Black", justify="center")
            name_entry.grid(row=0, column=0)
            tags_entry = ctk.CTkEntry(new_drill_popup, placeholder_text="Enter Drill Tag(s)", font=("Abadi", 14), placeholder_text_color="Black", justify="center")
            tags_entry.grid(row=0, column=1)
            age_entry = ctk.CTkEntry(new_drill_popup, placeholder_text="Enter Drill Age(s)", font=("Abadi", 14), placeholder_text_color="Black", justify="center")
            age_entry.grid(row=1, column=0)
            duration_entry = ctk.CTkEntry(new_drill_popup, placeholder_text="Enter Drill Duration", font=("Abadi", 14), placeholder_text_color="Black", justify="center")
            duration_entry.grid(row=1, column=1)
            textbox_label = ctk.CTkLabel(new_drill_popup, text="Enter Drill Description in\n textbox on the right", font=("Abadi", 14), text_color="Black", justify="center")
            textbox_label.grid(row=2, column=0)
            description_entry = ctk.CTkTextbox(new_drill_popup, border_width=2, border_color="#AEAEAE")
            description_entry.grid(row=2, column=1)

            #Button to select diagram
            picture_icon = ctk.CTkImage(light_image=Image.open("Images/picture icon.png"), dark_image=Image.open("Images/picture icon.png"), size=(15, 15))
            diagram_button = ctk.CTkButton(new_drill_popup, text="Select Drill Diagram", corner_radius=10, font=("ADLaM Display", 18), text_color="White", fg_color="#FF7A53", hover_color="#c7c7c7", image=picture_icon, compound="right", command=select_diagram)
            diagram_button.grid(row=3, column=0)

            #Button to save new drill
            save_icon = ctk.CTkImage(light_image=Image.open("Images/save icon.png"), dark_image=Image.open("Images/save icon.png"), size=(15, 15))
            save_button = ctk.CTkButton(new_drill_popup, corner_radius=10, text="Save New Drill", font=("ADLaM Display", 18), text_color="White", hover_color="#c7c7c7", fg_color="#7ec76b", image=save_icon, compound="right", command=save_new_drill)
            save_button.grid(row=3, column=1)

        new_drill_button = ctk.CTkButton(left_column, corner_radius=10, text="Add New Drill", font=("ADLaM Display", 25), text_color="white", height=65, width=100, fg_color="#FF7A53", hover_color="#c7c7c7", command=add_new_drill)
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

