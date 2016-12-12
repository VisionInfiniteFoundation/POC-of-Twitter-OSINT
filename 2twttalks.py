import time
from TwitterAPI import TwitterAPI
consumer_key = 'eiavHcTexJq6Sw1AhMoEeH48P'
consumer_secret = '9XMCHgEtOO1xHG6zsEjuVEFrG5NDJ4way0jAu1acU5nVyXnJmI'

targetlst = []

Dangerous = []
DangerTerms = open("/root/Desktop/DangerTerms","r")
for term in DangerTerms.readlines():
	Dangerous.append(term.strip())

def tweets_by_screen_name(screen_name):
	api = TwitterAPI(consumer_key,consumer_secret,auth_type='oAuth2')
	response= api.request( 'statuses/user_timeline',{'screen_name':screen_name, 'count':20} )
	for item in response.json():
		text= item['text']
		entities= item['entities']
# entities include $symbols, @user_mentions, #hashtags, urls, media
		sym_list = [s['text'] for s in entities['symbols']]
		user_list = [u['screen_name'] for u in entities['user_mentions']]
		hash_list = [h['text'] for h in entities['hashtags']]
		url_list = [u['expanded_url'] for u in entities['urls']]
		if 'media' in entities:
			media_list = [m['media_url'] for m in entities['media']]
		else:
			media_list = []
		for terms in Dangerous:
			if text.find(terms) != -1:
				print("\n" +  item['text'], "$", sym_list, "@", user_list, hash_list, url_list, media_list)
				targetlst.append(screen_name)

varname = open("/root/Desktop/TARGET_HANDLES","r")
stlst = []
for line in varname.readlines():
	stlst.append(line.strip())
lst = set(stlst)
varname.close()

for n in lst:
	print("**************" + n)
	time.sleep(15)
	tweets_by_screen_name(n)

filename = str("Report")
rep = open(filename,"a")
for n in set(targetlst):
	rep.write(n + "\n")
