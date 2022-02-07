import pytrends
from pytrends.request import TrendReq

pytrend = TrendReq()

kw_list = ['tasa de interes']

DATE_INTERVAL = '2022-01-01 2022-01-30'

pytrend.build_payload(kw_list, timeframe = DATE_INTERVAL, geo = 'CL')


historicaldf = pytrend.interest_over_time()

historicaldf.plot(figsize=(20,12))
