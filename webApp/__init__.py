from flask import Flask, request

import webApp.views
import webApp.models

app = Flask(__name__)

app.register_blueprint(webApp.views.login)
app.register_blueprint(webApp.views.user)

