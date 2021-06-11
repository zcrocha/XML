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
    enderecoip = arquivo.readline()
    # -------------------------------------------------------------------
    arquivo = open('ConfigMtOxipira.txt', 'w')
    arquivo.write("Tempo de execução em segundos (300 = 5 minutos):\n")
    arquivo.write(tempoDeExecucao)
    arquivo.write(enderecoip)
    enderecoip = str(enderecoip)

    print(enderecoip)

    time.sleep(2)

    """    # Busca o arquivo local xml
        tree = ET.parse('device.xml')
        root = tree.getroot()"""

    # Busca o XML externo
    url = enderecoip
    header = {'Accept': 'application/xml'}
    r = requests.get(url, headers=header)

    tree = ET.ElementTree(ET.fromstring(r.content))
    root=tree.getroot()


    # Percorre pelo arquivo XML inteiro
    for el in root.findall('.//*'):

        # Filtro de busca para encontrar uma tag específica
        if el.tag.find('header') != -1 and el.tag.find('headeer') == -1:
            sender = el.get('sender')
            version = el.get('version')

            print(f"\nSender: {sender}")
            print(f"Version: {version}")
            print("-" * 150)

        if el.tag.find('availability') != -1 and el.tag.find('availabilityy') == -1:
            avail = el.text
            print(f"\nDisponibilidade da máquina (avail): {avail}")
            print("-" * 150)

        if el.tag.find('edgeconnectcutmode') != -1 and el.tag.find('edgeconnectcutmodee') == -1:
            cutmode = el.text
            print(f"\nModo de corte (cutmode): {cutmode}")
            print("-" * 150)

        if el.tag.find('program') != -1 and el.tag.find('programm') == -1:
            dataitemid = el.get('dataitemid')
            if dataitemid == 'partname':
                partname = el.text
                print(f"\nPartname: {partname}")
                print("-" * 150)

        if el.tag.find('execution') != -1 and el.tag.find('executionn') == -1:
            executestatus = el.text
            print(f"\nStatus de execução (executestatus): {executestatus}")
            print("-" * 150)

        if el.tag.find('normal') != -1 and el.tag.find('normall') == -1:
            executeerror = el.text
            print(f"\nErro de status de execução (executeerror): {executeerror}")
            print("-" * 150)

        if el.tag.find('message') != -1 and el.tag.find('messagee') == -1:
            dataitemid = el.get('dataitemid')
            if dataitemid == 'jobstatusmessage':
                jobstatusmessage = el.text
                print(f"\nJobStatusMessage: {jobstatusmessage}")
                print("-" * 150)

        if el.tag.find('plasmatoolstate') != -1 and el.tag.find('plasmatoolstatee') == -1:
            dataitemid = el.get('dataitemid')
            if dataitemid == 'xpr1_state':
                xpr1_state = el.text
                print(f"\nxpr1_state: {xpr1_state}")
                print("-" * 150)

        if el.tag.find('plasmaprocessrecordid') != -1 and el.tag.find('plasmaprocessrecordidd') == -1:
            dataitemid = el.get('dataitemid')
            if dataitemid == 'xpr1_process_id':
                xpr1_process_id = el.text
                print(f"\nxpr1_process_id: {xpr1_process_id}")
                print("-" * 150)

        if el.tag.find('plasmaprocessdescription') != -1 and el.tag.find('plasmaprocessdescriptionn') == -1:
            dataitemid = el.get('dataitemid')
            if dataitemid == 'xpr1_process_description':
                xpr1_process_description = el.text
                print(f"\nxpr1_process_description: {xpr1_process_description}")
                print("-" * 150)

        if el.tag.find('equipmenttimer') != -1 and el.tag.find('equipmenttimerr') == -1:
            dataitemid = el.get('dataitemid')
            if dataitemid == 'xpr1_arc_time':
                xpr1_arc_time = el.text
                print(f"\nxpr1_arc_time: {xpr1_arc_time}")
                print("-" * 150)

    #Verifica se o tempo de execução está vazio
    if(len(tempoDeExecucao) == 0):
        tempoDeExecucao = "300"
        arquivo.write(tempoDeExecucao)


    arquivo.close()
    time.sleep(int(tempoDeExecucao))
