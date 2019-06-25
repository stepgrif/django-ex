import os
from datetime import datetime

import pandas as pd
import requests
from numpy import nan


class CsvDataLoader:
    def __init__(self, url, file_path, column_name, start, end):
        self.url = url
        self.file_path = file_path
        self.column_name = column_name
        self.start = start
        self.end = end

    def load(self):
        file = pd.read_csv(self.file_path)
        data = file[self.column_name][self.start:self.end]
        for text in data:
            if text is not nan:
                tmp = {'text': text}
                resp = requests.post(self.url, data=tmp)
                print(resp, datetime.now())


if __name__ == '__main__':
    filepath = os.path.join(os.getcwd(), 'data.csv')
    loader = CsvDataLoader('http://localhost:8000/rest_api/data_raw/', filepath, 'Consumer complaint narrative', 0,
                           1000)
    loader.load()
