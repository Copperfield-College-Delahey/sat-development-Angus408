import xml.etree.ElementTree as ET
from tkinter import messagebox

#Class for drills to be based off
class Drill:
    def __init__(self, drill_id, drill_name, drill_tags, drill_age, drill_description, drill_duration, drill_diagram):
        self.drill_id = int(drill_id)  #drill_id can only be an integer
        self.drill_name = drill_name
        self.drill_tags = [tag.strip() for tag in drill_tags] #Already a list
        self.drill_age = [age.strip() for age in drill_age.split(",")]
        self.drill_description = drill_description
        self.drill_duration = int(drill_duration)  #drill_duration can only be an integer
        # Only prepend if not already present
        if not drill_diagram.startswith("drill_diagrams/"):
            self.drill_diagram = "drill_diagrams/" + drill_diagram.lstrip("/")
        else:
            self.drill_diagram = drill_diagram

#Class to manage all drills and related functions
class Drill_manager:
    def __init__(self):
        self.drills = []
    #Function to save drills onto xml file
    def save_to_xml(self, filepath):
        root = ET.Element("drills")
        for drill in self.drills:
            drill_elem = ET.SubElement(root, "drill")

            ET.SubElement(drill_elem, "drill_id").text = str(drill.drill_id)
            ET.SubElement(drill_elem, "drill_name").text = drill.drill_name
            ET.SubElement(drill_elem, "drill_tags").text = ",".join(drill.drill_tags) #Converts back to string
            ET.SubElement(drill_elem, "drill_age").text = ",".join(drill.drill_age) #Converts back to string
            ET.SubElement(drill_elem, "drill_description").text = drill.drill_description
            ET.SubElement(drill_elem, "drill_duration").text = str(drill.drill_duration)
            ET.SubElement(drill_elem, "drill_diagram").text = drill.drill_diagram
            
        tree = ET.ElementTree(root)
        tree.write(filepath, encoding="utf-8", xml_declaration=True)

    #Function to load drills from xml file onto software
    def load_from_xml(self, filepath):
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            #Loops through each drill element 
            for drill_elem in root.findall("drill"):
                drill_id = drill_elem.find("drill_id").text
                drill_name = drill_elem.find("drill_name").text
                drill_tags = (drill_elem.find("drill_tags").text).split(",")  #Turns values into list at each comma
                drill_age = drill_elem.find("drill_age").text
                drill_description = drill_elem.find("drill_description").text
                drill_duration = drill_elem.find("drill_duration").text
                drill_diagram = drill_elem.find("drill_diagram").text
                #Create drill and add it to the list of drills
                drill = Drill(drill_id, drill_name, drill_tags, drill_age, drill_description, drill_duration, drill_diagram)
                self.drills.append(drill)
        except FileNotFoundError:
            messagebox.showerror("Error", "Drills xml file could not be found")