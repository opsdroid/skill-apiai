from opsdroid.skills import match_apiai
import logging
import random

@match_apiai('smalltalk')
async def smalltalk(opsdroid, message):
    if message.apiai["result"]["speech"]:
        await message.respond(message.apiai["result"]["speech"])
