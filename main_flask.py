from flask import Flask
from Subapp.task1_flask import flask1
from Subapp.task4_flask import taskfour

app = Flask(__name__)

app.register_blueprint(flask1)
app.register_blueprint(taskfour)
