from flask import Flask
from controllers.task_controller import task_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprint
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)