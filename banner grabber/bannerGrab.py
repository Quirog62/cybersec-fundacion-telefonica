import socket

def addPorts():
    print("Ingrese a continuación los puertos para escanear: ")
    print("PRESIONE UNA LETRA CUALQUIERA PARA TERMINAR")
    portAux = input()
    ports = []
    while(portAux.isdigit()):
        ports.append(int(portAux))
        portAux = input()
    return ports

def bannerGrab(net_address,min_host,max_host,ports):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for host in range(min_host,max_host):
        for port in ports:
            try:
                socket.setdefaulttimeout(2)
                ip_adress =  net_address + "." + str(host)
                s.connect((ip_adress,int(port)))
                banner = s.recv(25).decode("utf-8")
                print("Banner encontrado en IP = " + ip_adress + ", puerto = " + str(port))
                print("Banner = " + banner)
            except:
                pass

print("ESTE PROGRAMA FUNCIONA UNICAMENTE CON PREFIJOS DE RED /24!!!")
network_address = input("Ingrese la dirección de red (SIN EL ULTIMO OCTETO): ")
ports = addPorts()
min_host = int(input("Ingrese el número del primer host a escanear, según el último octeto de su dirección IP: "))
max_host = int(input("Ingrese el número del último host a escanear, según el último octeto de su dirección IP: "))
bannerGrab(network_address,min_host,max_host,ports)


