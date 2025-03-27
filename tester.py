import tkinter as tk
import customtkinter as ctk
import string
import math
import time
from tkinter import messagebox
import os

# Function to display banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  Password-Tester
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Show banner at script startup
show_banner()

# Ask user for input
choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()

if choice == 'n':
    print("\nExiting the script. Goodbye!")
    exit()
elif choice == 'y':
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen on Linux/Mac ('clear') or Windows ('cls')
else:
    print("\nInvalid choice. Exiting the script.")
    exit()

def logo():
    logo_text = r"""

████████╗███████╗███████╗████████╗███████╗██████╗ 
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
   ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
   ██║   ███████╗███████║   ██║   ███████╗██║  ██║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                    
"""
    print(logo_text)
    return logo_text

# Function to calculate password strength
def calculate_strength(password):
    length_score = min(len(password) / 16, 1)  # Max score for length is 1
    variety_score = sum(any(c in password for c in cat) for cat in [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]) / 4
    
    entropy = math.log2(len(set(password)) ** len(password)) if password else 0
    
    score = (length_score + variety_score) / 2  # Weighted score
    
    return score, entropy

# Function to check password strength and update UI
def check_password():
    password = entry.get()
    score, entropy = calculate_strength(password)
    
    if score < 0.3:
        status.configure(text="Weak", fg_color=("#ff4d4d", "#660000"))
    elif score < 0.7:
        status.configure(text="Medium", fg_color=("#ffcc00", "#665500"))
    else:
        status.configure(text="Strong", fg_color=("#33cc33", "#003300"))
    
    entropy_label.configure(text=f"Entropy: {entropy:.2f} bits")
    
    # Animation effect
    for i in range(3):
        root.update()
        time.sleep(0.1)
        status.configure(fg_color=("#ffffff", "#000000"))
        root.update()
        time.sleep(0.1)
        status.configure(fg_color=("#ff4d4d" if score < 0.3 else "#ffcc00" if score < 0.7 else "#33cc33"))

# GUI Setup
root = ctk.CTk()
root.title("Password Tester")
root.geometry("400x350")
ctk.set_appearance_mode("dark")

logo()

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

logo_label = ctk.CTkLabel(frame, text=logo(), font=("Courier", 10), justify="center")
logo_label.pack(pady=10)

label = ctk.CTkLabel(frame, text="Enter Password:", font=("Arial", 14))
label.pack(pady=5)

entry = ctk.CTkEntry(frame, show="*", width=250)
entry.pack(pady=5)

button = ctk.CTkButton(frame, text="Check Strength", command=check_password)
button.pack(pady=10)

status = ctk.CTkLabel(frame, text="", font=("Arial", 16, "bold"), width=100)
status.pack(pady=5)

entropy_label = ctk.CTkLabel(frame, text="", font=("Arial", 12))
entropy_label.pack(pady=5)

root.mainloop()
