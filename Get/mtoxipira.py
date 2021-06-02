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

    """ # Busca o arquivo local xml
        tree = ET.parse('device.xml')
        root = tree.getroot()"""

    # Busca o XML externo
    url = "http://mtconnect.mazakcorp.com:5609"
    header = {'Accept': 'application/xml'}
    r = requests.get(url, headers=header)

    tree = ET.ElementTree(ET.fromstring(r.content))
    root=tree.getroot()



    # Percorre pelo arquivo XML inteiro
    for el in root.findall('.//*'):

        # Filtro de busca para encontrar uma tag específica
        if el.tag.find('Header') != -1 and el.tag.find('Headeer') == -1:
            creationTime = el.get('creationTime')

            print("\n\nTempo de criação: ", creationTime)

        if el.tag.find('PlasmaTool') != -1 and el.tag.find('PlasmaTooll') == -1:
            id = el.get('id')
            name = el.get('name')

            print("\n\nPlasmaTool id: ", id)
            print("\nPlasmaTool name: ", name)

        if el.tag.find('Description') != -1 and el.tag.find('Descriptionn') == -1:
            manufacturer = el.get('manufacturer')
            serialNumber = el.get('serialNumber')

            print("\nManufacturer: ", manufacturer)
            print("\nSerialNumber: ", serialNumber)

            # Texto entre a tag
            print("\nTipo de máquina de corte : ", el.text)

        if el.tag.find('DataItem') != -1 and el.tag.find('DataItemm') == -1:
            id = el.get('id')
            category = el.get('category')
            type = el.get('type')


            print("-" * 150)
            print("Dados Relevantes: \n".center(50))
            print(f" Id: {id}; Categoria: {category}; Tipo: {type}; \n".center(50))

    #Verifica se o tempo de execução está vazio
    if(len(tempoDeExecucao) == 0):
        tempoDeExecucao = "300"
        arquivo.write(tempoDeExecucao)


    arquivo.close()
    time.sleep(int(tempoDeExecucao))


