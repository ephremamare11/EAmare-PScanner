from tkinter import messagebox
import nmap
import time

# Function to validate the IP address
def is_valid_ip(ip):
    ip_parts = ip.split('.')
    if len(ip_parts) != 4:
        return False
    for part in ip_parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def get_ip_address(ip, output_text):
    if is_valid_ip(ip):
        messagebox.showinfo("Info", "This is a valid IP address")
        output_text.insert('end', f"{ip} is a valid IP address.\n")
        return ip
    else:
        messagebox.showinfo("Error", "Invalid IP address. Please try again and ensure that there are no spaces before or in between. (Ex. 0-255.0-255.0-255.0-255)")
        output_text.insert('end', f"{ip} is not a valid IP address.\n")
        return None

# Function to validate individual ports and port ranges
def is_valid_port_or_range(port):
    if port.isdigit():
        return 1 <= int(port) <= 65535
    elif '-' in port:
        try:
            start_port, end_port = map(int, port.split('-'))
            return 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port < end_port
        except ValueError:
            return False
    return False

# Function to handle multiple ports/ranges input
def parse_ports_input(port_ranges):
    port_ranges_list = port_ranges.replace(" ", "").split(',')
    valid_ports = []
    for port_range in port_ranges_list:
        if is_valid_port_or_range(port_range):
            valid_ports.append(port_range)
        else:
            return None
    return valid_ports

# Function to handle port scanning
def port_scanner(port_input, e1, tree, output_text):
    target_ip = e1.get()
    if not is_valid_ip(target_ip):
        output_text.insert('end', "Invalid IP address. Please enter a valid IP.\n")
        return

    port_ranges = parse_ports_input(port_input)
    if not port_ranges:
        output_text.insert('end', "Invalid port or range. Please enter valid ports or ranges (Ex. 20, 22-80, 443).\n")
        return

    nm = nmap.PortScanner()
    output_text.insert('end', f'Scanning {target_ip} for ports {port_input}...\n')
    time.sleep(1)

    tree.delete(*tree.get_children())

    try:
        for scan_target in port_ranges:
            nm.scan(target_ip, scan_target)
            if 'tcp' in nm[target_ip]:
                ports_to_be_scanned = [(port, nm[target_ip]['tcp'][port]['state']) for port in nm[target_ip]['tcp']]
                for port, state in ports_to_be_scanned:
                    tree.insert("", "end", values=(port, state))
                    output_text.insert('end', f"Port {port} is {state}\n")
            else:
                output_text.insert('end', f"No open TCP ports found for {scan_target}.\n")
    except Exception as e:
        output_text.insert('end', f"An error occurred: {str(e)}\n")
