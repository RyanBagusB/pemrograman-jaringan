import socket

data_payload = 2048

def echo_client(host, port):
    f = open('%s.txt' % host, "a")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (host, port)
        
        sock.settimeout(5)
        sock.sendto('first_join?'.encode('utf-8'), server_address)
        data, _ = sock.recvfrom(data_payload)

        if data.decode() == 'successfully_connected?':
            print('Koneksi berhasil\n')
            sock.settimeout(None)
        while True:
            message = input('Client: ')

            if message == 'quit':
                print('Data disimpan')
                break

            sock.sendto(message.encode('utf-8'), server_address)
            f.write('Client: %s\n' % message)
            data, _ = sock.recvfrom(data_payload)
            f.write('Msg dari server: %s\n' % data.decode())
            print('Msg dari server: %s' % data.decode())
    except socket.error as e:
        print('Socket error: %s' % str(e))
    except Exception as e:
        print('Other exception: %s' % str(e))
    finally:
        sock.close()
        f.close()

def read_history(filename):
    f = open(filename, 'r')
    print(f.read())

if __name__ == '__main__':
    print("Pilih opsi:")
    print("1. Koneksi ke server")
    print("2. Melihat history")

    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        host = input("Masukkan IP Server: ")
        port = int(input("Masukkan port server: "))
        echo_client(host, port)
    elif pilihan == '2':
        filename = input("Masukkan nama file: ")
        read_history(filename)
    else:
        print("Pilihan tidak valid!")
