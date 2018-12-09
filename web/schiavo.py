import requests
from urllib.parse import urlencode
from random import randint
from common.akatsuki.discord_hooks import Webhook
from objects import glob

class schiavo:
	"""
	Schiavo Bot class
	"""
	def __init__(self, botURL=None, prefix="", maxRetries=20):
		"""
		Initialize a new schiavo bot instance

		:param botURL: schiavo api url. oepsie i changed this a lot.
		:param maxRetries: max retries if api request fail. 0 = don't retry.
		"""
		self.maxRetries = 20

	def sendMessage(self, message, botURL, customParams=""):
		"""
		Send a generic message through schiavo api

		:param channel: api channel.
		:param message: message content.
		:param customParams: Let all hell break loose
		:return:

		Let's call it 50% spaghetti code.. Deal..?
		"""

		if botURL is None:
			return
		else:
			embed = Webhook(botURL, color=randint(100000, 999999))
			if customParams == "":
				embed.set_author(name='cmyui\'s schiavo', icon='https://a.akatsuki.pw/999', url="http://akatsuki.pw/")
				#embed.set_image('https://i.namir.in//bTr.png')
				embed.set_title(title="Logging Utility")
				embed.add_field(name=message, value='** **')
			elif customParams[0] == "sendMapRequest":
				"""
				:customParams: passed from command

				1 = fro
				2 = userID
				3 = beatmapset_id
				4 = song_name
				5 = mapID
				6 = rankType
				7 = mapType
				8 = gameMode
				"""
				embed.set_author(name=customParams[1], icon='http://a.akatsuki.pw/{}'.format(customParams[2]), url="http://akatsuki.pw/u/{}".format(customParams[2]))
				embed.set_image('https://assets.ppy.sh/beatmaps/{}/covers/cover.jpg?1522396856'.format(customParams[3]))
				embed.set_title(title="{}".format(customParams[4]), url="http://akatsuki.pw/b/{}".format(customParams[5]))
				embed.set_footer(text='requested for {}ed on'.format(customParams[6], icon='https://i.namir.in/SXJisKLwL.png', ts=True))
				embed.add_field(name='This **{}** has been requested for **{}ed** by {} for gamemode {}.'.format(customParams[7], customParams[6], customParams[1], customParams[8]), value='** **')

			elif customParams[0] == "sendMapRequestAccepted":
				"""
				:customParams: passed from command

				1 = fro
				2 = userID
				3 = beatmapset_id
				4 = song_name
				5 = mapID
				6 = rankType
				7 = mapType
				8 = gameMode
				"""
				embed.set_author(name=customParams[1], icon="http://a.akatsuki.pw/{}".format(customParams[2]), url="http://akatsuki.pw/u/{}".format(customParams[2]))
				embed.set_image('https://assets.ppy.sh/beatmaps/{}/covers/cover.jpg?1522396856'.format(customParams[3]))
				embed.set_title(title="{}".format(customParams[4]), url="http://akatsuki.pw/b/{}".format(customParams[5]))
				embed.set_footer(text='{}ed on'.format(customParams[6]), icon='https://i.namir.in/SXJisKLwL.png', ts=True)
				embed.add_field(name='This {} has been **{}ed** on gamemode {}'.format(customParams[7], customParams[6], customParams[8]), value='** **')
			else:
				return "how do u manage this. u specified to use customParams but didnt specify a valid [0] u retard"

			#elif customParams == "userAchieveFirstPlace":

		for _ in range(0, self.maxRetries):
			try:
				embed.post()
				break
			except requests.RequestException:
				continue


	def sendConfidential(self, message):
		"""
		Send a message to #bunk

		:param message: message content.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['confidential']
		self.sendMessage(message, botURL)

	def sendStaff(self, message):
		"""
		Send a message to #staff

		:param message: message content.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['staff']
		self.sendMessage(message, botURL)

	def sendGeneral(self, message):
		"""
		Send a message to #general

		:param message: message content.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['general']
		self.sendMessage(message, botURL)

	def sendChatlog(self, message):
		"""
		Send a message to #chatlog.

		:param message: message content.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['chatlog']
		self.sendMessage(message, botURL)

	def sendCM(self, message):
		"""
		Send a message to #communitymanagers

		:param message: message content.
		:return:
		"""
		botURL = glob.conf.config['webhooks']['cm']
		self.sendMessage(message, botURL)