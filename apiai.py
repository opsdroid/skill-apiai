from opsdroid.skills import match_apiai

@match_apiai('') # Matches all
async def passthrough(opsdroid, message):
    if "action" in message.apiai["result"]:
        action = message.apiai["result"]["action"]

        if "include" in opsdroid.config["skills"]["apiai"]:
            includes = opsdroid.config["skills"]["apiai"]["include"]
            if True not in [x in action for x in includes]:
                return

        if "exclude" in opsdroid.config["skills"]["apiai"]:
            excludes = opsdroid.config["skills"]["apiai"]["exclude"]
            if True in [x in action for x in excludes]:
                return

        if message.apiai["result"]["speech"]:
            await message.respond(message.apiai["result"]["speech"])
