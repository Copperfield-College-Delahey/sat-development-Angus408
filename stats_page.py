import customtkinter as ctk
from CTkTable import *
from customtkinter import filedialog
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image


class Stats_page(ctk.CTkFrame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.show_frame = controller
         #Function to get and analyse stats, displaying analysis in table
        def analyse_stats():
            #Opens filediolog in same direcotry and allows only xlsx file types
            file_name = filedialog.askopenfilename(initialdir="C:\\Software Development\\SAT Project\\sat-development-Angus408", title="Open an Excel file", filetypes=[("xlsx files", "*.xlsx")])

            if file_name:
                #validates that the file is correct and has been found, displaying relevant error messages if not.
                try:
                    #Uses read_excel to get selected file and assign it to dataframe
                    file_name = r"{}".format(file_name)
                    data_frame = pd.read_excel(file_name)
                except ValueError:
                    messagebox.showerror("Error", "File could not be opened. Please import an excel file")
                except FileNotFoundError:
                    messagebox.showerror("Error", "File was not found. Please try again")

                #Validates that all required columns (given by list) are present, displaying an error message if not
                required_columns = ["Total FGM", "Total FGA", "FTM", "FTA", "O - Boards", "D - Boards", "Assists", "Steals", "Blocks", "Turnovers", "Fouls"]
                if not all(col in data_frame.columns for col in required_columns):
                    messagebox.showerror("Error", "Please import statistics which match the template on the home screen, including correct headings")

                
                #List of analysis to be added into table. Placed here means old data will be cleared
                analysis = [["Focuses","Ammount"]]   #Header row

                #Calculates Total Field Goal percentage and appends list with analysis on focus and amount of drills
                total_FGP = data_frame["Total FGM"].sum()/data_frame["Total FGA"].sum()*100
                if total_FGP < 30:
                    analysis.append(["Shooting & Offence", "x3"])
                elif total_FGP < 50:
                    analysis.append(["Shooting & Offence", "x2"])
                else:
                    analysis.append(["Shooting", "x1"])

                #Calculates Total Free Throw percentage and appends list with analysis on focus and amount of drills    
                total_FTP = data_frame["FTM"].sum()/data_frame["FTA"].sum()*100
                if total_FTP < 50:
                    analysis.append(["Freethrows", "x2"])
                else:
                    analysis.append(["Freethrows", "x1"])

                #Calculates total rebounds and appends list with analysis on focus and amount of drills
                rebounds = data_frame["O - Boards"].sum()+data_frame["D - Boards"].sum()
                if rebounds < 10:
                    analysis.append(["Rebounding & Defence", "x2"])
                else:
                    analysis.append(["Rebounnding", "x1"])

                #Calculates total assists and appends list with analysis on focus and amount of drills
                assists = data_frame["Assists"].sum()
                if assists < 10:
                    analysis.append(["Passing & Offence", "x2"])
                else:
                    analysis.append(["Offence", "x1"])

                #Calculates total steals and appends list with analysis on focus and amount of drills
                steals = data_frame["Steals"].sum()
                if steals < 8:
                    analysis.append(["Defence", "x2"])
                else:
                    analysis.append(["Defence", "x1"])

                #Calculates total blocks and appends list with analysis on focus and amount of drills
                blocks = data_frame["Blocks"].sum()
                if blocks < 2:
                    analysis.append(["Defence", "x1"])

                #Calculates total turnovers and appends list with analysis on focus and amount of drills
                turnovers = data_frame["Turnovers"].sum()
                if turnovers > 10:
                    analysis.append(["Dribbling & Passing", "x2"])
                else:
                    analysis.append(["Dribbling & Passing", "x1"])
                
                #Calculates total fouls and appends list with analysis on focus and amount of drills
                fouls = data_frame["Fouls"].sum()
                if fouls > 10:
                    analysis.append(["Defence", "x2"])
                else:
                    analysis.append(["Defence", "x1"])

                #Table to display analysed stats
                stats_analysis = CTkTable(master=right_column, row=len(analysis), column=2, values=analysis, corner_radius=1, header_color="#b0b0b0", colors=["#dbdbdb","#dbdbdb"], border_width=1, border_color="#7a7878", font=("Abadi", 20), text_color="Black")
                stats_analysis.grid(row=0, column=0, pady=15, padx=15, sticky="nsew")

                messagebox.showinfo("Success", "Statistics have been Analysed!")


        #Stats Page content
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


        #Left Column, contains buttons and entry box
        left_column = ctk.CTkFrame(self, width=650, bg_color="#F2F2F2", fg_color="#F2F2F2")
        left_column.grid(row=1, column=0, sticky="nsew")
        left_column.grid_columnconfigure(0, weight=1)
        left_column.grid_rowconfigure(0, weight=1)
        left_column.grid_rowconfigure(1, weight=0)
        left_column.grid_rowconfigure(2, weight=0)
        left_column.grid_rowconfigure(3, weight=0)
        left_column.grid_rowconfigure(4, weight=1)

        analyse_stats_button = ctk.CTkButton(left_column, height=50, corner_radius=10, text="Select & Analyse \nStatistics", font=("ADLaM Display", 25), text_color="white", fg_color="#FF7A53", hover_color="#c7c7c7", command=analyse_stats)
        analyse_stats_button.grid(row=0, column=0, pady=10, padx=10)

        instruction_label = ctk.CTkLabel(left_column, text="Enter Team Age", font=("Abadi", 16), text_color="Black")
        instruction_label.grid(row=1, column=0, padx=10, pady=2, sticky="s")
        team_age_entry = ctk.CTkEntry(left_column, corner_radius=0)
        team_age_entry.grid(row=2, column=0, pady=5)
        age_description_label = ctk.CTkLabel(left_column, text="Must be either U8s, U10s, U12s, U14s, U16s, U18s or U20s", font=("Abadi", 14), text_color="Black", wraplength=150, justify="center")
        age_description_label.grid(row=3, column=0, pady=2, sticky="n")

        generate_plan_button = ctk.CTkButton(left_column, height=60, corner_radius=10, text="Generate Training \nPlan", font=("ADLaM Display", 25), text_color="white", fg_color="#FF7A53", hover_color="#c7c7c7")
        generate_plan_button.grid(row=4, column=0, pady=2, padx=10)        


        #Right Column, display analysed stats in table
        right_column = ctk.CTkFrame(self, width=600, bg_color="#F2F2F2", fg_color="#F2F2F2")
        right_column.grid(row=1, column=1, sticky="nsew")
        right_column.grid_columnconfigure(0, weight=1)
        right_column.grid_rowconfigure(0, weight=1)
