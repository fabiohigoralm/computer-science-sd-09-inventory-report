from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as xmlreader

import csv
import json


class Inventory:
    def xml_reader(file):
        xml_content = xmlreader.parse(file)
        root = xml_content.getroot()
        list_data = []
        for item in root:
            obj = {}
            for item_data in item:
                obj[item_data.tag] = item_data.text
            list_data.append(obj)
        return list_data

    @classmethod
    def read_data(cls, path):
        with open(path, mode='r') as file:
            if (path.endswith(".csv")):
                content = csv.DictReader(file)
                return [*content]
            if (path.endswith(".json")):
                content = json.load(file)
                return content
            if (path.endswith(".xml")):
                content = cls.xml_reader(file)
                return content

    @classmethod
    def import_data(cls, path, report_type):
        data = cls.read_data(path)
        if (report_type == 'simples'):
            return SimpleReport.generate(data)
        if (report_type == 'completo'):
            return CompleteReport.generate(data)
