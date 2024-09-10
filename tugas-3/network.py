import socket

def get_machine_info(host_name=None):
    if not host_name:
        host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return {
        'host_name': host_name,
        'ip_address': ip_address
    }

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown service"