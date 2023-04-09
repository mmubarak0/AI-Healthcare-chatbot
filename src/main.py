#!/bin/env/python3
from bot import Query, Reply

mubarak = Query("I have a headache on the left side of my head with some pain on the upper left part of my neck")
mubarak.set_age = 22
mubarak.set_gender = "male"
Reply(mubarak.Create()).send(interactive=True)


while (True):
	print("Describe you problem")
	mubarak.set_message(input())
	Reply(mubarak.Create()).send(interactive=True)
#mubarak.set_message("I think my left arm is broken")
#Reply(mubarak.Create()).send(interactive=True)
