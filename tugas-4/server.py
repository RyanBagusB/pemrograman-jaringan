import socket
import argparse

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    finally:
        s.close()
    return ip_address

host = get_local_ip()
data_payload = 2048
backlog = 5

def chat_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    sock.bind(server_address)
    sock.listen(backlog)

    print('Menunggu Koneksi')
    client, address = sock.accept()

    while True:
        data = client.recv(data_payload).decode('utf-8')
        if data:
            print(f"Client: {data}")
            if data.lower() == 'exit':
                print("Client disconnected")
                break

            server_response = input('Msg dari server: ')
            client.sendall(server_response.encode('utf-8'))
        
        if server_response.lower() == 'exit':
            break

    client.close()
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TCP Chat Server')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    chat_server(port)
