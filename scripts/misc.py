# encoding: utf-8

import matplotlib

zhfont = matplotlib.font_manager.FontProperties(
    fname='c:/windows/fonts/xhei.ttc'
)

matplotlib.use('Agg')

import matplotlib.pyplot as plt


def parse_line(line):
    fn, dist = line.split()
    params = map(float, fn.rsplit('.', 1)[0].split('_')[1:])
    fn = fn.rsplit('.', 1)[0].split('_')[0]

    return fn, params, float(dist)


def make_scatter_plot(xlabel, x, ylabel, y, fname):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(xlabel, fontsize=12, fontproperties=zhfont)
    ax.set_ylabel(ylabel, fontsize=12, fontproperties=zhfont)
    ax.grid(True, linestyle='-', color='0.75')

    ax.scatter(x, y)
    fig.savefig(fname)



