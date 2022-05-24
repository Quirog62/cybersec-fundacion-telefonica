import nmap
import sys
import socket
import ipaddress
import netifaces
import json
import requests
#import pdb; pdb.set_trace()
def bannerGrab(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,int(port)))
        banner = s.recv(25).decode("utf-8").rstrip()
        return banner
    except:
        return ''
interfaz = sys.argv[2]
nm = nmap.PortScanner()
try:
    if sys.argv[1]=="-i":
        ip = netifaces.ifaddresses(interfaz)[netifaces.AF_INET][0]['addr']
        subnet_mask = netifaces.ifaddresses(interfaz)[netifaces.AF_INET][0]['netmask']
        netAddr = ipaddress.IPv4Network(ip + '/' + subnet_mask,strict=False)
        print("Buscando maquinas en la red " + str(netAddr) + "\n")
        parametrosScan = '-T4 -sSU --max-retries 0 -e ' + interfaz
        output = nm.scan(hosts=str(netAddr),arguments=parametrosScan)
        host_list = nm.all_hosts()

        #Imprimo los hosts con sus puertos correspondientes
        for host in host_list:
            print("IP " + host)
            print("====================")
            tcpPorts = nm[host].all_tcp()
            print("TCP:\n")
            for port in tcpPorts:
                result = '\t' + str(port) + ':   ' + bannerGrab(host,port)
                print(result)
            print("\n")
            udpPorts = nm[host].all_udp()
            print("UDP:\n")
            for port in udpPorts:
                result = '\t' + str(port) + ':   ' + bannerGrab(host,port)
                print(result)
            print("--------------------------------------------------")

        outputJson = json.dumps(output)

        #Subo el archivo output.json a una web
        url = 'http://127.0.0.1/example/fake_url.php'
        try:
            r = requests.post(url, data=outputJson)
            print("Enviando resultados a la url http://127.0.0.1/example/fake_url.php.  .  .  .     [OK]")
        except requests.exceptions.ConnectionError:
            print("Enviando resultados a la url http://127.0.0.1/example/fake_url.php.  .  .  .     [FAIL]")
        #Genero el archivo output.json
        with open('output.json','w') as salida:
            salida.write(outputJson)
        print("Generando fichero output.json .  .  .    [OK]")



except IndexError:
    print("NO SE INGRESÓ UNA INTERFAZ!!!")

except ValueError:
    print("INTERFAZ INVALIDA!!!")
