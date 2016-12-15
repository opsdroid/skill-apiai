from opsdroid.skills import match_apiai
import logging
import random

@match_apiai('')
async def passthrough(opsdroid, message):
    if "action" in message.apiai["result"]:
        if "include" in opsdroid.config["skills"]["apiai"]:
            includes = opsdroid.config["skills"]["apiai"]["include"]
            action = message.apiai["result"]["action"]
            if True not in [x in action for x in includes]:
                return

        if "exclude" in opsdroid.config["skills"]["apiai"]:
            excludes = opsdroid.config["skills"]["apiai"]["exclude"]
            action = message.apiai["result"]["action"]
            if True in [x in action for x in excludes]:
                return

        if message.apiai["result"]["speech"]:
            await message.respond(message.apiai["result"]["speech"])
