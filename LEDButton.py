import tkinter as tk
import http.client
import json

def post_light_status(color, is_on, onoff_id):
    # Define the host and endpoint
    host = "techbutler.tech"
    endpoint = "/ard/Service1.svc/ChangeLightStatus"

    # Data to be sent in the POST request
    data = {
        "color": color,
        "isOn": is_on,
        "onoffID": onoff_id
    }

    # Convert data to JSON
    json_data = json.dumps(data)

    # Create a connection
    conn = http.client.HTTPConnection(host)

    # Define headers
    headers = {
        "Content-Type": "application/json"
    }

    # Send POST request
    conn.request("POST", endpoint, body=json_data, headers=headers)

    # Get the response
    response = conn.getresponse()
    status = response.status
    reason = response.reason
    response_content = response.read().decode()

    # Close the connection
    conn.close()

    # Return response details
    return {
        "status": status,
        "reason": reason,
        "content": response_content
    }

# Example usage:
result = post_light_status("String content", True, 2147483647)
print("Response:", result)

def red_button_click():
    print("Red button clicked")
    post_light_status("red", True, 1)

def green_button_click():
    print("Green button clicked")
    post_light_status("green", True, 1)

def blue_button_click():
    print("Blue button clicked")
    post_light_status("blue", True, 1)

def toggle_on_off():
    if on_off_button.config('text')[-1] == 'Off':
        on_off_button.config(text='On')
        print("Turned On")
        post_light_status("red", True, 1)
    else:
        on_off_button.config(text='Off')
        print("Turned Off")
        post_light_status("red", False, 1)

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

# Create buttons and assign them to the functions, with respective colors
red_button = tk.Button(root, text="Red", command=red_button_click, fg="red", activebackground="black", activeforeground="black", width=20, height=2)
green_button = tk.Button(root, text="Green", command=green_button_click, bg="green", fg="green", activebackground="black", activeforeground="black", width=20, height=2)
blue_button = tk.Button(root, text="Blue", command=blue_button_click, bg="blue", fg="blue", activebackground="black", activeforeground="black", width=20, height=2)

# Pack the buttons into the window
red_button.pack(pady=10)
green_button.pack(pady=10)
blue_button.pack(pady=10)

# Create an On/Off button
on_off_button = tk.Button(root, text="Off", command=toggle_on_off, width=20, height=2)
on_off_button.pack(pady=10)

# Run the application
root.mainloop()
