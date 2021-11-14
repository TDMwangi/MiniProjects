from instabot import Bot

bot = Bot()

bot.login(username="usr", password="pwd")

bot.upload_photo("image.jpg", caption="Image upload")
