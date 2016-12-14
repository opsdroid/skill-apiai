from opsdroid.skills import match_apiai
import logging
import random

@match_apiai('smalltalk')
async def smalltalk(opsdroid, message):
    await message.respond(message.apiai.result.speech)
