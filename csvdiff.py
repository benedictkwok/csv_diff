import csv
import socket
import sys
sophos_hosts=[]
iventi_hosts=[]
nessus_hosts=[]
newhosts=[]

def sophos_devices():
    device = '/Users/bkwok/Downloads/sophos_devices_full.csv'
    with open(device, 'r') as input_files:
        for line in input_files:
            line = line.strip()
            if line not in sophos_hosts:
                sophos_hosts.append(line)
    return sophos_hosts

def sophos_servers():
    server = '/Users/bkwok/Downloads/sophos_servers_full.csv'
    with open(server, 'r') as input_file:
        for line in input_file:
            line=line.strip()
            if line  not in sophos_hosts:
                sophos_hosts.append(line)
    return sophos_hosts

def iventi_devices():
    with open('/Users/bkwok/Downloads/Iventi-All-devices.csv', 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if line not in iventi_hosts:
                iventi_hosts.append(line)
    return iventi_hosts

def add_to_sophos(newhosts):
    with open('/Users/bkwok/Downloads/add_to_sophos.csv', 'w') as output_file:
        line:str
        for line in newhosts:
            output_file.write(line)
            output_file.write(",")
"""
def nessus_ips():
    with open('/Users/bkwok/Downloads/xperi_internal_nessus_ip.txt', 'r') as input_file:
   # with open('/Users/bkwok/Downloads/myip.txt', 'r') as input_file:
        hostname=''
        for line in input_file:
            print(line)
            try:
                #hostname = socket.gethostbyaddr('172.217.164.100')
                hostname = socket.gethostbyaddr(line)
                print (list(hostname))
                return hostname
            except socket.herror:
                #print('Unknown')
                pass
            except socket.gaierror:
                #print ('Nodename nor servname not knwon')
                pass
            if hostname not in nessus_hosts:
                nessus_hosts.append(hostname)
    return nessus_hosts
"""
def main():
    sophos_devices()
    sophos_servers()
    iventi_devices()
    #nessus_ips()

    newhosts= list(filter(lambda x: x not in sophos_hosts, iventi_hosts))
    #print("Iventi hosts to be added into  Sophos : ", list(newhosts))
    add_to_sophos(newhosts)
    #print ("Sophos : ", list(sophos_hosts))
    #print ("Iventi : ", list(iventi_hosts))
    #print ("Nessus Known Hosts : ", list(nessus_hosts))
    #print ("Intercept : ", list(filter(lambda x: x in sophos_hosts, iventi_hosts)))
    #print ("Iventi hosts not in Sophos : ", list(filter(lambda x: x not in sophos_hosts, iventi_hosts)))
    #print ("Iventi hosts not in Sophos : ", list(newhosts))
    #print ("Sophos hosts not in Iventi : ", list(filter(lambda x: x not in iventi_hosts, sophos_hosts)))
    print ("# of Sophos hosts: ", len(list(sophos_hosts)))
    print ("# of Iventi hosts: ", len(list(iventi_hosts)))
    print ("# of the Intercept : ", len(list(filter(lambda x: x in sophos_hosts, iventi_hosts))))
    print ("# of Iventi hosts not in Sophos : ", len(list(filter(lambda x: x not in sophos_hosts, iventi_hosts))))
    print ("# of Sophos hosts not in Iventi : ", len(list(filter(lambda x: x not in iventi_hosts, sophos_hosts))))
if __name__=="__main__":
    main()