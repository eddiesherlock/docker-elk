import twint
from elasticsearch import Elasticsearch


abc =('MLB,New York Yankees,Boston Red Sox,Chicago White Sox,Cleveland Indians,Detroit Tigers,Baltimore Orioles,Oakland Athletics,Minnesota Twins,Atlanta Braves,Miami Marlins,New York Mets,Philadelphia Phillies,Washington Nationals,Chicago Cubs,Cincinnati Reds,Milwaukee Brewers,Pittsburgh Pirates,St. Louis Cardinals,Arizona Diamondbacks,Colorado Rockies,Los Angeles Dodgers,San Diego Padres,San Francisco Giants')
acc = abc.split(",")
# print(acc)
# print(abc)
# print(type(acc))
# print(type(abc))
# Configure
for i in acc:
    i.lower()
    c = twint.Config()
    c.Search = i
    c.Elasticsearch = "http://34.80.0.41:9200"
    c.Min_likes = 100
    c.Min_replies = 10
    c.Min_retweets = 100
    # c.Lowercase = True
    c.Index_tweets =f'search-{i}'
    c.Lang = 'en'
    c.Store_json = True
    c.Output = f"search{i}.json"
    c.Since = "2016-01-01 00:00:00"
# c.Pandas = True
#
#
#
# # c.Store_object_follow_list
# # c.Store_object_tweets_list
# # c.Store_object_users_list
#
# # # Run
twint.run.Search(c)
