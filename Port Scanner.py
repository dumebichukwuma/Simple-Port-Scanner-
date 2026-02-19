import socket
import threading
import time


#'Try this ip 16.58.223.238'
while True:
    try:
        ip_address = input('Input valid ip addresss')
        resolved_ip = socket.gethostbyname(ip_address)
        break
    except socket.gaierror:
        print("Invalid IP or hostname")
        

while True:
    try:
        First_port = int(input("First port: "))
        Last_port = int(input("Last port: "))
    except ValueError:
        print("Ports must be integers")
        continue
    if First_port < 1 or Last_port > 65535 or First_port > Last_port:
        print("Invalid port range")
        continue
    break



def scan_port(resolved_ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((resolved_ip,port))
    if result == 0:
        print(f"PORT {port} is OPEN")
    s.close() 

threads = []

start_time = time.time()
for port in range (First_port, Last_port+1):
    thread = threading.Thread(target=scan_port, args=(resolved_ip,port,))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

end_time = time.time()
elapsed_time = end_time - start_time 
print(f"Scan Time {elapsed_time} seconds")