import os
import json
from datetime import datetime

class loadData:

	def __init__(self, username):
		self.username = username
		self.DefaultAccountDataContents = {
				"Name":	'',
				"AccountCreated": '',
				"LastLogin": ''
		}
		try:
			# Does account exist?
			self.AccountDataFile = open("data/%s/%s.json" % (self.username, self.username), "r")
			self.AccountDataFile.close()
		except:
			# Instead of making an account, we could simply return an account not found message
			os.makedirs('data/%s' % self.username)
			self.AccountDataFile = open("data/%s/%s.json" % (self.username, self.username), "w")
			self.DefaultAccountDataContents["Name"] = self.username
			self.DefaultAccountDataContents["AccountCreated"] = str(datetime.now())
			json.dump(self.DefaultAccountDataContents, self.AccountDataFile, indent=4)
			self.AccountDataFile.close()

		#self.updateLoginTime()

	def loadPirate(self, pirateID):
		
		print self.AccountData["Name"]

	def updateLoginTime(self):
		self.AccountDataFile = open("data/%s/%s.json" % (self.username, self.username), "r+")
		self.AccountDataContents = json.load(self.AccountDataFile)
		self.AccountDataContents["LastLogin"] = str(datetime.now())
		json.dump(self.AccountDataContents, self.AccountDataFile, indent=4)