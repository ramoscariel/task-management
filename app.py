from flask import Flask
from controllers.task_controller import task_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)