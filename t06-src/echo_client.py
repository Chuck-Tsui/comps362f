from concurrent.futures import ThreadPoolExecutor
import logging, socket, sys

HOST, PORT = "localhost", 7000

def echo_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
        ss.connect((host, port))

        my_file = ss.makefile("rw", encoding = "UTF-8", newline = "")
        while True:          
            my_input = input("Enter you message: ").strip()
            if my_input == "":
                break
            my_file.write(my_input + "\r\n")
            my_file.flush()
            rx_file = my_file.readline().strip()
            print("This is the rx message: " + rx_file)
            

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT
    echo_client(host, port)