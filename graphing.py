from matplotlib import pyplot as plt
from setup import *

def plot_pairwise_diversities(x, y1, y2, y3, col1, col2, col3, q, xlab='Years'):
    """
    :param x: x_axis
    :param y1: turnover
    :param y2: sorensen
    :param y3: jaccard
    :param col1: for turnover
    :param col2: for sorensen
    :param col3: for jaccard
    :param q: diversity index
    :param xlab: No. of Years
    :return: None. Just plots and saves the graphs
    """

    div_typ = "d%s diversities" % q
    ylab = "d%s" % q
    fig = plt.figure()
    fig.suptitle('%s Diversities against Time' % ylab, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    plt.plot(x, y1, color=col1, linewidth=2.0, label='Turnover')
    plt.plot(x, y2, color=col2, linewidth=2.0, label='Sorensen')
    plt.plot(x, y3, color=col3, linewidth=2.0, label='Jaccard')
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    plt.legend()
    fig.savefig('results/%s/%s_%s.png' % (graph_typ, div_typ, ylab))

def plot_abundance_by_year(years, abundance, xlab, ylab):
    fig = plt.figure()
    fig.suptitle('%s against %s' % (ylab, xlab), fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    for s in range(len(abundance)):
        plt.plot(years, abundance[s], linewidth=2.0)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    ax.legend(["100 species"])
    fig.savefig('results/%s/abundance_by_year.png' % (graph_typ))

def plot_diversities(x, y, col, q, ylab, sim_num, xlab='Years'):
    div_typ = "d%s" % q
    fig = plt.figure()
    fig.suptitle('%s against Time' % ylab, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    plt.plot(x, y, color=col, linewidth=2.0)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    fig.savefig('results/%s/%s_%s_simulation%s.png' % (graph_typ, div_typ, ylab, sim_num))

def plot_simulations(x, y, stderr, col, q, n, typ, xlab="Years"):
    ylab="d%s %s over %s simulations" % (q, typ, n)
    div_typ = "d%s" % q
    fig = plt.figure()
    fig.suptitle('%s against Time' % ylab, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)
    plt.plot(x, y, color=col, linewidth=2.0)
    plt.errorbar(x, y, stderr, ecolor="blue")
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    fig.savefig('results/%s/%s_%s.png' % (graph_typ, div_typ, ylab))
