from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
  def __init__(self , username , password):
    self.username = username
    self.password = password
    self.bot = webdriver.Firefox()

  def login(self):
    bot=self.bot
    bot.get('https://twitter.com/login')
    time.sleep(6)   #to pause bot for miliseconds
    email=bot.find_element_by_class_name("r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1inuy60.r-utggzx.r-vmopo1.r-1w50u8q.r-1lrr6ok.r-1dz5y72.r-1ttztb7.r-13qz1uu" )
    password=bot.find_element_by_name('session[password]')
    email.clear()
    password.clear()
    email.send_keys(self.username)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(5)

  def like_tweet(self,hashtag):
    bot=self.bot
    bot.get('https://twitter.com/'+hashtag)
    time.sleep(5)
    for i in range(10):
      bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
      time.sleep(5)
      links= bot.find_element_by_class_name("css-1dbjc4n.r-1loqt21.r-16y2uox.r-1wbh5a2.r-1udh08x.r-1j3t67a.r-o7ynqc.r-6416eg")
      for link in links:
        bot.get('https://twitter.com/'+link)
        try:
          bot.find_element_by_class_name("css-1dbjc4n r-1niwhzg r-sdzlij r-1p0dtai r-xoduu5 r-1d2f490 r-xf4iuw r-u8s1d r-zchlnj r-ipm5af r-o7ynqc r-6416eg").click()
          time.sleep(10)
        except Exception as ex:
          time.sleep(60)
sel=TwitterBot('email','password')
sel.login()
sel.like_tweet('Bitcoin')
