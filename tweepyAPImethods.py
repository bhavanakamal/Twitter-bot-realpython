import tweepy

#Authenticate to twitter
auth = tweepy.OAuthHandler("czgFrUnvkUDdn2htfANyzfNV4", "GNnwMsjmgUOwIoLl6pCysLck52syfdGP4biB3g4FyQ6cSZX5Un")
auth.set_access_token("1276863422836035586-IvKNzOs0yfNGO7eVw5q0pTOf3TF9fl", "qMu9PDudPpMxL8dEDPcIQqlvry2mKrK5eFSAi36EQYJPk")

#Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    

try:
	api.verify_credentials()
	print("Authentication OK")
except:
    print("Error during authentication")


#Methods for User Timelines
timeline = api.home_timeline()

print("TIMELINE is: ", timeline)
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")


#Methods for Tweets
#api.update_status("Test tweet from Tweepy Python")

#Methods for Users

# user = api.get_user("subodh_sah")
# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)
#
# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)
# #
# #
# #Methods for Followers
# #print("ENTERS CREATE FRIENDSHIP")
# api.create_friendship("realpython")
# #
# #Methods for Likes
# tweets = api.home_timeline(count=1)
# #print("TWEETS are: ", tweets[0])
# tweet = tweets[0]
# print(f"Liking tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)
# #
# #Methods for Trends
# trends_result = api.trends_place(1)
# #print("TRENDS_RESULT ARE: ", trends_result[0]["trends"])
# for trend in trends_result[0]["trends"]:
#     print(trend["name"])

trends_result_available = api.trends_available()
print("available locations: ",trends_result_available )

#Methods for Your Account
#api.update_profile(description="I like learning new tech skills")

#Methods for Blocking Users
# for block in api.blocks():
#     print(block.name)

#Methods for Searches
# for tweet in api.search(q="Python", lang="en", rpp=10):
#     print(f"{tweet.user.name}:{tweet.text}")








