# Python GUI Port Scanner

A multithreaded TCP port scanner built with Python and CustomTkinter.  
This tool scans a target host for open TCP ports within a specified range and displays results in a graphical interface with a live progress bar.

---

## Features

- TCP Connect Port Scanning  
- Graphical User Interface (GUI)  
- Real-time Progress Bar  
- Multithreading (keeps UI responsive)  
- Input Validation (IP + port range)  
- Service Name Detection for Common Ports  
- Scan Time Display  

---

## 🛠 Technologies Used

- Python 3  
- socket – Network connections  
- threading – Background scanning  
- time – Scan duration tracking  
- customtkinter – Modern GUI  

---

## 📦 Installation

1. Install Python 3.10 or higher  
2. Install CustomTkinter:

```bash
pip install customtkinter
```

3. Run the program:

```bash
python portscanner.py
```

---

## 🖥 How It Works

1. The user enters:
   - Target IP address or hostname
   - First port
   - Last port

2. The program:
   - Validates input
   - Resolves hostname to IP address
   - Scans each port using TCP `connect_ex`
   - Updates the progress bar in real time
   - Displays open ports with detected services

3. After completion:
   - Displays total scan duration
   - Shows all discovered open ports

---

## Example Output


<img width="497" height="626" alt="Screenshot 2026-02-24 1627432" src="https://github.com/user-attachments/assets/1922fa03-032e-4e34-b31f-1dee3e401528" />


---

## Ethical Use Notice

This tool is intended strictly for:

- Educational purposes  
- Testing systems you own  
- Authorized lab environments  

Do NOT scan networks or systems without explicit permission. Unauthorized scanning may be illegal.

Safe practice target:
- scanme.nmap.org (provided for learning purposes)

---

## What I Learned

- Working with TCP sockets  
- Handling concurrency using threading  
- Updating GUI elements safely using `root.after`  
- Tracking execution time  
- Designing a functional desktop interface  

---

## Future Improvements

- Add UDP scanning  
- Implement thread pool for better performance  
- Add export-to-file functionality  
- Add a Stop Scan button  
- Add colored output for open ports  
- Add logging system  

---

## License

This project is for educational purposes only.
