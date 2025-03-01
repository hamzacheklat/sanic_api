from sanic import Sanic
from sanic.response import json
from routes import blueprint

app = Sanic("SanicAPI")

app.blueprint(blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
