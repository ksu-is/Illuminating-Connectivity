import tkinter as tk

def button1_click():
    print("Button 1 clicked")

def button2_click():
    print("Button 2 clicked")

def button3_click():
    print("Button 3 clicked")

def toggle_on_off():
    if on_off_button.config('text')[-1] == 'Off':
        on_off_button.config(text='On')
        print("Turned On")
    else:
        on_off_button.config(text='Off')
        print("Turned Off")

# Create the main window
root = tk.Tk()
root.title("Three Buttons")

# Set the window size
window_width = 300
window_height = 300

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position for the window to be centered
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window
root.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

# Create a header label
header = tk.Label(root, text="Illuminating Connectivity", font=("Arial", 16))
header.pack(pady=10)

# Create buttons and assign them to the functions
button1 = tk.Button(root, text="Button 1", command=button1_click)
button2 = tk.Button(root, text="Button 2", command=button2_click)
button3 = tk.Button(root, text="Button 3", command=button3_click)

# Pack the buttons into the window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Create an On/Off button
on_off_button = tk.Button(root, text="Off", command=toggle_on_off)
on_off_button.pack(pady=10)

# Run the application
root.mainloop()
