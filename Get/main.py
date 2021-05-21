# Importa a lib que trata o arquivo XML
import xml.etree.ElementTree as ET

# Busca o arquivo xml
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
        print("\n\nO nome do ativo é: ", dataItemId)
        print("\nTimestamp: ", timestamp)
        print("\nNúmero de sequência: ", sequence)
        print("\nTipo de máquina de corte : ", el.text)


    # Streams/DeviceStream/ComponentStream/Events/