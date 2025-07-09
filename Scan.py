import socket
import threading
import json

# Load known services
with open("services.json", "r") as f:
    services = json.load(f)

open_ports = []

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        service_name = services.get(str(port), "Unknown")
        print(f"[+] Port {port} OPEN ({service_name})")
        open_ports.append((port, service_name))
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP: ").strip()

    print(f"\n[!] Scanning all 65535 ports on {target}...\n")

    threads = []

    for port in range(1, 65536):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan complete. Open ports:")
    for port, service in sorted(open_ports):
        print(f" - Port {port}: {service}")

if __name__ == "__main__":
    main()
