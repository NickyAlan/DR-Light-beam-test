import matplotlib.pyplot as plt

def display(arr, axis=False) :
    plt.imshow(arr, cmap="gray")
    plt.axis(axis)