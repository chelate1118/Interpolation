""" Piecewise Function """

import numpy as np
from matplotlib import pyplot as plt


class Function:
    def __init__(self):
        self.data = []
    

    def __call__(self, x: float) -> float:
        for start, end, poly in self.data:
            if not start <= x <= end:
                continue
            return poly(x)
        raise Exception("Out of Range")


    def plot(self, label=""):
        if len(self.data) == 0:
            raise Exception("Cannot Plot Empty Graph")
        
        x_range = np.linspace(self.data[0][0], self.data[0][1])
        for i in range(1, len(self.data)):
            x_range = np.append(x_range, np.linspace(self.data[i][0], self.data[i][1]))
        
        y_range = [
            self(x) for x in x_range
        ]

        plt.plot(x_range, y_range, label=label)
