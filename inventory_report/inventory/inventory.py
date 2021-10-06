from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def read_data(path):
        with open(path, mode='r') as file:
            if (path.endswith(".csv")):
                content = csv.DictReader(file)
                return [*content]
            if (path.endswith(".json")):
                content = json.load(file)
                return content

    @classmethod
    def import_data(cls, path, report_type):
        data = cls.read_data(path)
        if (report_type == 'simples'):
            return SimpleReport.generate(data)
        if (report_type == 'completo'):
            return CompleteReport.generate(data)


teste = 'xablau.json'
print(teste.endswith(".csv"))
