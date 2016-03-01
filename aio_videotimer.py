import requests
from aiohttp import web


async def send_to_hub(request):
    # logging.debug("activating scene {}".format(scene_id))
    scene_id = request.match_info.get('scene_id', '')
    requests.get('http://192.168.0.106/api/scenes?sceneid={}'.format(scene_id))
    return web.Response(body=b"succeeded")


app = web.Application()

app.router.add_route('GET', '/hub/{scene_id}', send_to_hub)
app.router.add_static("/static/", "static/")

if __name__ == "__main__":
    web.run_app(app)
