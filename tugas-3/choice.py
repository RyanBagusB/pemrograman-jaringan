import socket
from network import get_service_name, get_machine_info

def first_choice():
    try:
        port = int(input("Masukkan port protokol: "))
        service_name = get_service_name(port)
        print(f"Port: {port} => Service name: {service_name}")
    except ValueError:
        print("Port harus berupa angka.")

def second_choice():
    website = input("Masukkan alamat web: ")
    try:
        local_info = get_machine_info()
        website_info = get_machine_info(website)
        print(f"Anda mengakses {website_info['host_name']} dengan alamat IP {website_info['ip_address']}")
        print(f"dari komputer {local_info['host_name']} dengan alamat IP {local_info['ip_address']}")
    except socket.gaierror:
        print("Alamat web tidak valid atau tidak dapat diakses.")