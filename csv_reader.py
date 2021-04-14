import csv


class CSVReader(list):

    def __init__(self, filename, quotechar='"', delimiter=',', encoding=None, postprocess=None):
        super().__init__()
        with open(filename, encoding=encoding, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=delimiter, quotechar=quotechar)
            header = None
            for row in reader:
                if header is None:
                    header = [x.strip() for x in row]
                else:
                    if postprocess:
                        row = postprocess(row)
                    self.append(row)

    @staticmethod
    def get_encoding(filename):
        with open(filename, 'rb') as f:
            prefix = list(f.read(2))
            if prefix[0] == 0xFF and prefix[1] == 0xFF:
                encoding = 'utf-8'
            elif prefix[0] == 0xFF and prefix[1] == 0xFE:
                encoding = 'utf-16'
            else:
                encoding = 'latin 1'
        return encoding
