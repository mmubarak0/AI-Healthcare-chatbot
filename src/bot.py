#!/bin/env/python3

import os
import poe
import logging
import sys
import threading
import time

client = poe.Client(os.getenv("POE_TOKEN"))

# poe.logger.setLevel(logging.INFO)

# uncomment this for production only - Note: only one message per day is allowed for GPT-4
#model = "beaver" #GPT-4
model = "chinchilla" # ChatGPT

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class Query:
	def __init__(self, message="who are you ?"):
		self.message = message
		self.description = message
		self.age = None
		self.gender = None
		self.weight = None
		self.height = None
		self.bp = None # blood pressure
		self.hr = None # heart rate

	def set_message(self, message):
		self.message = message
		self.description = message
		return self.message

	def set_age(self, age):
		text = f"My age is: {age}"
		self.age = text
		return self.age

	def set_gender(self, gender):
		text = f"My gender type is: {gender}"
		self.gender = text
		return self.message

	def set_weight(self, weight):
		text = f"My weight is: {weight}"
		self.weight = text
		return self.weight

	def set_height(self, height):
		text = f"My height is: {height}"
		self.height = text
		return self.height

	def set_bp(self, bp):
		text = f"My blood pressure is: {bp}"
		self.bp = text
		return self.bp

	def Create(self):
		params = [self.age, self.gender, self.weight, self.height, self.bp, self.hr]
		text = []
		for value in params:
			if (value != None):
				print(value)
				text.append(str(value))
		text = ", ".join(text) + '\n'
		text += self.message
		self.message = text
		return self

	def get_message(self):
		return self.description


class Reply:
	def __init__(self, query=Query()):
		self.query = query
		self.response = None
		self.thread_count = 0

	def send(self, interactive=False):
		self.response = client.send_message(model, self.query.message, with_chat_break=True)
		print(f"{bcolors.OKCYAN}Prompt >> {bcolors.ENDC}", self.query.get_message())
		if (interactive == True):
			for i in self.response:
				print(i["text_new"], end="", flush=True)
		else:
			for i in self.response:
				pass
			print(i["text"])
		print()
		self.purge()

	# handle multiple users
	def message_thread(self, desc, prompt, counter):
		for i in client.send_message(model, prompt, with_chat_break=True):
			pass
		print(f"{bcolors.OKCYAN}Prompt >> {bcolors.ENDC}", end="")
		print(desc+"\n"+i["text"]+"\n"+"-"*100+"\n")
		self.thread_count -= 1

	def send_multiple(self, *queries):
		for i in range(len(queries)):
			t = threading.Thread(target=self.message_thread, args=(queries[i].get_message(), queries[i].message, i), daemon=True)
			t.start()
			self.thread_count += 1
		
		while self.thread_count:
			time.sleep(0.1)

		print()
		self.purge()

	def purge(self):
		client.purge_conversation(model)

if __name__ == "__main__":
	############## 
	# Test Cases #
	##############

	# Query will build the message
	text = "I have headache and some pain on my neck"
	ki2kid = Query(text)
	ki2kid.set_age(22)
	ki2kid.set_gender("male")

	text2 = "I can't see clearly"
	mano = Query(text2)
	mano.set_age(15)
	mano.set_gender("male")

	# Create the message
	ki2kid.Create()
	mano.Create()

	# Reply takes a Query and return a response
	answer = Reply(ki2kid)
	answer.send(interactive=True)
	answer.send_multiple(ki2kid, mano)
