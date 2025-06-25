'''Stats2Drills GUI Application. date started: 23/06/2025'''

import customtkinter as ctk
import pyglet,ctk
pyglet.font.add_file('ADLaMDisplay-Regular.ttf')

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
navigation_bar.grid(row=0, column=0, columnspan=9, sticky="nsew")
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

title_label = ctk.CTkLabel(navigation_bar, text="Stats2Drills", font="ADLaMDisplay-Regular", text_color="White")
title_label.grid(row=0, column=1, columnspan=2)

home_button = ctk.CTkButton(navigation_bar, text="Home", font=("ADLaM Display", 15), fg_color="#16CCCC")
home_button.grid(row=0, column=3)


drills_button = ctk.CTkButton(navigation_bar, text="Drills", font=("ADLaM Display", 15), fg_color="#16CCCC")
drills_button.grid(row=0, column=5)

previous_plans_button = ctk.CTkButton(navigation_bar, text="Previous Training Plans", font=("ADLaM Display", 15), fg_color="#16CCCC")
previous_plans_button.grid(row=0, column=7)


#Right Column Home page buttons/info
right_column = ctk.CTkFrame(app)
right_column.grid(row=1, column=1)
right_column.grid_columnconfigure(0, weight=1)
right_column.grid_columnconfigure(1, weight=1)
right_column.grid_rowconfigure(0, weight=1)
right_column.grid_rowconfigure(1, weight=1)
right_column.grid_rowconfigure(2, weight=1)

import_stats_button = ctk.CTkButton(right_column, text="Import Statistics", font=("", 15), fg_color="#FF7A53")
import_stats_button.grid(row=0, column=0, padx=10, pady=10)
import_stats_label = ctk.CTkLabel(right_column, text="Click this button to import statistics from Excel, ensuring your template matches the image to the left", font=("",12))
import_stats_label.grid(row=0, column=1, padx=5, pady=5)

generate_plan_button = ctk.CTkButton(right_column, text="Generate Training Plan", font=("", 15), fg_color="#FF7A53")
generate_plan_button.grid(row=1, column=0, padx=10, pady=10)
generate_plan_label = ctk.CTkLabel(right_column, text="Click this button to generate a training plan like the image on the left based on your analysed statistics", font=("", 12))
generate_plan_label.grid(row=1, column=1, padx=5, pady=5)

new_drill_button = ctk.CTkButton(right_column, text="Add New Drill", font=("", 15), fg_color="#FF7A53")
new_drill_button.grid(row=2, column=0, padx=10, pady=10)
new_drill_label = ctk.CTkLabel(right_column, text="Click this button to add a new drill to the drills database", font=("", 12))
new_drill_label.grid(row=2, column=1, padx=5, pady=5)


#Left Column Home page, diagrams for users
left_column = ctk.CTkFrame(app)
left_column.grid(row=1, column=0)
left_column.grid_columnconfigure(0, weight=1)
left_column.grid_rowconfigure(0, weight=1)
left_column.grid_rowconfigure(1, weight=1)
left_column.grid_rowconfigure(2, weight=1)

app.mainloop()