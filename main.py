import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Function to run Flappy Bird game
def run_flappybird():
    current_directory = os.getcwd()
    script1_path = os.path.join(current_directory, "flappybird.py")
    os.system("python " + script1_path)

# Function to run Space Invaders game
def run_space_invaders():
    current_directory = os.getcwd()
    script2_path = os.path.join(current_directory, "space_inavader.py")
    os.system("python " + script2_path)

# Function to run Tic-Tac-Toe game
def run_tictactoe():
    current_directory = os.getcwd()
    script3_path = os.path.join(current_directory, "tic.py")
    os.system("python " + script3_path)

# Function to run car game
def run_car_game():
    current_directory = os.getcwd()
    script4_path = os.path.join(current_directory, "car_game.py")
    os.system("python " + script4_path)

def main():
    # Create main window
    window = tk.Tk()
    window.title("Game Launcher")
    window.geometry("800x600")
    window.configure(bg="#316178")  # Background color

    # Create a style for buttons
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12), foreground="white", background="#316178")

    # Label for instructions: Enter your name
    name_lbl = tk.Label(window, text="\n\n\n\n\nEnter your name:", font=("Arial", 30,"bold"), bg="#316178")
    name_lbl.pack(pady=20)

    # Entry widget for name input
    entry = tk.Entry(window, width=30, font=("Arial", 20))
    entry.pack()
    entry.config(bg="#D6e6f2")
    # Label for instructions: Enter your Age
    age_lbl = tk.Label(window, text="Enter your Age:", font=("Arial", 30,"bold"), bg="#316178")
    age_lbl.pack(pady=20)

    # Entry widget for age input
    entry_age = tk.Entry(window, width=30, font=("Arial", 20))
    entry_age.pack()
    entry_age.config(bg="#D6e6f2")

    # Function to display greeting message and game buttons
    def display_hello():

        # Hide name and age labels
        name_lbl.pack_forget()
        age_lbl.pack_forget()
        entry.pack_forget()
        entry_age.pack_forget()
        submit_button.pack_forget()


        name = entry.get()
        age = entry_age.get()

        # Display message with name and age
        hello_label.config(text="\n\n\n\nHello " + name + "!\nSelect a game to play:\n\n", font=("Arial", 30,"bold"), bg="#316178",fg="white")

        # Create image buttons with game commands
        button_images = {
            "flappybird": "flappybird.jpg",
            "space_invaders": "space_invaders.jpg",
            "ttt": "tictactoe.jpg",
            "car" : "car_logo.jpg"
        }

        # Create buttons for each game
        button_frame = tk.Frame(window, bg="#316178")
        button_frame.pack(pady=10)

        for game, image_file in button_images.items():
            # Load and resize the image
            img = Image.open(image_file)
            img = img.resize((300, 175))  # Resize image to 200x100
            img = ImageTk.PhotoImage(img)

            # Create button with image and command
            button = ttk.Button(button_frame, image=img, command=lambda g=game: game_command(g), style="TButton")
            button.image = img  # Keep a reference to the image
            button.pack(side="left", padx=30)  # Pack buttons side by side
    
    # Button to submit name and age
    submit_button = tk.Button(window, text="Submit", command=display_hello, width=10, height=1, bg="#180e0a", fg="white", font=("Arial", 20))
    submit_button.pack(pady=30)

    # Label to display the greeting message
    hello_label = tk.Label(window, text="", font=("Arial", 20), bg="#316178")
    hello_label.pack()

    # Function to execute the corresponding game function based on button click
    def game_command(game):
        if game == "flappybird":
            run_flappybird()
        elif game == "space_invaders":
            run_space_invaders()
        elif game == "ttt":
            run_tictactoe()
        elif game == "car":
            run_car_game()    

    window.mainloop()

if __name__ == "__main__":
    main()
