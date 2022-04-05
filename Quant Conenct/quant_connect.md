# 《海淀的远方》

​		Quant Connect: Build a Line Chart

```python
class CrawlingGreenPanda(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 3, 10)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.AddEquity("ARCH", Resolution.Minute)
        
        price_plot = Chart("ARCH Chart")
        price_plot.AddSeries(Series('Price',SeriesType.Line,0))
        self.AddChart(price_plot)


    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''

        if not self.Portfolio.Invested:
             self.SetHoldings("ARCH", 1)
             
        self.Plot("ARCH Chart", "Price", self.Securities['ARCH'].Open)
```

Quant Connect: Build a Candle Chart
