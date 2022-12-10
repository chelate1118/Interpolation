""" Original Data """

from matplotlib import pyplot as plt


class Data:
    def __init__(self, data):
        unzipped = list(zip(*data))
        self.x = list(unzipped[0])
        self.y = list(unzipped[1])
    

    def len(self) -> int:
        return len(self.x)


    def plot(self, label=""):
        plt.scatter(self.x, self.y, label=label)
