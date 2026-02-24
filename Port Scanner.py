import socket
import threading
import time
import customtkinter


common_ports = {
    20: "FTP-data (TCP)",
    21: "FTP (TCP)",
    22: "SSH (TCP)",
    23: "Telnet (TCP)",
    25: "SMTP (TCP)",
    53: "DNS (TCP/UDP)",
    67: "DHCP Server (UDP)",
    68: "DHCP Client (UDP)",
    69: "TFTP (UDP)",
    80: "HTTP (TCP)",
    110: "POP3 (TCP)",
    123: "NTP (UDP)",
    137: "NetBIOS Name Service (UDP)",
    138: "NetBIOS Datagram Service (UDP)",
    139: "NetBIOS Session Service (TCP)",
    143: "IMAP (TCP)",
    161: "SNMP (UDP)",
    162: "SNMPTRAP (UDP)",
    179: "BGP (TCP)",
    389: "LDAP (TCP/UDP)",
    443: "HTTPS (TCP)",
    445: "SMB (TCP)",
    465: "SMTPS (TCP)",
    500: "ISAKMP/IKE (UDP)",
    514: "Syslog (UDP)",
    515: "LPD (TCP)",
    520: "RIP (UDP)",
    587: "SMTP Submission (TCP)",
    636: "LDAPS (TCP)",
    989: "FTPS-data (TCP)",
    990: "FTPS (TCP)",
    993: "IMAPS (TCP)",
    995: "POP3S (TCP)",
    1433: "Microsoft SQL Server (TCP)",
    1521: "Oracle DB (TCP)",
    1723: "PPTP (TCP)",
    2049: "NFS (TCP/UDP)",
    2082: "cPanel (TCP)",
    2083: "cPanel SSL (TCP)",
    2086: "WHM (TCP)",
    2087: "WHM SSL (TCP)",
    2181: "Zookeeper (TCP)",
    2375: "Docker (TCP)",
    2483: "Oracle DB SSL (TCP)",
    3306: "MySQL (TCP)",
    3389: "RDP (TCP)",
    3690: "Subversion (TCP)",
    4444: "Metasploit (TCP)",
    5432: "PostgreSQL (TCP)",
    5601: "Kibana (TCP)",
    5900: "VNC (TCP)",
    5985: "WinRM (HTTP)",
    5986: "WinRM (HTTPS)",
    6379: "Redis (TCP)",
    6443: "Kubernetes API (TCP)",
    6667: "IRC (TCP)",
    7001: "WebLogic (TCP)",
    8000: "HTTP Alt (TCP)",
    8008: "HTTP Alt (TCP)",
    8080: "HTTP Alt (TCP)",
    8443: "HTTPS Alt (TCP)",
    9000: "SonarQube (TCP)",
    9042: "Cassandra (TCP)",
    9092: "Kafka (TCP)",
    9200: "Elasticsearch (TCP)",
    27017: "MongoDB (TCP)"
}
def input_validation(ip_address, First_port, Last_port):
    try:
        resolved_ip = socket.gethostbyname(ip_address)
    except socket.error:
        return "Invalid IP address"
    try:
        First_port = int(First_port)
        Last_port = int(Last_port)
    except ValueError:
        return "Ports must be integers"
    if First_port < 1 or Last_port > 65535 or First_port > Last_port:
        return "Invalid port range"
    return resolved_ip, First_port, Last_port


def loopscan(resolved_ip, First_port, Last_port):
    ports_scanned = 0
    open_ports = []
    start_time = time.time()
    for port in range (First_port, Last_port+1):
        ports_scanned += 1
        total_ports = Last_port - First_port + 1
        pregress = ports_scanned / total_ports
        my_progress_bar.set(pregress)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((resolved_ip,port))
        if result == 0:
            output = f"PORT {port} is OPEN"
            if port in common_ports:
                output += f" Service: {common_ports[port]}"
            else:
                output += " Service: Unknown"
            open_ports.append(output)
        s.close()
            

    end_time = time.time()
    elapsed_time = end_time - start_time 
    open_ports.append(f"Scan completed in {elapsed_time:.2f} seconds")
    return "\n".join(open_ports)


def start_scan():
    button.configure(state="disabled")

    ip_address = entry1.get()
    First_port = entry2.get()
    last_port = entry3.get()
    

    result= input_validation(ip_address, First_port, last_port)

    if isinstance(result, str):
        root.after(0, display_result, result)
        return
    
    resolved_ip, First_port, Last_port = result
    result1 =  loopscan(resolved_ip, First_port, Last_port)

    root.after(0, display_result, result1)


    

def display_result(text):
    results.delete("1.0", "end")
    results.insert("end", text)
    button.configure(state="normal")

def scan():
    button.configure(state="disabled")
    threading.Thread(target=start_scan).start()


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x600")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
       
label = customtkinter.CTkLabel(master=frame, text="Port Scanner", font=("Segoe UI",24))
label.pack(pady=12, padx=10)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="IP Address", show="")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="First Port", show="")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Last Port", show="")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Scan Ports", command=lambda: scan())
button.pack(pady=12, padx=10)

results = customtkinter.CTkTextbox(master=frame, width=400, height=150, )
results.pack(pady=12, padx=10)

my_progress_bar = customtkinter.CTkProgressBar(master=frame,orientation="horizontal", width=400, height=30)
my_progress_bar.pack(pady=30)
my_progress_bar.set(0.0)

label = customtkinter.CTkLabel(master=frame, text="Progress Bar", font=("Segoe UI",15))
label.pack(pady=5, padx=10)


root.mainloop()
