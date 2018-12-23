from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pandas as pd

access_token = "810489185861824512-sa6J6p1RAaolOFcLh1TOPmuOP9XHmDM"
access_token_secret = "zczOpmqn2vpzIg68XuKhXQgXzE4nMhuJGTu1gGugyV6Mv"
consumer_key = "mYh1sti2PMGKmiU0C8pPLbGGl"
consumer_secret = "0Kf8DNw8HklsHnINLGOPRryZMo3EvSCJvIL0Edh9JKS6ShCfx1"

class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            #data = data.encode('utf-8')
            #data = data.decode('unicode_escape')
            print(data)
        except:
            pass
        return True

    def on_error(self, status):
         print('error:', status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #stream.filter(track=['python', 'javascript', 'ruby'])
    
    
    raw_words = pd.read_csv('../data/twitter_filter/twt_filter_10.csv', header = 0, quoting=3, encoding='cp949',
                            error_bad_lines=False)
    raw_words = raw_words['words']
    values = raw_words.values;
    
    filter_words=[]
    for word in values:
        filter_words.append(word[0])
    
    stream.filter(track=filter_words)
