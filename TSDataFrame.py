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
    def num_columns(self):
        "Returns number of data columns"
        if self.data: 
            return len(self.data[0])
        else: 
            return 0
    def add(self, data_object):
        """This takes an array of dictionaries consisting of 
        {'time': DateTime, 'value': Float}

        or an array of arrays like 
        [[period1,value1],[period2,value2]]"""
        if len(data_object) == 0:
            raise(Exception("Empty data series passed"))

        object_type = type(data_object[0])

        cols = self.num_columns()

        for d in data_object:
            if object_type == type({}):
                period = d['time']
                value = d['value']
            elif object_type == type([]):
                period = d[0]
                value = d[1]
            else: 
                pass

            if period in self.index:
                "If index already exists, append data."
                self.data[self.index.index(period)].append(value)
            else:
                """When it's a new index, find the first index
                   that is greater and insert there."""
                if len([t for t in self.index if t > period]) == 0:
                    self.index.append(period)
                    self.data.append([float('nan')]*cols + [value])
                else:
                    min_index = self.index.index(min(t for t in self.index if t > period))
                    self.index.insert(min_index, period)
                    self.data.insert(min_index, [float('nan')]*cols + [value])

        for d in self.data:
            "Add NaN to cols that got missed."
            if len(d) == cols:
                d.append(float('nan'))


if __name__ == '__main__':
    ts = TSDataFrame()
    dict1 = [{'time': datetime.date(2013,1,1), 'value': 60},
             {'time': datetime.date(2013,1,2), 'value': 70},
             {'time': datetime.date(2013,1,4), 'value': 90}]
    dict2 = [{'time': datetime.date(2013,1,1), 'value': 1.2},
             {'time': datetime.date(2013,1,2), 'value': -5},
             {'time': datetime.date(2013,1,3), 'value': 3.1415}]
    dict3 = [[datetime.date(2013,1,1), 1000], 
             [datetime.date(2013,1,5), 1200]]
    ts.add(dict1)
    ts.add(dict2)
    ts.add(dict3)
    for i, v in enumerate(ts.index):
        print(v, ts.data[i])
    print ts.data