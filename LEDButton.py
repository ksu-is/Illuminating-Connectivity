import tkinter as tk

def button1_click():
    print("Button 1 clicked")

def button2_click():
    print("Button 2 clicked")

def button3_click():
    print("Button 3 clicked")

# Create the main window
root = tk.Tk()
root.title("Three Buttons")

# Create buttons and assign them to the functions
button1 = tk.Button(root, text="Button 1", command=button1_click)
button2 = tk.Button(root, text="Button 2", command=button2_click)
button3 = tk.Button(root, text="Button 3", command=button3_click)

# Pack the buttons into the window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Run the application
root.mainloop()
