'''Stats2Drills GUI Application. date started: 23/06/2025'''

import customtkinter as ctk

app = ctk.CTk()
app.title("Stats2Drills GUI Interface")
app.geometry("1250x700")

#Configure main grid
app.grid_columnconfigure(0, weight=1) #Left column
app.grid_columnconfigure(1, weight=1) #Right column
app.grid_rowconfigure(0, weight=1)  #Top navigation bar
app.grid_rowconfigure(1, weight=1)  
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=1)

#Top Navigation bar
navigation_bar = ctk.CTkFrame(app, border_width=3)
navigation_bar.grid(row=0, column=0, columnspan=2)
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

title_label = ctk.CTkLabel(navigation_bar, text="Stats2Drills", font=("ADLaM Display", 30))
title_label.grid(row=0, column=1, columnspan=2)

home_button = ctk.CTkButton(navigation_bar, text="Home", font=("ADLaM Display", 15), fg_color="#16CCCC", height=35)
home_button.grid(row=0, column=3)
home_icon = 

drills_button = ctk.CTkButton(navigation_bar, text="Drills", font=("ADLaM Display", 15), fg_color="#16CCCC")
drills_button.grid(row=0, column=5)

previous_plans_button = ctk.CTkButton(navigation_bar, text="Previous Training Plans", font=("ADLaM Display", 15), fg_color="#16CCCC")
previous_plans_button.grid(row=0, column=7)

app.mainloop()