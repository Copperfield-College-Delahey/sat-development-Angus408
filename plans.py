import customtkinter as ctk
import xml.etree.ElementTree as ET
import os
from tkinter import messagebox
from PIL import Image
from datetime import datetime

    #Function to save plans onto xml file
    def save_plan_to_xml(self, filepath):
        try:
            # If file exists, load and extend existing XML
            if os.path.exists(filepath):
                tree = ET.parse(filepath)
                root = tree.getroot()
            else:
                root = ET.Element("plans")

            plan = ET.SubElement(root, "plan")
            date_elem = ET.SubElement(plan, "plan_date")
            date_elem.text = datetime.today().strftime("%d/%m/%Y") #Gets the current date

            for drill in self.current_plan:
                drill_elem = ET.SubElement(plan, "drill")

                ET.SubElement(drill_elem, "drill_name").text = drill["name"]
                ET.SubElement(drill_elem, "drill_duration").text = drill["duration"]
                
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
            for plan in root.findall("plan"):
                plan_date = plan.find("plan_date").text

                drills = []
                for drill_elem in plan.findall("drill"):
                    drill_data = {"name":drill_elem.find("drill_name").text, "duration":drill_elem.find("drill_duration").text}
                    drills.append(drill_data)
                #Button for each previous plan which displays in scrollable frame
                plan_button = ctk.CTkButton(self.plans_display, height=50, text=plan_date, font=("Abadi", 20), text_color="black", border_width=2, border_color="#AEAEAE", corner_radius=1, fg_color="#E8E8E8", hover_color="white", command=lambda d=drills: self.display_previous_plan(d))
                plan_button.grid(pady=10, padx=10, sticky="ew")

        except FileNotFoundError:
            messagebox.showerror("Error", "Plans xml file could not be found")