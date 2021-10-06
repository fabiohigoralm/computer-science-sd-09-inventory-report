from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if (path.endswith(".csv")):
            with open(path, mode='r') as file:
                content = csv.DictReader(file)
                return [*content]
        raise ValueError('A extensão do arquivo é inválida')
