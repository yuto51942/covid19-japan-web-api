from sanic import Blueprint, Sanic
from sanic.response import json

app = Sanic()

apiv1 = Blueprint('apiv1', url_prefix='/api/v1')


@app.route('/')
async def index(request):
    return json({'result': 'ok'})


@apiv1.route('/all')
async def all(request):
    return json({'result': 'all'})


apiv1.static('/prefectures', './data/created_json/prefectures.json', name='prefectures')


api = Blueprint.group(apiv1)
app.blueprint(api)
