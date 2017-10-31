# opsdroid skill api.ai

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to passthrough messages from [api.ai](https://api.ai).

## Requirements

To enable api.ai `parsers.apiai.access-token` must be set in your `configuration.yaml`.

**Example**
```yaml
parsers:
  apiai:
    access-token: "my_apiai_access_key"
```

## Configuration

By default this skill will reply with all responses from api.ai. However you can whitelist or blacklist certain actions using the `include` and `exclude` options in the configuration.

```yaml
skills:
  - name: apiai:
    include:
      - smalltalk
    exclude:
      - smalltalk.agent
```

The above example configuration will only reply with messages from the smalltalk domain, but not the agent category.
