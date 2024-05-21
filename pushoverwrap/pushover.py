import requests
import json
import os


class Pushover:
    URL = 'https://api.pushover.net/1/messages.json'

    def __init__(self, app_token, user_token):
        self.app_token = app_token
        self.user_token = user_token

    def send_msg(self, message, image=None, **kwargs):
        valid_params = {
            'callback',
            'device',
            'expire',
            'html',
            'monospace',
            'priority',
            'retry',
            'sound',
            'timestamp',
            'title',
            'ttl',
            'url',
            'url_title',
        }
        data = {
            'token': self.app_token,
            'user': self.user_token,
            'message': message,
        }

        # Validate kwargs
        invalid_params = set(kwargs) - valid_params
        if invalid_params:
            raise ValueError(f'Invalid parameters: {invalid_params}')

        data.update(kwargs)

        # image as attachment
        if image:
            with open(image, 'rb') as img_data:
                filename = os.path.basename(image)
                filetype = f'image/{os.path.splitext(filename)[1][1:]}'
                response = requests.post(
                    self.URL,
                    data=data,
                    files={'attachment': (filename, img_data, filetype)},
                )
        else:
            response = requests.post(self.URL, data=data)

        rsp = response.json()

        return rsp['status'] == 1, rsp
