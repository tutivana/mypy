# Host Scanner developed in Python 3
# Script writen under sys e socket Python libraries
# Use it for learning purpose
# By Tuti

import sys
import socket

argumentos = sys.argv # le configurando argumentos
try:
    host = argumentos[1]
except:
    host = 'localhost'
    #print("Nenhum IP ou domínio passado como argumento")
    #print("Precisa passar um endereço IP ou domínio para escaneo das portas.")
    #print("Sintaxe: \'hostcan.py 192.168.43.3\' ou \'hostscan.py dm.com\'")
    # sys.exit(1)

#portas = [20, 21, 22, 23, 26, 80, 119, 143, 443, 465, 587,
#990, 993, 995, 2221, 3306, 8080, 8443, 14147, 55432]

portas = [20, 21, 22, 23, 25, 26, 79, 80, 105, 106, 110, 119, 143, 443, 465, 587,
990, 993, 995, 2221, 2224, 3306, 8080, 8443, 14147, 55432]

print('{} {}'.format('Script analisando', host), end='\n\n')

portas_activas = 0
portas_filtradas = 0

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(2)

    codigo = cliente.connect_ex((host, porta))
    ip = socket.gethostbyname(host)
    dominio = socket.getfqdn(host)
    try:
        servico = socket.getservbyport(porta)
    except:
        servico = '\'filtrado\''
        if codigo == 0:
            portas_filtradas += 1
    
    #ip_do_cliente = socket.gethostbyname(socket.gethostname())
    #imprime_ip+ = cliente.getsockname()
    #imprime_timeout = cliente.gettimeout()


    if codigo == 0:
        if not 'check' in locals():
            #print("{} resolvido para {}".format(host))
            print('{:6} {stat} {servico}'.format('Porta', stat='Estado', servico='Serviço'))
            check = 1
        print("{:6} {} {:16} {} {:3}".format(porta, "ABERTA", servico, ip, dominio))
        portas_activas += 1
    #exception: socket.error    [Errno 111] Connection refused
print("\nPortas abertas: {}\tPortas filtradas: {}".format(portas_activas, portas_filtradas))
if portas_activas == 0:
    print("{}".format("Nenhum serviço correndo no host {}".format(host)))