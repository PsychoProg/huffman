import tkinter as tk

def show_username():
    # Get the username from the entry widget
    username = username_entry.get()
    
    # Update the label with the username
    result_label.config(text="Hello " + username + "!")

# Create the main window
root = tk.Tk()

# Create the username label and entry widgets
username_label = tk.Label(root, text="Enter your username:")
username_entry = tk.Entry(root)

# Create the button widget
submit_button = tk.Button(root, text="Submit", command=show_username)

# Create the result label widget
result_label = tk.Label(root, text="")

# Pack the widgets into the window
username_label.pack()
username_entry.pack()
submit_button.pack()
result_label.pack()

# Start the main event loop
root.mainloop()
