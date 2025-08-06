import customtkinter as ctk
from PIL import Image

class Home_page(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller

#Home Page content
        #Configure main grid
        self.grid_columnconfigure(0, weight=1) #Left column
        self.grid_columnconfigure(1, weight=1) #Right column
        self.grid_rowconfigure(0, weight=0)  #Top navigation bar
        self.grid_rowconfigure(1, weight=1)  #Main page content

        #Navigation bar
        navigation_bar = ctk.CTkFrame(self, height=35, bg_color="#00A29E", fg_color="#00A29E")
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

        home_button = ctk.CTkButton(navigation_bar, width=120, height=40, text="Home", font=("ADLaM Display", 20), text_color="light grey", border_width=2, border_color="light grey", fg_color="#16CCCC", hover_color="#00A29E")
        home_button.grid(row=0, column=3, sticky="e")
        home_icon= ctk.CTkImage(light_image=Image.open("Images/grey home icon.png"), dark_image=Image.open("Images/grey home icon.png"), size=(35, 35))
        home_icon_button = ctk.CTkButton(navigation_bar, text="", image=home_icon, bg_color="#00A29E", fg_color="#00A29E", height=30, width=35, hover_color="#00A29E")
        home_icon_button.grid(row=0, column=4, sticky="w")
        #Configure buttons to raise home page
        home_button.configure(command=lambda: self.show_frame("Home_page"))
        home_icon_button.configure(command=lambda: self.show_frame("Home_page"))

        drills_button = ctk.CTkButton(navigation_bar, height=40, text="Drills", font=("ADLaM Display", 20), text_color="white", border_width=2, border_color="white", fg_color="#16CCCC", hover_color="#c7c7c7")
        drills_button.grid(row=0, column=5, sticky="e")
        drills_icon= ctk.CTkImage(light_image=Image.open("Images/white drills icon.png"), dark_image=Image.open("Images/white drills icon.png"), size=(35, 35))
        drills_icon_button = ctk.CTkButton(navigation_bar, text="", image=drills_icon, bg_color="#00A29E", fg_color="#00A29E",  height=30, width=35, hover_color="#c7c7c7")
        drills_icon_button.grid(row=0, column=6, sticky="w")
        #Configure buttons to raise the drills page
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

        #Main content of Home page
    
        #Right Column Home page buttons/description
        right_column = ctk.CTkFrame(self, width=600, bg_color="#F2F2F2", fg_color="#F2F2F2")
        right_column.grid(row=1, column=1, sticky="nsew")
        right_column.grid_columnconfigure(0, weight=1)
        right_column.grid_columnconfigure(1, weight=1)
        right_column.grid_rowconfigure(0, weight=1)
        right_column.grid_rowconfigure(1, weight=1)
        right_column.grid_rowconfigure(2, weight=1)

        graph_icon = ctk.CTkImage(light_image=Image.open("Images/graph icon.png"), dark_image=Image.open("Images/graph icon.png"), size=(30, 30))
        import_stats_button = ctk.CTkButton(right_column, corner_radius=10, text="Import Statistics     ", text_color="white", height=50, font=("ADLaM Display", 25), image=graph_icon, compound="right", fg_color="#FF7A53", hover_color="#c7c7c7")
        import_stats_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        import_stats_label = ctk.CTkLabel(right_column, text="Click this button to be directed to statistics page where you can import and analyse your statistics from Excel, ensuring your template matches the image to the left", font=("Abadi",15), wraplength=300, justify="left")
        import_stats_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        #Configure button to display stats page and load stats from excel
        import_stats_button.configure(command=lambda: self.show_frame("Stats_page"))
    
        generate_plan_button = ctk.CTkButton(right_column, corner_radius=10, text="Generate Training \nPlan", font=("ADLaM Display", 25), text_color="white", image=file_icon, fg_color="#FF7A53", compound="right", hover_color="#c7c7c7", command=lambda: self.show_frame("Stats_page"))
        generate_plan_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        generate_plan_label = ctk.CTkLabel(right_column, text="Click this button to generate a training plan, which once converted to a pdf will look like the image on the left", font=("Abadi", 15), wraplength=300, justify="left")
        generate_plan_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        new_drill_button = ctk.CTkButton(right_column, corner_radius=10, text="Add New Drill     ", font=("ADLaM Display", 25), text_color="white", height=50, fg_color="#FF7A53", image=drills_icon, compound="right", hover_color="#c7c7c7", command=lambda: self.show_frame("Drills_page"))
        new_drill_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        new_drill_label = ctk.CTkLabel(right_column, text="Click this button to add a new drill to the drills database", font=("Abadi", 15), wraplength=300, justify="left")
        new_drill_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")


        #Left Column Home page, diagrams for users
        left_column = ctk.CTkFrame(self, border_width=2, corner_radius=0, border_color="#7F7F7F", bg_color="#F2F2F2", fg_color="#F2F2F2")
        left_column.grid(row=1, column=0, sticky="nsew")
        left_column.grid_columnconfigure(0, weight=1)
        left_column.grid_rowconfigure(0, weight=1)
        left_column.grid_rowconfigure(1, weight=1)
        left_column.grid_rowconfigure(2, weight=1)

        stats_diagram = ctk.CTkImage(light_image=Image.open("Images/Stats image.png"), dark_image=Image.open("Images/Stats image.png"), size=(500,150))
        stats_diagram_label = ctk.CTkLabel(left_column, text="", image=stats_diagram, bg_color="#F2F2F2", fg_color="#F2F2F2")
        stats_diagram_label.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")

        down_arrow = ctk.CTkImage(light_image=Image.open("Images/down arrow.png"), dark_image=Image.open("Images/down arrow.png"), size=(45,45))
        down_arrow_label = ctk.CTkLabel(left_column, text="", image=down_arrow, bg_color="#F2F2F2", fg_color="#F2F2F2")
        down_arrow_label.grid(row=1, column=0, padx=3, pady=3, sticky="nsew")

        plan_diagram = ctk.CTkImage(light_image=Image.open("Images/Plan Diagram.png"), dark_image=Image.open("Images/Plan Diagram.png"), size=(370,350))
        plan_diagram_label = ctk.CTkLabel(left_column, text="", image=plan_diagram, bg_color="#F2F2F2", fg_color="#F2F2F2")
        plan_diagram_label.grid(row=2, column=0, padx=3, pady=3, sticky="nsew")