import customtkinter as ctk
import xml.etree.ElementTree as ET
import os
from tkinter import messagebox

#Function to save plans onto xml file
def save_plan_to_xml(filepath, plans):
    print("Hello")
    # If file exists, load and extend existing XML
    if os.path.exists(filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
    else:
        root = ET.Element("plans")
    print("Plans received:", plans)
    #save individual plans
    for plan in plans:
        print("hi")
        plan_elem = ET.SubElement(root, "plan")
        date_elem = ET.SubElement(plan_elem, "plan_date")
        date_elem.text = plan['date']
        
        for drill in plan["drills"]:
            print(drill)
            drill_elem = ET.SubElement(plan_elem, "drill")
            ET.SubElement(drill_elem, "drill_name").text = drill["name"]
            ET.SubElement(drill_elem, "drill_duration").text = str(drill["duration"])
            
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding="utf-8", xml_declaration=True)

    messagebox.showinfo("Success", "Training plan has been successfully saved to previous_plans.xml")

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