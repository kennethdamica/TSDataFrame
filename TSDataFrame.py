"""Frequency conversion functions"""
import datetime

class TSDataFrame:
    """Very basic time series class. 
        *Just lines up data into a matrix.
        *No built-in frequencies."""

    def __init__(self):
        self.data = []
        self.index = []
    def add_from_dict(self, data_dict):

        """This takes an array of dictionaries consisting of 
        {'time': DateTime, 'value': Float}."""

        "See how many columns there are currently"
        if self.data: 
            cols = len(self.data[0])
        else: 
            cols = 0

        for d in data_dict:
            
            if d['time'] in self.index:
                "If index already exists, append data."
                self.data[self.index.index(d['time'])].append(d['value'])
            else:
                """When it's a new index, find the first index
                   that is greater and insert there."""
                if len([t for t in self.index if t > d['time']]) == 0:
                    self.index.append(d['time'])
                    self.data.append([float('nan')]*cols + [d['value']])
                else:
                    min_index = self.index.index(min(t for t in self.index if t > d['time']))
                    self.index.insert(min_index, d['time'])
                    self.data.insert(min_index, [float['nan']]*cols + [d['value']])


        for d in self.data:
            "Add NaN to cols that got missed."
            if len(d) == cols:
                d.append[float('nan')]

if __name__ == '__main__':
    ts = TSDataFrame()
    dict1 = [{'time': datetime.date(2013,1,1), 'value': 60},
             {'time': datetime.date(2013,1,2), 'value': 70}]
    dict2 = [{'time': datetime.date(2013,1,1), 'value': 1.2},
             {'time': datetime.date(2013,1,2), 'value': -5},
             {'time': datetime.date(2013,1,3), 'value': 80}]
    ts.add_from_dict(dict1)
    ts.add_from_dict(dict2)
    for i, v in enumerate(ts.index):
        print(v, ts.data[i])
    print ts.data