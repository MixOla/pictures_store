import base64
import io
from urllib.parse import urljoin

import requests
from django.core.files.base import ContentFile


class GenerateImageHandler:
    class Endpoint:
        INITIATE = "/initiate_processing"
        CHECK_STATUS = "/check_status"
        GET_RESULTS = "/get_results"

    def __init__(
        self,
        imgs=None,
        n=1,
        height=512,
        width=512,
        steps=50,
        scale=7.5,
        seed=None,
        desc=False,
        cpu=False,
    ):
        self.imgs = imgs
        self.n = n
        self.height = height
        self.width = width
        self.steps = steps
        self.scale = scale
        self.seed = seed
        self.desc = desc
        self.imgs = imgs
        self.cpu = cpu
        self.host = "http://208.51.60.18:2020/"

    def initiate_processing(
        self,
        prompt,
        neg_prompt="",
    ):
        params = {
            "prompt": prompt,
            "neg_prompt": neg_prompt,
            "imgs": self.imgs,
            "n": self.n,
            "height": self.height,
            "width": self.width,
            "steps": self.steps,
            "scale": self.scale,
            "seed": self.seed,
            "desc": self.desc,
            "cpu": self.cpu,
        }
        url = urljoin(self.host, self.Endpoint.INITIATE)
        response = requests.post(url, json=params)
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError(
                "Error! " + str(response.status_code) + " " + response.text
            )

    def check_status(self, order_id):
        params = {"id": order_id}
        url = urljoin(self.host, self.Endpoint.CHECK_STATUS)
        response = requests.post(url, json=params)
        if response.status_code == 200:
            return response.text
        else:
            raise ValueError(
                "Error! " + str(response.status_code) + " " + response.text
            )

    def get_results(self, order_id):
        params = {"id": order_id}
        url = urljoin(self.host, self.Endpoint.GET_RESULTS)
        response = requests.post(url, json=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(
                "Error! " + str(response.status_code) + " " + response.text
            )

    def decode_img(self, raw_img):
        decoded = base64.b64decode(raw_img)
        return ContentFile(decoded, name="prompt.png")
