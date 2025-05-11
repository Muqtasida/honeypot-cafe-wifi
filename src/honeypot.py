import socket
import datetime

HOST = "0.0.0.0"   # Listen on all network interfaces
PORT = 8000        # Port to listen on

def log_connection(addr, data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = data.decode('utf-8', errors='ignore')[:100]
    log_entry = f"[{timestamp}] Connection from {addr[0]}:{addr[1]} - Data: {message}\n"
    print(log_entry.strip())

    with open("honeypot_log.txt", "a") as log_file:
        log_file.write(log_entry)

def run_honeypot():
    print(f"[INFO] Honeypot listening on port {PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        while True:
            conn, addr = server_socket.accept()
            with conn:
                try:
                    data = conn.recv(1024)
                    if data:
                        log_connection(addr, data)
                        conn.sendall(b"Access Denied. This activity has been logged.\n")
                except Exception as e:
                    print(f"[ERROR] {e}")

if __name__ == "__main__":
    run_honeypot()


