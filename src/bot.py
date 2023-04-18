#########
#!/bin/env/python3

import os
import poe
import threading
import time
import logging

client = poe.Client(os.getenv("POE_TOKEN"))

# poe.logger.setLevel(logging.INFO)

# Uncomment this for production only - Note: only one message per day is allowed for GPT-4
# model = "beaver" # GPT-4
model = "chinchilla"  # ChatGPT

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
	    	self.params = {}
	
	def set_message(self, message):
		self.message = message
		self.description = message
		return self.message
	
	def set_param(self, key, value):
		text = f"My {key} is: {value}"
		self.params[key] = text
	
	def create_message(self):
		text = []
		for value in self.params.values():
			text.append(value)
		text.append(self.message)
		self.message = ", ".join(text) + '\n'
		return self
	
	def get_message(self):
		return self.description


class Reply:
	def __init__(self, query=Query()):
		self.query = query
		self.response = None
		self.thread_count = 0
	
	def send(self, interactive=False):
		self.response = client.send_message(model, self.query.message, with_chat_break=False)
		print(f"{bcolors.OKCYAN}Prompt >> {bcolors.ENDC}", self.query.get_message())
		if interactive:
			for i in self.response:
				print(i["text_new"], end="", flush=True)
		else:
			for i in self.response:
				pass
			print(i["text"])
		print()
		return (i["text"])
	
	def message_thread(self, desc, prompt, counter):
		for i in client.send_message(model, prompt, with_chat_break=True):
			pass
		print(f"{bcolors.OKCYAN}Prompt >> {bcolors.ENDC}", end="")
		print(desc + "\n" + i["text"] + "\n" + "-" * 100 + "\n")
		self.thread_count -= 1
	
	def send_multiple(self, *queries):
		for query in queries:
			t = threading.Thread(target=self.message_thread, args=(query.get_message(),
						query.message, self.thread_count), daemon=True)
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
	ki2kid.set_param("age", 22)
	ki2kid.set_param("gender", "male")
	
	text2 = "I can't see clearly"
	mano = Query(text2)
	mano.set_param("age", 15)
	mano.set_param("gender", "male")
	
	# Create the message
	ki2kid.create_message()
	# Reply takes a Query and return a response
	answer = Reply(ki2kid)
	rep = answer.send(interactive=True)
	print(rep)
