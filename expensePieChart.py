# expensePieChart
# CS 175
# Ez Racancoj

import matplotlib.pyplot as plt
import numpy as np

def main():
    label_list = []
    value_list = []
    line_list = []
    for i in open('expenses.txt', 'r'):
        line = i.split('\t')
        label_list.append(line[0])
        value_list.append(int(line[1]))
    print(label_list)
    print(value_list)

    plt.style.use('_mpl-gallery-nogrid')

    (np.linspace(0.2, 0.7, len(value_list)))

    
    fig, ax = plt.subplots()
    ax.pie(value_list, labels = label_list, colors = ['b', 'orange', 'green','red','purple','brown'], radius=3, center=(4, 4),
           wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()


main()



