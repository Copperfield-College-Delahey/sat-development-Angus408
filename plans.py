import customtkinter as ctk
import xml.etree.ElementTree as ET
import os
from tkinter import messagebox
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
        messagebox.showerror("Error", f"Failed to save to previous_plans XML file\n{e}")

#Function to load plans from xml file onto software
def load_plan_from_xml(filepath):
    if not os.path.exists(filepath):
        messagebox.showerror("Error", "No previous plans file found")
        return []
    
    tree = ET.parse(filepath)
    root = tree.getroot()
    plans = []
    
    #Loops through each drill element 
    for plan in root.findall("plan"):
        plan_date = plan.find("plan_date").text
        drills = []
        for drill_elem in plan.findall("drill"):
            drill_data = {"name":drill_elem.find("drill_name").text, "duration":drill_elem.find("drill_duration").text}
            drills.append(drill_data)

        plans.append({"plan_date":plan_date, "drill":drills})

    return plans