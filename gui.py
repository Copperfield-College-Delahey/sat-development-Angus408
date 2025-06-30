'''Stats2Drills GUI Application. date started: 23/06/2025'''

import customtkinter as ctk
from PIL import Image
app = ctk.CTk()
app.title("Stats2Drills GUI Interface")
app.geometry("1250x700")

#Configure main grid
app.grid_columnconfigure(0, weight=1) #Left column
app.grid_columnconfigure(1, weight=1) #Right column
app.grid_rowconfigure(0, weight=1)  #Top navigation bar
app.grid_rowconfigure(1, weight=1)  #Main page content

#Top Navigation bar
navigation_bar = ctk.CTkFrame(app, bg_color="#00A29E", fg_color="#00A29E")
navigation_bar.grid(row=0, column=0, columnspan=2, sticky="nsew")
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

home_button = ctk.CTkButton(navigation_bar, text="Home", font=("ADLaM Display", 15), fg_color="#16CCCC")
home_button.grid(row=0, column=3)
home_icon= ctk.CTkImage(light_image=Image.open("Images/white home icon.png"), dark_image=Image.open("Images/white home icon.png"), size=(35, 35))
home_icon_button = ctk.CTkButton(navigation_bar, text="", image=home_icon, bg_color="#00A29E", fg_color="#00A29E")
home_icon_button.grid(row=0, column=4, sticky="nsew")

drills_button = ctk.CTkButton(navigation_bar, text="Drills", font=("ADLaM Display", 15), fg_color="#16CCCC")
drills_button.grid(row=0, column=5)
drills_icon= ctk.CTkImage(light_image=Image.open("Images/white drills icon.png"), dark_image=Image.open("Images/white drills icon.png"), size=(35, 35))
drills_icon_button = ctk.CTkButton(navigation_bar, text="", image=drills_icon, bg_color="#00A29E", fg_color="#00A29E")
drills_icon_button.grid(row=0, column=6, sticky="nsew")

previous_plans_button = ctk.CTkButton(navigation_bar, text="Previous Training Plans", font=("ADLaM Display", 15), fg_color="#16CCCC")
previous_plans_button.grid(row=0, column=7)
file_icon= ctk.CTkImage(light_image=Image.open("Images/white file icon.png"), dark_image=Image.open("Images/white file icon.png"), size=(35, 35))
file_icon_button = ctk.CTkButton(navigation_bar, text="", image=file_icon, bg_color="#00A29E", fg_color="#00A29E")
file_icon_button.grid(row=0, column=8, sticky="nsew")

#Right Column Home page buttons/info
right_column = ctk.CTkFrame(app, width=600)
right_column.grid(row=1, column=1, sticky="nsew")
right_column.grid_columnconfigure(0, weight=1)
right_column.grid_columnconfigure(1, weight=1)
right_column.grid_rowconfigure(0, weight=1)
right_column.grid_rowconfigure(1, weight=1)
right_column.grid_rowconfigure(2, weight=1)

import_stats_button = ctk.CTkButton(right_column, text="Import Statistics", font=("ADLaM Display", 25), fg_color="#FF7A53")
import_stats_button.grid(row=0, column=0, padx=10, pady=10)
import_stats_label = ctk.CTkLabel(right_column, text="Click this button to import statistics from Excel, ensuring your template matches the image to the left", font=("Abadi",12), wraplength=300, justify="left")
import_stats_label.grid(row=0, column=1, padx=5, pady=5)

generate_plan_button = ctk.CTkButton(right_column, text="Generate Training Plan", font=("ADLaM Display", 25), height=20, fg_color="#FF7A53")
generate_plan_button.grid(row=1, column=0, padx=10, pady=10)
generate_plan_label = ctk.CTkLabel(right_column, text="Click this button to generate a training plan like the image on the left based on your analysed statistics", font=("Abadi", 12), wraplength=300, justify="left")
generate_plan_label.grid(row=1, column=1, padx=5, pady=5)

new_drill_button = ctk.CTkButton(right_column, text="Add New Drill", font=("ADLaM Display", 25), fg_color="#FF7A53")
new_drill_button.grid(row=2, column=0, padx=10, pady=10)
new_drill_label = ctk.CTkLabel(right_column, text="Click this button to add a new drill to the drills database", font=("Abadi", 12), wraplength=300, justify="left")
new_drill_label.grid(row=2, column=1, padx=5, pady=5)


#Left Column Home page, diagrams for users
left_column = ctk.CTkFrame(app, border_width=2)
left_column.grid(row=1, column=0, sticky="nsew")
left_column.grid_columnconfigure(0, weight=1)
left_column.grid_rowconfigure(0, weight=1)
left_column.grid_rowconfigure(1, weight=1)
left_column.grid_rowconfigure(2, weight=1)

stats_diagram = ctk.CTkImage(light_image=Image.open("Images/Stats image.png"), dark_image=Image.open("Images/Stats image.png"), size=(500,150))
stats_diagram_label = ctk.CTkLabel(left_column, text="", image=stats_diagram)
stats_diagram_label.grid(row=0, column=0, sticky="nsew")

down_arrow = ctk.CTkImage(light_image=Image.open("Images/down arrow.png"), dark_image=Image.open("Images/down arrow.png"), size=(50,50))
down_arrow_label = ctk.CTkLabel(left_column, text="", image=down_arrow)
down_arrow_label.grid(row=1, column=0, sticky="nsew")

plan_diagram = ctk.CTkImage(light_image=Image.open("Images/Plan Diagram.png"), dark_image=Image.open("Images/Plan Diagram.png"), size=(360,350))
plan_diagram_label = ctk.CTkLabel(left_column, text="", image=plan_diagram)
plan_diagram_label.grid(row=2, column=0, sticky="nsew")


app.mainloop()