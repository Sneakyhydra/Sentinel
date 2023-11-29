import tkinter as tk
from tkinter import ttk
import json

f = open('command_data.json')
data = json.load(f)
f.close()

def add_command():
    command_name = command_name_entry.get()
    todo = todo_entry.get()
    command_type = command_type_entry.get()
    
    if command_type != "urls" or command_type != "app":
        command_type_entry.delete(0, tk.END)
        display_command_data()
        return

     # Check if command name and todo are not empty
    if command_name and todo:
        # Add command and URL to the data list
        data[command_type][command_name] = todo
        
        # Serializing json
        json_object = json.dumps(data, indent=4)
        
        # Writing to sample.json
        with open("command_data.json", "w") as outfile:
            outfile.write(json_object)

        # Clear the input fields after adding the command
        command_name_entry.delete(0, tk.END)
        todo_entry.delete(0, tk.END)
        command_type_entry.delete(0, tk.END)
        
    # Update the displayed command data
    display_command_data()

def remove_command():
    selected_itm = command_listbox.get(command_listbox.curselection())
    for i in range(len(selected_itm)):
        if(selected_itm[i]==':'):
            selected_itm = selected_itm[:i]
            break

    try:
        data["urls"].pop(selected_itm)
    except Exception as e:
        pass

    try:
        data["app"].pop(selected_itm)
    except Exception as e:
        pass
   
    # Serializing json
    json_object = json.dumps(data, indent=4)
    
    # Writing to sample.json
    with open("command_data.json", "w") as outfile:
        outfile.write(json_object)
            
    # Update the displayed command data
    display_command_data()

def display_command_data():
    command_listbox.delete(0, tk.END)
    for urls in data["urls"]:
        command_listbox.insert(tk.END, f"{urls}: {data['urls'][urls]}")
    for app in data["app"]:
        command_listbox.insert(tk.END, f"{app}: {data['app'][app]}")

    selected_idx = command_listbox.curselection()
    if selected_idx:
        remove_command_button.config(state=tk.NORMAL)
    else:
        remove_command_button.config(state=tk.DISABLED)       

def on_selection(event):
    # Update the state of the "Remove Command" button when a command is selected
    selected_idx = command_listbox.curselection()
    if selected_idx:
        remove_command_button.config(state=tk.NORMAL)
    else:
        remove_command_button.config(state=tk.DISABLED)

    selected_idx = command_listbox.curselection()
    if selected_idx:
        add_command_button.config(state=tk.DISABLED)
    else:
        add_command_button.config(state=tk.NORMAL)

    add_command_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Commands")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y positions to center the window
x = (screen_width - 400) // 2
y = (screen_height - 370) // 2

# Set the window position
window.geometry(f"400x400+{x}+{y}")

window.resizable(False,False)

# Create a style for the labels
label_style = ttk.Style()
label_style.configure("TLabel", font=("Arial", 12))

# Create a custom style for the entry field
entry_style = ttk.Style()
entry_style.configure("Custom.TEntry",
                      fieldbackground="#E0E0E0",
                      font=("Arial", 12))

# Create the "URL" label and text box
command_type_label = ttk.Label(window, text="Command Type(urls/app):", style="TLabel")
command_type_label.grid(row=2, column=0, padx=5, pady=10)

command_type_entry = ttk.Entry(window, style="Custom.TEntry")
command_type_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the "Command Name" label and text box
command_name_label = ttk.Label(window, text="Command Name:", style="TLabel")
command_name_label.grid(row=0, column=0, padx=5, pady=10)

command_name_entry = ttk.Entry(window, style="Custom.TEntry")
command_name_entry.grid(row=0, column=1, padx=5, pady=10)

# Create the "URL" label and text box
todo_label = ttk.Label(window, text="Todo(url/path):", style="TLabel")
todo_label.grid(row=1, column=0, padx=5, pady=10)

todo_entry = ttk.Entry(window, style="Custom.TEntry")
todo_entry.grid(row=1, column=1, padx=5, pady=10)


# Create a frame to display the entered command data
command_data_frame = ttk.Frame(window)
command_data_frame.grid(row=4, columnspan=2, padx=5, pady=20)

# Create a listbox to display the command data
command_listbox = tk.Listbox(command_data_frame, width=60, height=10)
command_listbox.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Create a scrollbar for the command listbox
command_scrollbar = tk.Scrollbar(command_data_frame, orient=tk.VERTICAL)
command_scrollbar.config(command=command_listbox.yview)
command_scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)

# Set the scrollbar for the command listbox
command_listbox.config(yscrollcommand=command_scrollbar.set)

# Bind the selection event to the listbox
command_listbox.bind("<<ListboxSelect>>", on_selection)

# Create the "Add Command" button
add_command_button = ttk.Button(window, text="Add Command", command=add_command)
add_command_button.grid(row=5, column=1, padx=(0, 20), pady=10, sticky=tk.E)

# Create the "Remove Command" button
remove_command_button = ttk.Button(window, text="Remove Command", command=remove_command)
remove_command_button.grid(row=5, column=0, padx=(20, 0), pady=10, sticky=tk.W)

# Display the initial command data
display_command_data()

# Run the main event loop
window.mainloop()
