import logging

import azure.functions as func
import requests

hostname = "hidden.phish.framework.domain"
key = "SECRET-KEY"

def merge_two_dicts(x, y):
    logging.info(x)
    return x | y

def set_header():
    headers = {'X-Key': key}
    return headers

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    url = f"https://{hostname}/track"

    if req.method == "GET":
        resp = requests.get(url, params=req.params, headers=merge_two_dicts(dict(req.headers), set_header()))
        return func.HttpResponse(body=resp.content, status_code=resp.status_code, mimetype=resp.headers['content-type'])
    else:
        return func.HttpResponse("Method not supported.", status_code=200)

