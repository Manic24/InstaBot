  
from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("ns160.jpg", caption="Bike")

######  follow someone #######
bot.follow("elonrmuskk")

######  send a message #######
bot.send_message("Hello from Manish", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("_mxnigxndxn_")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()