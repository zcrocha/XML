# Importa a lib que trata o arquivo XML
import xml.etree.ElementTree as ET

#Delay
import time

# Permite que seja possível se conectar a um XML externo
import requests

a = True

while a:

    # Busca o XML externo
    """url = "https://www.w3schools.com/xml/note.xml"
    header = {'Accept': 'application/xml'}
    r = requests.get(url, headers=header)

    tree = ET.ElementTree(ET.fromstring(r.content))
    root=tree.getroot()"""

    # Busca o arquivo local xml
    tree = ET.parse('teste.xml')
    root = tree.getroot()

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

    # Pausa de 10 minutos (600seg)
    time.sleep(600)
