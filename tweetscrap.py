from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
from tabulate import tabulate

begin_date = dt.date(2019,4,15)
end_date = dt.date(2019,4,18)

limit = 10 #no.of tweets
lang = "english"

#user = realDonaldTrump

tweets = query_tweets("notre d", begindate=begin_date, enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

# print(df)
pd.options.display.max_columns = None
pd.options.display.width=None
print(tabulate(df, headers='keys', tablefmt='plain'))
