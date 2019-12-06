import socket
import json

host = input("IP >>> ")
port = input("PORT >>> ")

sock = socket.socket()
sock.bind((host, int(port)))
sock.listen(True)

while True:
    conn, addr = sock.accept()
    e_data = conn.recv(1024)
    data = json.loads(e_data.decode('utf-8'))
    print(data)
    if data['title'] == 'side':
        file_side = open(data['side']+'_side.txt', 'w')
        file_side.close()
        with open('name.txt', 'w') as file:
            file.write(data['name'])
    elif data['title'] == 'ready':
        with open('other_comp_ready.txt', 'w') as file:
            file.write(' ')
    elif data['title'] == 'coords':
        with open('top.txt', 'w') as file:
            file.write(str(data['top']))
        with open('bot.txt', 'w') as file:
            file.write(str(data['bottom']))
        with open('x.txt', 'w') as file:
            file.write(str(data['speed_x']))
        with open('y.txt', 'w') as file:
            file.write(str(data['speed_y']))
        with open('spawn.txt', 'w') as file:
            file.write(" ")
    elif data['title'] == 'goal':
        with open('goal.txt', 'w') as file:
            file.write(' ')
    elif data['title'] == 'finish':
        with open('close.txt', 'w') as file:
            file.write(' ')