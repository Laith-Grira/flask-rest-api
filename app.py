from flask import Flask
from controllers import data_controller

app = Flask(__name__)

app.register_blueprint(data_controller.data_bp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)
