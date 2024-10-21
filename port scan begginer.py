
import socket 

def port_scan(ip,start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, port))
            open_ports.append(port)
            sock.close()
        except socket.error:
            pass
        return open_ports
    
def main():
    ip = input("Enter IP address")
    start_port = int(input("Enter start port:"))
    end_port = int(input("Enter end port:"))

    open_ports = port_scan(ip,start_port, end_port)

    print(f"Open ports on {ip}: {open_ports}")

if __name__ == "__main__" :
    main()