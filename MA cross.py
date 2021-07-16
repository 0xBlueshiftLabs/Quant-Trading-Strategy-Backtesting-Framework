import backtrader as bt
import backtrader.analyzers as bta
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance


class MaCrossStrategy(bt.Strategy):

    # signal generator
    def __init__(self):

        ma_fast = bt.ind.SMA(period = 10)
        ma_slow = bt.ind.SMA(period = 20)

        self.crossover = bt.ind.CrossOver(ma_fast, ma_slow)

    # executes order from the signals
    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()


cerebro = bt.Cerebro()

# pulls price data from yahoo finance
data = bt.feeds.YahooFinanceCSVData(dataname='BTC-USD.csv')

# converts to log chart
data.plotinfo.plotlog = True

# adds data to engine
cerebro.adddata(data)
# adds strategy to engine
cerebro.addstrategy(MaCrossStrategy)

# sets starting capital
cerebro.broker.setcash(1000.0)
# sets size per trade
cerebro.addsizer(bt.sizers.PercentSizer, percents = 10)

# analysis
cerebro.addanalyzer(bta.SharpeRatio, _name = "sharpe")
cerebro.addanalyzer(bta.Transactions, _name = "trans")
cerebro.addanalyzer(bta.TradeAnalyzer, _name = "trades")

# runs back test
back = cerebro.run()
print(cerebro.broker.getvalue())

# useful output data
sharpeRatio = back[0].analyzers.sharpe.get_analysis()
print(sharpeRatio)
transactions = back[0].analyzers.trans.get_analysis()
#print(transactions)
tradeAnalyzer = back[0].analyzers.trades.get_analysis()
#print(tradeAnalyzer)


# colour scheme of plot
plt.style.use('fivethirtyeight')

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams['lines.linewidth'] = 1

SIZE = 7
plt.rcParams['axes.labelsize'] = SIZE
plt.rcParams['ytick.labelsize'] = SIZE
plt.rcParams['xtick.labelsize'] = SIZE
plt.rcParams["font.size"] = SIZE

COLOR = '1'
plt.rcParams['text.color'] = COLOR
plt.rcParams['axes.labelcolor'] = COLOR
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR

plt.rcParams['grid.linewidth']=0.1
plt.rcParams['grid.color']="#101622"
plt.rcParams['lines.color']="0.5"
plt.rcParams['axes.edgecolor']="0.2"
plt.rcParams['axes.linewidth']=0.5

plt.rcParams['figure.facecolor']="#101622"
plt.rcParams['axes.facecolor']="#101622"
plt.rcParams["savefig.dpi"]=120
dpi = plt.rcParams["savefig.dpi"]
width = 1080
height = 1920
plt.rcParams['figure.figsize'] = height/dpi, width/dpi
plt.rcParams["savefig.facecolor"] ="#101622"
plt.rcParams["savefig.edgecolor"]="#101622"

plt.rcParams['legend.fontsize'] = SIZE
plt.rcParams['legend.title_fontsize'] = SIZE + 1
plt.rcParams['legend.labelspacing'] =0.25
plt.rcParams['image.cmap']='tab10'


cerebro.plot(style = 'candle',barup='white', bardown='#1973c2',volume = False)
plt.show()

