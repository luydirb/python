from pandas import read_csv
from matplotlib import pyplot
series = read_csv(r"C:\Users\luydi\OneDrive\Documentos\python\USD_BRL_hist.csv", header=0, index_col=0, parse_dates=True) 
series.squeeze("columns")
series.plot()
pyplot.show()
