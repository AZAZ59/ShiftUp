import flask_profiler

from Client.app import app

"""
app.config["DEBUG"] = True


app.config["flask_profiler"] = {
    "verbose": True,
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth": {
        "enabled": True,build"
        "username": "admin",
        "password": "admin"
    }
}
"""

# flask_profiler.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
