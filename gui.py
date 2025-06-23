'''Space for internal documentation of entire code purpose date started: 23/06/2025'''

import customtkinter

app = customtkinter.CTk()
app.title("Stats2Drills GUI Interface")
app.geometry("1250x700")

button = customtkinter.CTkButton(app, text="my button")
button.grid(row=2, column=4, padx=20, pady=20, sticky="ew", columnspan=2)


app.mainloop()