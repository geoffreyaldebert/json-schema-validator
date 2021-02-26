from aiohttp import web
from jsonschema import Draft7Validator
from jsonschema import validate
import requests
import json

routes = web.RouteTableDef()


@routes.post('/validate')
async def say_hello(request):

    data = await request.json()

    url = data['schema']
    response = requests.get(url)
    schemaData = json.loads(response.content)
    
    validator = Draft7Validator(schemaData)
    arr = {}
    arr['errors'] = []
    i = 0

    for error in sorted(validator.iter_errors(data["json"]), key=str):
        arr['errors'].append(str(error).split("\n")[0])
        i = 1
    if(i == 0):
        arr['valid'] = True
    else:
        arr['valid'] = False

    return web.json_response(arr, status=200)
