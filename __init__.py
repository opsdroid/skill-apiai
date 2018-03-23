from opsdroid.matchers import match_dialogflow_action


@match_dialogflow_action('') # Matches all
async def passthrough(opsdroid, config, message):
    if "action" in message.dialogflow["result"]:
        action = message.dialogflow["result"]["action"]
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
        
        if "speech" in message.dialogflow["result"]:
            response = message.dialogflow["result"]["speech"]
        elif "speech" in message.dialogflow["result"]["fulfillment"]:
            response = message.dialogflow["result"]["fulfillment"]["speech"]

        if response:
            await message.respond(response)
