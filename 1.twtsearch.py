import time
from twitter import *
from TwitterAPI import TwitterAPI
consumer_key = 'eiavHcTexJq6Sw1AhMoEeH48P'
consumer_secret = '9XMCHgEtOO1xHG6zsEjuVEFrG5NDJ4way0jAu1acU5nVyXnJmI'
Access_Token = '740857079267659776-zC3go6UbtXSZRDr4sVbkDOELXrYgQ4j'
Access_Secret = 'dxfioz6l7DM829XfJzJLaUUyjuaZ9V2au6hOrUVQwhcmN'
##api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')
oauth = OAuth(Access_Token, Access_Secret, consumer_key, consumer_secret)
twitter = Twitter(auth=oauth)
flood = []
lst = []
stlst = []

var_name = open("/root/Desktop/SEARCH_TERMS","r")
for line in var_name.readlines():
	stlst.append(line.strip())
lst = set(stlst)
var_name.close()

nam = [] 
for n in lst:
	print (">>>>>>>>>>>>> Search Term : " + n + "\n")
	time.sleep(15)
	results = twitter.users.search(q = n,count = 200)
	
	for user in results:
		nam.append(user["screen_name"])



targtfl = open("TARGET_HANDLES","a")
for now in set(nam):
	targtfl.write(now + "\n")
