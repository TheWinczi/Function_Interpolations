import matplotlib.pyplot as plt
import functions.spline_functions_interpolation as sp
import functions.lagrange_interpolation as li
import functions.calculate_error as er
import constants as const
from classes import Database
import random



def set_symmetric_data(xs: list, ys: list, interval: int):
    """ set data needed to approximate functions """

    x_data = xs[0:-1:interval]
    y_data = ys[0:-1:interval]

    x_data[-1] = xs[-1]
    y_data[-1] = ys[-1]

    return x_data, y_data


def set_random_data(xs: list, ys: list, interval: int):
    """ set random data for each interval needed to proximate functions """

    x_data = []
    y_data = []

    for i in range(len(xs) // interval):
        index = random.randrange(interval * i, interval * (i+1))
        x_data.append(xs[index])
        y_data.append(ys[index])

    x_data.append(xs[-1])
    y_data.append(ys[-1])

    x_data[0] = xs[0]
    y_data[0] = ys[0]

    return x_data, y_data


def main():
    """ main function in program """

    database = Database.Database()
    database.load_all_data(const.FILES_NAMES, const.FILES_PATHS)

    figures_index = 0
    samples_intervals = [10, 20, 50, 80, 120]

    for i, data_name in enumerate(const.FILES_NAMES):

        for samples_int in samples_intervals:
            xs = database.get_column_by_name(data_name, "distance")
            ys = database.get_column_by_name(data_name, "height")
            x_data, y_data = set_symmetric_data(xs, ys, samples_int)

            lagrange_approx = li.lagrange_interpolation(x_data, y_data, xs)
            spline_approx = sp.spline_functions_interpolation(x_data, y_data, xs)

            lagrange_error = er.calculate_error(ys, lagrange_approx)
            spline_error = er.calculate_error(ys, spline_approx)

            # create approximate functions figure
            fig = plt.figure(figures_index)
            plt.plot(xs, ys, '-b')
            # plt.plot(xs, lagrange_approx, '-'.join(const.lagrange_color), label='lagrange')
            plt.plot(xs, spline_approx, '-'.join(const.spline_color), label='spline functions')
            plt.xlabel('dystans [m]')
            plt.ylabel('wysokosc n.p.m. [m]')
            plt.title('Wykres przyblizen funkcji dwoma sposobami, l. ROWNOODLEGLYCH probek = {0}'.format(len(x_data)))
            plt.legend()
            plt.show()
            fig.savefig("img\\{0}_{1}_aproksymacje.png".format(i, figures_index))

            # close figure
            plt.close()

            # create errors data figure
            fig, axs = plt.subplots(2, 1, constrained_layout=True, sharex=True)
            axs[0].plot(xs, lagrange_error["avgs"], '-'.join(const.lagrange_color), label='lagrange')
            axs[0].plot(xs, spline_error["avgs"], '-'.join(const.spline_color), label='spline functions')
            axs[0].set_ylabel('srednia wartosc bledu')
            axs[0].set_title('Wykres wartosci srednich bledow przyblizen, l. ROWNOODLEGLYCH probek = {0}'.format(len(x_data)))
            axs[0].legend()

            axs[1].plot(xs, lagrange_error["sums"], '-'.join(const.lagrange_color), label='lagrange')
            axs[1].plot(xs, spline_error["sums"], '-'.join(const.spline_color), label='spline functions')
            axs[1].set_xlabel('kolejne przyblizenia')
            axs[1].set_ylabel('suma bledow przyblizenia')
            axs[1].set_title('Wykres wartosci sum bledow przyblizen, l. ROWNOODLEGLYCH probek = {0}'.format(len(x_data)))
            axs[1].legend()
            plt.show()
            fig.savefig("img\\{0}_{1}_bledy.png".format(i, figures_index))

            figures_index += 1

    # ---------------------------------------------------------

    sample_interval = 80
    xs = database.get_column_by_name(const.FILES_NAMES[1], "distance")
    ys = database.get_column_by_name(const.FILES_NAMES[1], "height")

    for i in range(5):
        x_data, y_data = set_random_data(xs, ys, sample_interval)

        lagrange_approx = li.lagrange_interpolation(x_data, y_data, xs)
        spline_approx = sp.spline_functions_interpolation(x_data, y_data, xs)

        lagrange_error = er.calculate_error(ys, lagrange_approx)
        spline_error = er.calculate_error(ys, spline_approx)

        # create approximate functions figure
        fig = plt.figure(figures_index)
        plt.plot(xs, ys, '-b')
        plt.plot(xs, lagrange_approx, '-'.join(const.lagrange_color), label='lagrange')
        plt.plot(xs, spline_approx, '-'.join(const.spline_color), label='spline functions')
        plt.xlabel('dystans [m]')
        plt.ylabel('wysokosc n.p.m. [m]')
        plt.title('Wykres przyblizen funkcji dwoma sposobami, l. LOSOWYCH probek = {0}'.format(len(x_data)))
        plt.legend()
        plt.show()
        fig.savefig("img\\{0}_losowe_{1}_aproksymacje.png".format(i, figures_index))

        # close figure
        plt.close()

        # create errors data figure
        fig, axs = plt.subplots(2, 1, constrained_layout=True, sharex=True)
        axs[0].plot(xs, lagrange_error["avgs"], '-'.join(const.lagrange_color), label='lagrange')
        axs[0].plot(xs, spline_error["avgs"], '-'.join(const.spline_color), label='spline functions')
        axs[0].set_ylabel('srednia wartosc bledu')
        axs[0].set_title('Wykres wartosci srednich bledow przyblizen, l. LOSOWYCH probek = {0}'.format(len(x_data)))
        axs[0].legend()

        axs[1].plot(xs, lagrange_error["sums"], '-'.join(const.lagrange_color), label='lagrange')
        axs[1].plot(xs, spline_error["sums"], '-'.join(const.spline_color), label='spline functions')
        axs[1].set_xlabel('kolejne przyblizenia')
        axs[1].set_ylabel('suma bledow przyblizenia')
        axs[1].set_title('Wykres wartosci sum bledow przyblizen, l. LOSOWYCH probek = {0}'.format(len(x_data)))
        axs[1].legend()
        plt.show()
        fig.savefig("img\\{0}_losowe_{1}_bledy.png".format(i, figures_index))

        figures_index += 1


# Let's start the project!
if __name__ == '__main__':
    main()
