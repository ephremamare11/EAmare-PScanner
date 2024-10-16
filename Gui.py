import nmap
import time
from tkinter import *
from tkinter import messagebox, ttk, Text, font  # Import font module for custom fonts
from infilvalidation import *  # Import IP and port validation functions

# Welcome message box
def welcome_box():
    try:
        messagebox.showinfo(
            "WELCOME", 
            "Welcome to INFILTR8R!\n\n"
            "For more information on how to use our port scanner, head over to the 'Help' option in the menu.\n\n"
            "Happy Scanning!! :)"
        )
    except Exception as e:
        print(f"Error displaying welcome box: {e}")

# About message box
def show_about():
    messagebox.showinfo(
        "About", 
        "INFILTR8R is a port scanning tool designed to help network administrators and security professionals identify "
        "open ports and potential vulnerabilities.\n\n"
        "Version: 1.2.5\n"
        "Developed by: INFILTR8R Team\n\n"
        "For more information, visit our website or contact support at support@infiltr8r.com."
    )

# Help Desk message box
def show_help_desk():
    messagebox.showinfo(
        "Help Desk", 
        "When inputting an IP address, please use this format (e.g., 0-255.0-255.0-255.0-255).\n\n"
        "For ports, you can use a single port or a range (e.g., 20, 22-80, 443).\n\n"
        "For further assistance, contact support at support@infiltr8r.com."
    )

# Report issue message box
def show_report():
    messagebox.showinfo(
        "Report", 
        "If you encounter any issues, please report them to issues@infiltr8r.com."
    )

# Check for Updates message box
def show_updates():
    messagebox.showinfo(
        "Check for Updates", 
        "You're using the latest version of Infiltr8r.\nVersion: 1.2.5"
    )

# Exit function to close the app properly
def exit_app(root):
    root.destroy()  # Properly close the entire application

# Main GUI function
def start_gui():
    global e1, e2, tree, output_text
    root = Tk()
    root.title('INFILTR8R')

    # Custom Font for the Title
    scanner_font = font.Font(family='Courier', size=14, weight='bold')  # Monospace font resembling a port scanner

    # Welcome Label with Custom Font
    w = Label(root, text='WELCOME TO INFILTR8R', font=scanner_font)
    w.grid(row=0, column=0, columnspan=2)

    # Navigation Menu
    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Save as')
    filemenu.add_command(label='Mail to')
    filemenu.add_command(label='Export')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=lambda: exit_app(root))  # Exit button calls exit_app function

    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About', command=show_about)
    helpmenu.add_command(label='Help Desk', command=show_help_desk)
    helpmenu.add_command(label='Report', command=show_report)
    helpmenu.add_command(label='Check for updates', command=show_updates)

    # IP Address Input
    Label(root, text='IP Address').grid(row=2, column=0)
    e1 = Entry(root)
    e1.grid(row=2, column=1)

    submit_ip = Button(root, text='Validate', command=lambda: get_ip_address(e1.get(), output_text))
    submit_ip.grid(row=2, column=4)

    # Port Range Input
    Label(root, text='Ports').grid(row=4, column=0)
    e2 = Entry(root)
    e2.grid(row=4, column=1)

    submit_port = Button(root, text='Scan', command=lambda: port_scanner(e2.get(), e1, tree, output_text))
    submit_port.grid(row=4, column=4)

    # Treeview for displaying scan results
    tree = ttk.Treeview(root, columns=("Port", "State"), show='headings')
    tree.heading("Port", text="Port")
    tree.heading("State", text="State")
    tree.grid(row=5, column=0, columnspan=3)

    # Output Text Area for messages
    output_text = Text(root, height=10, width=50)
    output_text.grid(row=6, column=0, columnspan=3)

    # Display Welcome Message Box
    welcome_box()

    # Start the GUI event loop
    root.mainloop()

# Run the GUI if this script is the main program
if __name__ == "__main__":
    start_gui()
