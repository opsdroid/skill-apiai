from opsdroid.matchers import match_apiai_action

@match_apiai_action('') # Matches all
async def passthrough(opsdroid, config, message):
    if "action" in message.apiai["result"]:
        action = message.apiai["result"]["action"]
        response = None

        try:
            if "include" in config:
                includes = config["include"]
                if True not in [x in action for x in includes]:
                    return
        except TypeError:
            pass

        try:
            if "exclude" in config:
                excludes = config["exclude"]
                if True in [x in action for x in excludes]:
                    return
        except TypeError:
            pass
        
        if "speech" in message.apiai["result"]:
            response = message.apiai["result"]["speech"]
        elif "speech" in message.apiai["result"]["fulfillment"]:
            response = message.apiai["result"]["fulfillment"]["speech"]

        if response:
            await message.respond(response)
