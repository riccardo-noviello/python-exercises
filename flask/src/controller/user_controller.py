from flask import render_template

class user_controller:

    def get_user():
        return render_template('index.html', title='Home')

    def post_user(username):
        if user == 'riccardo':
            user = {'username': 'riccardo'}
            messages = [
                {
                    'author': {'username': 'riccardo'},
                    'body': 'Message 1'
                },
                {
                    'author': {'username': 'riccardo'},
                    'body': 'Message 2'
                }
            ]
            return render_template('user.html', title='User Messages', user=user, messages=messages)
        else:
            return render_template('index.html', title='Home', validation="User not found!")