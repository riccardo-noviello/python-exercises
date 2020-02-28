from flask import Flask
import config
import routes

server = Flask(__name__)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
