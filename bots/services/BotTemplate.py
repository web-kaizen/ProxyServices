import json

import requests
from common.Route import Route
from rest_framework.request import Request


class BotTemplate(Route):

    def __init__(self, request: Request) -> None:
        super().__init__(request=request)

    def send(self, endpoint: str) -> requests.Response:
        yadro_response = super().send(endpoint=endpoint)
        response = self.__add_additional_fields_to_response(response=yadro_response)
        return response

    @staticmethod
    def __add_additional_fields_to_response(response: requests.Response) -> requests.Response:
        fields_to_add = {
            'bot_name': 'ChatGPT',
            'model_name': 'Gpt-3.5',
            'mode_name': '4k context'
        }
        content = {'result': []}
        for obj in response.json()['result']:
            obj.update(fields_to_add)
            content['result'].append(obj)

        response._content = json.dumps(content).encode('utf-8')
        response.headers.pop('Content-Length')

        return response
