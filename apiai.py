from opsdroid.skills import match_apiai_action

@match_apiai_action('') # Matches all
async def passthrough(opsdroid, message):
    if "action" in message.apiai["result"]:
        action = message.apiai["result"]["action"]

        try:
            if "include" in opsdroid.config["skills"]["apiai"]:
                includes = opsdroid.config["skills"]["apiai"]["include"]
                if True not in [x in action for x in includes]:
                    return
        except TypeError:
            pass

        try:
            if "exclude" in opsdroid.config["skills"]["apiai"]:
                excludes = opsdroid.config["skills"]["apiai"]["exclude"]
                if True in [x in action for x in excludes]:
                    return
        except TypeError:
            pass

        if message.apiai["result"]["speech"]:
            await message.respond(message.apiai["result"]["speech"])
