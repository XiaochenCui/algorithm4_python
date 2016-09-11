import warnings
import matplotlib.cbook
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlim, ylim
from pylab import plot, gcf

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


class VisualAccumulator(object):
    plt.figure(num=None, figsize=(8, 6), dpi=100, facecolor='w', edgecolor='k')
    plt.ion()
    ax = plt.gca()
    ax.set_autoscale_on(True)

    fig = gcf()
    fig.canvas.set_window_title('VisualAccumulator')

    line, = plot([], [], linestyle='none', marker='.', color='grey', lw=0.2)
    line_ave, = plot([], [], linestyle='none', marker='.', color='black', lw=0.2)

    xdata, ydata = [], []
    xdata_ave, ydata_ave = [], []

    def __init__(self, x=1000, y=1000):
        self.n = 0
        self.total = 0

        xlim(0, x)
        ylim(0, y)

    def add_point(self, x, y, ave=False):
        if not ave:
            # add data to xdata and ydata
            self.xdata.append(x)
            self.ydata.append(y)
            self.line.set_data(self.xdata, self.ydata)
        else:
            # add data to xdata_ave and ydata_ave
            self.xdata_ave.append(x)
            self.ydata_ave.append(y)
            self.line_ave.set_data(self.xdata_ave, self.ydata_ave)

        # Recompute the data limits based on current artists.
        # Artist: Abstract base class for someone who renders into a FigureCanvas.
        self.ax.relim()

        # autoscale_view(tight=None, scalex=True, scaley=True):
        #   Autoscale the view limits using the data limits.
        self.ax.autoscale_view(True, True, True)

        xmin, xmax = xlim()
        if x >= xmax:
            xlim(xmin, xmax * 1.5)
            ylim(xlim())

        plt.draw()
        plt.pause(0.00000000000001)

    def add_data_value(self, value=0):
        self.n += 1
        self.total += value
        self.add_point(self.n, value)
        self.add_point(self.n, self.total / self.n, ave=True)


# 测试用例
if __name__ == '__main__':
    va_test = VisualAccumulator(20, 20)
    va_test.add_data_value(3)
    va_test.add_data_value(7)
    va_test.add_data_value(15)
    va_test.add_data_value(2)
    plt.pause(10)
