import socket
import argparse

def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80)) 
        ip_address = sock.getsockname()[0]
    except Exception as e:
        print(f'Error: {str(e)}')
        ip_address = None
    finally:
        sock.close()
    return ip_address

host = get_local_ip()
data_payload = 2048

def echo_server(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (host, port)
        sock.bind(server_address)
        print('Menunggu koneksi...')

        while True:
            data, address = sock.recvfrom(data_payload)
            
            if data:
                if (data.decode() == 'first_join?') :
                    print('Koneksi dari client: %s\n' % address[0])
                    sock.sendto('successfully_connected?'.encode('utf-8'), address)
                else :
                    print('Msg dari client: %s' % data.decode())
                    message = input('Server: ')
                    sock.sendto(message.encode('utf-8'), address)
    except socket.error as e:
        print('Socket error: %s' % str(e))
    except Exception as e:
        print('Other exception: %s' % str(e))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
