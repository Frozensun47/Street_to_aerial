import streamlit as st
import socket

def listen_for_packets(listen_ip, listen_port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    listen_address = (listen_ip, listen_port)
    udp_socket.bind(listen_address)

    st.write(f"Listening for packets on {listen_ip}:{listen_port}")

    try:
        while True:
            # Receive data and the address of the sender
            data, sender_address = udp_socket.recvfrom(1024)  # Adjust buffer size as needed

            # Decode the received data
            message = data.decode('utf-8')

            st.write(f"Received packet from {sender_address}: {message}")

            # Check for the 'q' key press
            if message.lower() == 'q':
                st.write("Program terminated by user.")
                udp_socket.close()
                break  # Exit the program

    except KeyboardInterrupt:
        st.write("Listening stopped by user.")
    finally:
        # Close the socket
        udp_socket.close()

# Streamlit UI
st.title("UDP Packet Listener")

listen_ip = st.text_input("Enter IP address to listen on:", "192.168.0.106")
listen_port = st.number_input("Enter port to listen on:", 1, 65535, 1234)

if st.button("Start Listening"):
    listen_for_packets(listen_ip, listen_port)
