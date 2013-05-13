"""Copyright (C) 2013 Kenneth J. D'Amica

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of 
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN 
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import numpy
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
                    self.data.insert(min_index, [float('nan')]*cols + [d['value']])

        for d in self.data:
            "Add NaN to cols that got missed."
            if len(d) == cols:
                d.append(float('nan'))

    def add_from_array(self, data_array):
        """Takes a series of [[time1, value1], [time2, value2]]"""
        pass

if __name__ == '__main__':
    ts = TSDataFrame()
    dict1 = [{'time': datetime.date(2013,1,1), 'value': 60},
             {'time': datetime.date(2013,1,2), 'value': 70},
             {'time': datetime.date(2013,1,4), 'value': 90}]
    dict2 = [{'time': datetime.date(2013,1,1), 'value': 1.2},
             {'time': datetime.date(2013,1,2), 'value': -5},
             {'time': datetime.date(2013,1,3), 'value': 3.1415}]
    ts.add_from_dict(dict1)
    ts.add_from_dict(dict2)
    for i, v in enumerate(ts.index):
        print(v, ts.data[i])
    print ts.data