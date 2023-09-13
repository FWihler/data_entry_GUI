import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()
    
    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            print("First name:", firstname, "Last name:", lastname)
            print("Age:", age, "Nationality:", nationality)
            print("------------------------------------------")
            
            # Create Table
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data 
                    (firstname TEXT, lastname TEXT, age INT, nationality TEXT)
            '''
            conn.execute(table_create_query)
            
            # Insert Data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, age, nationality)
            VALUES (?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, age, nationality)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")
window.geometry("400x300")  # Set window dimensions

# Improve GUI design with fonts and colors
window.configure(bg="#f2f2f2")  # Set background color
window.option_add("*TButton*highlightBackground", "#f2f2f2")  # Remove button border
window.option_add("*TButton*highlightColor", "#f2f2f2")  # Remove button border
window.option_add("*TButton*selectBackground", "#ff6600")  # Button click color

frame = tkinter.Frame(window, bg="#ffffff")  # Set frame background color
frame.pack(expand=True, fill="both")

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information", bg="#ffffff", font=("Arial", 12))
user_info_frame.pack(padx=20, pady=10, expand=True, fill="both")

first_name_label = tkinter.Label(user_info_frame, text="First Name", bg="#ffffff", font=("Arial", 10))
first_name_label.grid(row=0, column=0, pady=5)
last_name_label = tkinter.Label(user_info_frame, text="Last Name", bg="#ffffff", font=("Arial", 10))
last_name_label.grid(row=0, column=1, pady=5)

first_name_entry = tkinter.Entry(user_info_frame, font=("Arial", 10))
last_name_entry = tkinter.Entry(user_info_frame, font=("Arial", 10))
first_name_entry.grid(row=1, column=0, pady=5)
last_name_entry.grid(row=1, column=1, pady=5)

age_label = tkinter.Label(user_info_frame, text="Age", bg="#ffffff", font=("Arial", 10))
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110, font=("Arial", 10))
age_label.grid(row=2, column=0, pady=5)
age_spinbox.grid(row=3, column=0, pady=5)

nationality_label = tkinter.Label(user_info_frame, text="Nationality", bg="#ffffff", font=("Arial", 10))
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"], font=("Arial", 10))
nationality_label.grid(row=2, column=1, pady=5)
nationality_combobox.grid(row=3, column=1, pady=5)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions", bg="#ffffff", font=("Arial", 12))
terms_frame.pack(padx=20, pady=10, expand=True, fill="both")

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", bg="#ffffff", font=("Arial", 10))
terms_check.grid(row=0, column=0, pady=5)

# Button
button = ttk.Button(frame, text="Enter data", command=enter_data, style="TButton")
button.pack(expand=True, pady=10)

# Create a style for the button
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), foreground="#ffffff", background="#ff6600")

window.mainloop()
