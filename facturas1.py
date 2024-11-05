from lxml import etree
import xml.etree.ElementTree as ET
import os
import pandas as pd

# Ruta del directorio que contiene los archivos XML
directorio = r'C:\Listados\xd\z08110012590142400008af4\facturas'

# Lista para almacenar la información extraída de cada XML
datos_facturas = []

# Recorrer todos los archivos XML en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".xml"):
        xml_file = os.path.join(directorio, archivo)

        # Leer el contenido del archivo XML
        tree = etree.parse(xml_file)
        root = tree.getroot()

        # Definir namespaces
        namespaces = {
            'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
            'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
            'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
            'xades': 'http://uri.etsi.org/01903/v1.3.2#'
        }

        # Extraer datos desde la etiqueta <cbc:Description>
        descriptions = root.xpath('//cbc:Description/text()', namespaces=namespaces)
        mi_nuevo_xml = ET.fromstring(descriptions[0])

        # Extraer la información requerida
        id_factura = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")[0].text
        fecha_pago = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate")[0].text
        do = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note")[0].text
        n_pedido = mi_nuevo_xml.findall("{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note")[1].text
        pago_terceros = mi_nuevo_xml.findall(".//cbc:TaxableAmount", namespaces={"cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"})[0].text

        # Agregar la información extraída a la lista de datos
        datos_facturas.append({
            'ID Factura': id_factura,
            'Fecha de Pago': fecha_pago,
            'DO': do,
            'Número de Pedido': n_pedido,
            'Pago a Terceros': pago_terceros
        })

# Convertir la lista de datos en un DataFrame de pandas
df = pd.DataFrame(datos_facturas)

# Guardar el DataFrame en un archivo Excel
output_file = r'C:\Listados\xd\z08110012590142400008af4\Datos1.xlsx'
df.to_excel(output_file, index=False)

print(f"Datos extraídos y guardados en {output_file}")
