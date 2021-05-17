import matplotlib.pyplot as plt


def create_diagrams(x1_data: list,
                    y1_data: list,
                    x2_data: list,
                    y2_data: list,
                    style1: str,
                    style2: str,
                    x_label: str,
                    y_label: str,
                    title: str,
                    show: bool = True):
    """ Create diagram using data from user """

    plt.plot(x1_data, y1_data, style1)
    plt.show(x2_data, y2_data, style2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()

    if show:
        plt.show()
