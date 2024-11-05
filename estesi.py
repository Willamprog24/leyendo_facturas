import xml.etree.ElementTree as ET

# Cargar el XML
xml_file = r'C:\Listados\xd\z08110012590142400008af4\facturas\ad08110012590142400003d8c.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

# Definir los namespaces correctamente
namespace = {
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
    'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'
}

# Buscar la etiqueta <TaxableAmount> con el atributo currencyID dentro del namespace ext
taxable_amount_elements = root.findall('.//ext:TaxableAmount', namespaces=namespace)

# Filtrar elementos con el atributo currencyID
for elem in taxable_amount_elements:
    if 'currencyID' in elem.attrib:
        print(ET.tostring(elem, encoding='utf-8').decode())
