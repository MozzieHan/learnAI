from sanic import Sanic
from sanic.response import text, json


app = Sanic()

@app.route("/")
async def index(request):
    return text("hello moz")

@app.route("/json/")
async def index_json(request):
    return json({"hello": "moz"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000)

