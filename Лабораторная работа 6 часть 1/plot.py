import matplotlib.pyplot as plt
import numpy as np

def plot_area(U, area):
    
    Unp = np.arange(-2 * U, 2 * U, (U / 100))
    y = [0 for i in range(len(Unp))]

    fig, ax = plt.subplots()
    ax.plot(Unp, y, linewidth=1, color='black')

    LUnp = np.arange(-2 * U, -U, (U / 100))
    RUnp = np.arange(U, 2 * U, (U / 100))

    if area == 'left':
        y = [0 for i in range(len(LUnp))]
        ax.plot(LUnp, y, linewidth=3, color='blue')
        ax.plot([-U], [0], linewidth=10, marker = 'o', color='black')
        
    elif area == 'right':
        y = [0 for i in range(len(RUnp))]
        ax.plot(RUnp, y, linewidth=3, color='blue')
        ax.plot([U], [0], linewidth=10, marker = 'o', color='black')
    else:
        y = [0 for i in range(len(RUnp))]
        ax.plot(RUnp, y, linewidth=3, color='blue')
    
        LUnp = np.arange(-2 * U, -U, (U / 100))
        y = [0 for i in range(len(LUnp))]
        ax.plot(LUnp, y, linewidth=3, color='blue')
        ax.plot([-U], [0], linewidth=10, marker = 'o', color='black')
        ax.plot([U], [0], linewidth=10, marker = 'o', color='black')
        
    ax.plot([abs(2 * U)], [0], linewidth=10, marker = '>', color='black')
    
    ax.set(xlabel='U', title='Critical area')
    ax.grid()
    
    fig.savefig("graf.png")
    plt.show()
    
    