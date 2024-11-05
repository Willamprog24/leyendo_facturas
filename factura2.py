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

# Buscar la etiqueta <Description> dentro del namespace cbc
description_elements = root.findall('.//cbc:Description', namespaces=namespace)

# Convertir cada elemento en un par atributo-valor
for elem in description_elements:
    # Extraer el nombre del tag sin el namespace
    tag_name = elem.tag.split('}')[-1]
    
    # Extraer el texto
    value = elem.text.strip() if elem.text else ""
    
    # Imprimir el par clave-valor
    print(f"{tag_name}: {value}")

