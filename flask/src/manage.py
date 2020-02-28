from flask import Flask
from flask_script import Manager

import config

server = Flask(__name__)
server.debug = config.DEBUG

manager = Manager(server)

if __name__ == "__main__":
    manager.run()