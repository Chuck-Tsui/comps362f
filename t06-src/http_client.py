# File: http_client.py
import socket, sys

HOST, PORT = "google.com", 80

def get_page(host, port, page):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(f"GET {page} HTTP/1.0\r\n\r\n".encode())
        data = bytes()
        while True:
            chunk = s.recv(1024)
            if len(chunk) <= 0:
                break
            data = data + chunk
    return data.decode()

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT
    res = get_page(host, port, "/")
    print(len(res))
    print(res[:1500])
