import tkinter as tk
from tkinter import messagebox

# Function to check if there's a winner
def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show message box announcing the winner
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

# Function for button click events
def button_click(index):
    if buttons[index]["text"] == "" and not winner[0]:  
        buttons[index]["text"] = current_player[0]
        check_winner()
        toggle_player()

# Function to toggle between players
def toggle_player():
    current_player[0] = "X" if current_player[0] == "O" else "O"
    label.config(text=f"Player {current_player[0]}'s turn")

# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create and place buttons on the grid
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, 
                     command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initialize game state variables
current_player = ["X"]
winner = [False]  

# Add a label to show the current player's turn
label = tk.Label(root, text=f"Player {current_player[0]}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Run the Tkinter main loop
root.mainloop()
