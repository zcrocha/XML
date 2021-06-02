import xml.etree.ElementTree as ET
import time
import requests
import sys
import os

# Pausa de 5 minutos (300seg)
"""tempoDeExecucao = int(input("Digite o intervalo de tempo para consumo desses dados: "))"""


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


while 1:

    # Verifica o arquivo de texto
    arquivo = open('ConfigMtOxipira.txt', 'r')
    fraseDeExibicao = arquivo.readline()
    tempoDeExecucao = arquivo.readline()
    # -------------------------------------------------------------------
    arquivo = open('ConfigMtOxipira.txt', 'w')
    arquivo.write("Tempo de execução em segundos (300 = 5 minutos):\n")
    arquivo.write(tempoDeExecucao)

    # Busca o XML externo
    """url = "http://mtconnect.mazakcorp.com:5609"
    header = {'Accept': 'application/xml'}
    r = requests.get(url, headers=header)

    tree = ET.ElementTree(ET.fromstring(r.content))
    root=tree.getroot()"""

    # Busca o arquivo local xml
    tree = ET.parse('device.xml')
    root = tree.getroot()

    # Percorre pelo arquivo XML inteiro
    for el in root.findall('.//*'):

        # Filtro de busca para encontrar uma tag específica
        if el.tag.find('Header') != -1 and el.tag.find('Headeer') == -1:
            sender = el.get('sender')
            version = el.get('version')

            print(f"\nSender: {sender}")
            print(f"Version: {version}")

        if el.tag.find('DataItem') != -1 and el.tag.find('DataItemm') == -1:
            id = el.get('id')
            type = el.get('type')
            subType = el.get('subType')

            if id == 'avail':
                print(f"\nDisponibilidade da máquina: {type}")

            elif id == 'cutmode':
                print("-" * 150)
                print(f"Modo de corte (cutmode): {type}")

            elif id == 'partname':
                print(f"PartName: {type}")

            elif id == 'executestatus':
                print(f"Execute Status: {type}")

            elif id == 'executeerror':
                print(f"Execute Error: {type}")

            elif id == 'jobstatusmessage':
                print(f"Job Status Message: {type}")
                print("-" * 150)

            elif id == 'xpr1_state':
                print(f"\nxpr1_state: {type}")

            elif id == 'xpr1_process_id':
                print(f"xpr1_process_id: {type}")

            elif id == 'xpr1_process_description':
                print(f"xpr1_process_description: {type}")

            elif id == 'xpr1_arc_time':
                print(f"xpr1_arc_time: {type} --> {subType}")

    #Verifica se o tempo de execução está vazio
    if(len(tempoDeExecucao) == 0):
        tempoDeExecucao = "300"
        arquivo.write(tempoDeExecucao)


    arquivo.close()
    time.sleep(int(tempoDeExecucao))


