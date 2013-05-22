#!ipython --pylab=auto
# encoding: utf-8

from misc import parse_line, make_scatter_plot

if __name__ == '__main__':
    x, y = [], []
    with open('speckles.txt') as f:
        for line in f:
            fn, (parameter,), dist = parse_line(line)
            if fn == 'gs0' and parameter <= 0.1:
                x.append(parameter)
                y.append(dist)

    make_scatter_plot(u'椒盐噪声参数', x,
                      u'与原图的距离', y,
                      '../images/speckle_gs0.png')


