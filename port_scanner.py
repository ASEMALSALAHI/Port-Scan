import socket

def port_scan(target_host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            sock.settimeout(1)
            # Attempt to connect to the target host and port
            result = sock.connect_ex((target_host, port))
            
            if result == 0:
                open_ports.append(port)
                
            sock.close()
            
        except socket.error:
            pass

    return open_ports

# Get user input
target = input("Enter the target IP address or hostname: ")
start = int(input("Enter the starting port number: "))
end = int(input("Enter the ending port number: "))

# Perform port scan
open_ports = port_scan(target, start, end)
print("Open ports:", open_ports)