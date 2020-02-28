import os

APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/application")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))