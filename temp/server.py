import socket
import sys

def listen_for_packets(listen_ip, listen_port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    listen_address = (listen_ip, listen_port)
    udp_socket.bind(listen_address)

    print(f"Listening for packets on {listen_ip}:{listen_port}")

    try:
        while True:
            # Receive data and the address of the sender
            data, sender_address = udp_socket.recvfrom(1024)  # Adjust buffer size as needed

            # Decode the received data
            message = data.decode('utf-8')

            print(f"Received packet from {sender_address}: {message}")

            # Check for the 'q' key press
            if message.lower() == 'q':
                print("Program terminated by user.")
                udp_socket.close()
                break  # Exit the program

    except KeyboardInterrupt:
        print("Listening stopped by user.")
    finally:
        # Close the socket
        udp_socket.close()

# Example usage
listen_ip = '192.168.0.106'  # Listen on all available network interfaces
listen_port = 1234  # Choose a port to listen on

listen_for_packets(listen_ip, listen_port)
