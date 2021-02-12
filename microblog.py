from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':

    # force using PyCharm's debugger
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)

    # use Flask's native debugger
    # app.run(debug=True)
