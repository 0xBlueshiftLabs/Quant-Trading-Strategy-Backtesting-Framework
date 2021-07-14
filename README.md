

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



# Framework for backtesting quantitative trading strategies

Quantitative trading is a type of market strategy that relies on mathematical and statistical models to identify and execute opportunities and trades.

This project aims to serve as a framework for developing and backtesting trading strategies, allowing for easy data visualisation and strategy performance comparison.

Presented in the script as a demonstration, an extremely basic, and likely unprofitable, simple moving average crossover strategy is provided. Said strategy buys when the 10-day moving average crosses the 50-day moving average, and sells when the reverse occurs.

Building upon this framework, much more complex, robust, and profitable strategies can be built, tested, and optimised.






### Real-World Use-Cases


💰 Develop and backtest trading strategies

🏦 Develop highly customised indicators

💲 Compare and analyse quant strategies




### Development-Goals


🧰 Develop a framework for backtesting trading strategies

☑️ Deep dive into Backtrader's library and understand both it's capabilities and limitations.

🧾 Further develop knowledge of Matplotlib

🤖 Backtest a simple moving average crossover trading strategy




## Built With

* [Backtrader](https://www.backtrader.com/)
* [Matplotlib](https://matplotlib.org/)



<!-- GETTING STARTED -->
## Getting Started

1. [Obtain price data](https://github.com/Elisik/Binance-API-Price-Data-Interface).

2. Create a signal generator within the __init__ function of the strategy class:
  ```py
   # signal generator
    def __init__(self):

        ma_fast = bt.ind.SMA(period = 10)
        ma_slow = bt.ind.SMA(period = 50)

        self.crossover = bt.ind.CrossOver(ma_fast, ma_slow)
  ```
   
3. Create buy and sell orders based upon the previously generate signals. For example:
  ```py
   # executes order from the signals
    def next(self):
        if not self.position:         # if not already in a position
            if self.crossover > 0:    # if 10-day moving average crosses above 50-day moving average
                self.buy()            # take a long position
        elif self.crossover < 0:      # if 10-day moving average crosses below 50-day moving average
            self.close()              # close long position
   ```
   
3. Initialise the backtesting engine (Cerebro). Add the price data and strategy before setting inital conditions such as account size and risk amount per trade etc.
  ```py
    cerebro = bt.Cerebro()

    # adds data to engine
    cerebro.adddata(data)
    # adds strategy to engine
    cerebro.addstrategy(MaCrossStrategy)

    # sets starting capital
    cerebro.broker.setcash(1000.0)
    # sets size per trade
    cerebro.addsizer(bt.sizers.PercentSizer, percents = 10)
  ```

4. Run the back test using:
  ```
    back = cerebro.run()
  ```

  

  
  

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@TraderTDF](https://twitter.com/TraderTDF)

LinkedIn - [https://www.linkedin.com/in/RAMWatson/](https://www.linkedin.com/in/RAMWatson/)

Project Link: [https://github.com/Elisik/Quant-Trading-Strategy-Backtesting-Framework](https://github.com/Elisik/Quant-Trading-Strategy-Backtesting-Framework)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/RAMWatson/
[product-screenshot]: screenshot.jpg

