import xml.etree.ElementTree as ET

xml_file = r'C:\Listados\xd\z08110012590142400008af4\facturas\ad08110012590142400003d8c.xml'

tree = ET.parse(xml_file)
root = tree.getroot()
ET.dump(tree)


for x in root.findall(".//"):
    print(x.tag,"",x.text)
    
# Buscar todas las etiquetas <TaxableAmount> que tengan el atributo currencyID="COP"
# namespace = {'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'}

# for x in root.findall('.//cbc:TaxableAmount[@currencyID="COP"]', namespaces=namespace):
#     print(x.text)