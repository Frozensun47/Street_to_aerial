import socket

def send_packet(source_ip, source_port, destination_ip, destination_port, message):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific source address and port
    source_address = (source_ip, source_port)
    udp_socket.bind(source_address)

    # Pack the message into bytes
    message_bytes = message.encode('utf-8')

    # Specify the destination address and port
    destination_address = (destination_ip, destination_port)

    try:
        # Send the packet
        udp_socket.sendto(message_bytes, destination_address)
        print(f"Packet sent from {source_ip}:{source_port} to {destination_ip}:{destination_port}")
    finally:
        # Close the socket
        udp_socket.close()

# Example usage
source_ip = '0.0.0.0'  # Use 0.0.0.0 to let the OS choose the source address
source_port = 12345  # Replace with the desired source port
destination_ip = '104.28.200.94'#'100.89.252.158' #'111.125.208.245'#'100.89.252.158'# '192.168.0.106' #  # Replace with the actual IP address of the destination computer
destination_port = 1234  # Replace with the port on which the destination computer is listening
message = 'Hello, this is a test packet'

send_packet(source_ip, source_port, destination_ip, destination_port, message)
