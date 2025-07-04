'''Stats2Drills GUI Application. date started: 23/06/2025'''

import customtkinter as ctk
from PIL import Image
from home_page import Home_page
from drills_page import Drills_page
from previous_plans_page import Previous_plans_page

app = ctk.CTk(fg_color="#F2F2F2")
app.title("Stats2Drills GUI Interface")
app.geometry("1250x700")
 
app.grid_columnconfigure(0, weight=1) #Single column
app.grid_rowconfigure(0, weight=1)  #Single row 

container = ctk.CTkFrame(app)
container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
container.grid_rowconfigure(0, weight=1) # single row
container.grid_columnconfigure(0, weight=1) # single column

#Page-switching function
def show_frame(page_name):
    pages[page_name].tkraise()

#Load Home_page class
home_page = Home_page(container, controller=show_frame)
home_page.grid(row=0, column=0, sticky="nsew")

#Load Drills_page class
drills_page = Drills_page(container, controller=show_frame)
drills_page.grid(row=0, column=0, sticky="nsew")

#Load Previous_plans_page
previous_plans_page = Previous_plans_page(container, controller=show_frame)
previous_plans_page.grid(row=0, column=0, sticky="nsew")

#Dictionary of pages
pages = {
    "Home_page": home_page,
    "Drills_page": drills_page,
    "Previous_plans_page": previous_plans_page
}

# Initially show Home Page
show_frame("Home_page")


app.mainloop()