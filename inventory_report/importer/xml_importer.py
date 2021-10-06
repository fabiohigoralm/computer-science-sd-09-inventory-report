from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as xmlreader


class XmlImporter(Importer):
    def import_data(path):
        if (path.endswith(".xml")):
            with open(path, mode='r') as file:
                xml_content = xmlreader.parse(file)
                root = xml_content.getroot()
                list_data = []
                for item in root:
                    obj = {}
                    for item_data in item:
                        obj[item_data.tag] = item_data.text
                    list_data.append(obj)
                return list_data
        raise ValueError('A extensão do arquivo é inválida')
