import pytrends
from pytrends.request import TrendReq
import pandas as pd

pytrend = TrendReq()

kw_list = ['tasa de interes']

DATE_INTERVAL = '2015-01-01 2022-01-31'

pytrend.build_payload(kw_list, timeframe = DATE_INTERVAL, geo = 'CL')


historicaldf = pytrend.interest_over_time()

historicaldf.plot(figsize=(20,12))

