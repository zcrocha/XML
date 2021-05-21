# Importa a lib que trata o arquivo XML
import xml.etree.ElementTree as ET

# Permite que seja possível se conectar a um XML externo
import requests

# Busca o XML externo
"""url = "https://www.w3schools.com/xml/note.xml"
header = {'Accept': 'application/xml'}
r = requests.get(url, headers=header)

tree = ET.ElementTree(ET.fromstring(r.content))
root=tree.getroot()"""

# Busca o arquivo local xml
tree=ET.parse('exemplo.xml')
root=tree.getroot()

# Percorre pelo arquivo XML inteiro
for el in root.findall('.//*'):

    # Filtro de busca para encontrar uma tag específica
    # ----------------- Jeito certo ------------------------------- Jeito errado ------------
    if el.tag.find('EdgeConnectCutMode') != -1 and el.tag.find('EdgeConnectCutModee') == -1:

        dataItemId=el.get('dataItemId')
        timestamp=el.get('timestamp')
        sequence=el.get('sequence')

        # Valores dentro da tag
        print("\n\nO nome do ativo é: ", dataItemId)
        print("\nTimestamp: ", timestamp)
        print("\nNúmero de sequência: ", sequence)

        # Texto entre a tag
        print("\nTipo de máquina de corte : ", el.text)


    # Streams/DeviceStream/ComponentStream/Events/