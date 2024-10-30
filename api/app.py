from flask import Flask
from api.routes import feedback, inference

app = Flask(__name__)
app.register_blueprint(feedback.bp)
app.register_blueprint(inference.bp)

if __name__ == "__main__":
    app.run(debug=True)
