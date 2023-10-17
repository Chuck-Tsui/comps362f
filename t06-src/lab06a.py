# File: lab06a.py

# Replace the following by your full name and 8-digit student number
student_name = "Xu Xiaochi"
student_id = "12556828"

from concurrent.futures import ThreadPoolExecutor
import logging, socket, sys

HOST, PORT = "localhost", 5000

def handle_client(cs, addr):
    logging.info(f"Client connected from {addr}")
    with cs:
        #create make file
        my_file = cs.makefile("rw", encoding = "UTF-8", newline = "")
        while True:
            my_line = my_file.readline().strip()
            ls = my_line.split()
            int_list = [int (a) for a in ls]
            if my_file == "":
                break
            my_file.write(sum(int_list) + "\r\n")
            my_file.flush()
            
    logging.info(f"Client disconnected from {addr}")

def echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
        ss.bind((host, port))
        ss.listen()
        logging.info(f"Server started, listening on {(host, port)}")
        with ThreadPoolExecutor() as executor:
            while True:
                cs, addr = ss.accept()
                executor.submit(handle_client, cs, addr)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT
    echo_server(host, port)
