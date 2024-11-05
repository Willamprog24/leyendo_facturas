from lxml import etree
import xml.etree.ElementTree as ET
import os

# Recoge la lista de los path de todas las facturas
# lista = os.algooooo
# excel = fs.algoo
#for factura in lista:
#   Recoger datos por cada factura 
#   Meter en la variable excel
#   guardar datos 
#   Ya
xml_file = r'C:\Listados\xd\z08110012590142400008af4\facturas\factura1.xml'

# Leer el contenido del archivo XML
tree = etree.parse(xml_file)

# Cargar el XML

root = tree.getroot()


# Definir namespaces
namespaces = {
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
    'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
    'xades': 'http://uri.etsi.org/01903/v1.3.2#'
}

# Extraer datos  descripciones, y otros elementos

descriptions = root.xpath('//cbc:Description/text()', namespaces=namespaces)


#print(descriptions[0])

mi_nuevo_xml = ET.fromstring(descriptions[0])

id_factura = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")[0].text
fecha_pago = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate")[0].text
do = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note")[0].text
n_pedido = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note")[1].text
pago_terceros = mi_nuevo_xml.findall(".//cbc:TaxableAmount", namespaces={"cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"})[0].text



print(id_factura,fecha_pago,do,n_pedido,pago_terceros)
