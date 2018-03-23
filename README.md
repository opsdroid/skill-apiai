# opsdroid skill Dialogflow (previously Api.ai)

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to passthrough messages from [Dialogflow](https://dialogflow.com/).

## Requirements

To enable dialogflow `parsers.dialogflow.access-token` must be set in your `configuration.yaml`.

**Example**
```yaml
parsers:
  dialogflow:
    access-token: "my_apiai_access_key"
```

## Configuration

By default this skill will reply with all responses from Dialogflow. However you can whitelist or blacklist certain actions using the `include` and `exclude` options in the configuration.

```yaml
skills:
  - name: dialogflow
    include:
      - smalltalk
    exclude:
      - smalltalk.agent
```

The above example configuration will only reply with messages from the smalltalk domain, but not the agent category.
