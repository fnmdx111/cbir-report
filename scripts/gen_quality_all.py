#!ipython --pylab=auto
# encoding: utf-8

from misc import parse_line, make_scatter_plot

if __name__ == '__main__':
    x, y = [], []
    with open('qualities.txt') as f:
        for line in f:
            fn, (parameter,), dist = parse_line(line)
            if parameter > 0.9:
                x.append(parameter)
                y.append(dist)

    make_scatter_plot(u'质量因子Q', x,
                      u'与原图的距离', y,
                      '../images/quality_all_0.9_1.png')

    x, y = [], []
    with open('qualities.txt') as f:
        for line in f:
            fn, (parameter,), dist = parse_line(line)
            x.append(parameter)
            y.append(dist)

    make_scatter_plot(u'质量因子Q', x,
                      u'与原图的距离', y,
                      '../images/quality_all.png')


