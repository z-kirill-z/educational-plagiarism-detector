import matplotlib.pyplot as plt


def plot_similarity_matrix(matrix, labels):
    fig, ax = plt.subplots()
    cax = ax.matshow(matrix)

    plt.xticks(range(len(labels)), labels, rotation=90)
    plt.yticks(range(len(labels)), labels)

    fig.colorbar(cax)
    plt.tight_layout()
    plt.show()
