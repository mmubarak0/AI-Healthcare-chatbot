#!/bin/env/python3
from bot import Query, Reply

mubarak = Query("I have a headache on the left side of my head with some pain on the upper left part of my neck")
mubarak.set_param("age", 22)
mubarak.set_param("gender", "male")


while (True):
	print("Describe you problem")
	mubarak.set_message(input())
	Reply(mubarak.create_message()).send(interactive=True)
