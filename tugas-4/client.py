import socket

def chat_client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print('Koneksi Berhasil')
    sock.connect(server_address)

    try:
        while True:
            client_message = input('Msg dari client: ')
            sock.sendall(client_message.encode('utf-8'))

            if client_message.lower() == 'exit':
                print("Client disconnected")
                break

            data = sock.recv(2048).decode('utf-8')
            if data:
                print(f"Server: {data}")
                
            if data.lower() == 'exit':
                print("Server disconnected")
                break
    except socket.error as e:
        print('Socket error: %s' % str(e))
    except Exception as e:
        print('Other exception: %s' % str(e))
    finally:
        print('Closing connection')
        sock.close()

if __name__ == '__main__':
    host = input("Masukkan IP Server: ")
    port = int(input("Masukkan port server: "))
    chat_client(host, port)
