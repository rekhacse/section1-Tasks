import urllib2, json, sqlite3
wFD = urllib2.urlopen('http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Twitter_2013_11_12.txt')
blankLines = 0
goodLines = 0
numLines = 10000
while numLines > 0:
    line = wFD.readline()
    numLines = numLines - 1
    try:
         tweets.append(json.loads(line))
         goodLines = goodLines+1
    except:
        blankLines = blankLines + 1
blankLines
goodLines


#loading tweets using json and storing it as one big entry in table in database using SQLite3


SingleTable = """Create table SingleTable(tweet varchar(8038));"""
c.execute("drop table if exists SingleTable")
c.execute(SingleTable)

len_strTwt = 0
for tweet in tweets:
    str_tweet = str(tweet)
    c.execute("insert into SingleTable values (?)", (str_tweet,))
    if len_strTwt < len(str_tweet):
        len_strTwt = len(str_tweet)
len_strTwt
