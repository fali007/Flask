import matplotlib.pyplot as plt

class pmo:
    def __init__(self,var,title):
        plt.plot(var)
        plt.savefig(title+'.png')