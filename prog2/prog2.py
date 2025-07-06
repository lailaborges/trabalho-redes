import socket
import json
import sys
import numpy as np
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

# Classe do servidor
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        logging.info(f'Listening on: {self.host}:{self.port}')

    def wait_connection(self):
        return self.server.accept()

    def receive_data(self, conn):
        buffer = b''
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            buffer += chunk
        conn.close()
        return json.loads(buffer.decode('utf-8'))

    def send_data(self, host, port, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(json.dumps(data).encode('utf-8'))

# Leitura de argumentos
def parse_args():
    return dict(arg.split('=', 1) for arg in sys.argv[1:])

# Parâmetros
args = parse_args()
host = '0.0.0.0'
port_on = int(args.get('port_on', 5001))
port_to = int(args.get('port_to', 5003))

# Inicializa servidor
server = Server(host, port_on)

# Loop principal
while True:
    conn, addr = server.wait_connection()
    data = server.receive_data(conn)
    data['det'] = np.linalg.det(np.linalg.inv(data['matrix']))
    logging.info(f'Received package and sending to result:{port_to}')
    server.send_data('prog3', port_to, data)