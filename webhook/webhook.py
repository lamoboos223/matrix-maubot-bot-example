from maubot import Plugin, MessageEvent
from maubot.handlers import command
import requests
import json


url = 'https://webhook.site/623804e2-c11e-4440-b8bd-805095f8474e'
payload = {
    'greeting': 'Hello, world!'
}
json_payload = json.dumps(payload)
headers = {
    'Content-Type': 'application/json'
}

class WebhookBot(Plugin):
    async def start(self) -> None:
        await super().start()

    @command.new(
        name="webhook_lama", help="hit webhook",
        arg_fallthrough=False, require_subcommand=False
    )

    async def weather_handler(self, evt: MessageEvent) -> None:
        response = requests.post(url, data=json_payload, headers=headers)
        response = json.dumps({
            "greeting": "hello, world!"
        })
        await evt.respond(response)
