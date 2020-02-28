from server import server
from controller import user_controller

@server.route('/', methods=['GET'])
def index():
    user_controller.get_user()


@server.route('/user', methods=['POST'])
def user():
    user_controller.post_user(flask.request.values.get('user'))

