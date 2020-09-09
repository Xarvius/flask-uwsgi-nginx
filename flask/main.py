from app import app
from config import Config
from flask_bootstrap import Bootstrap

app.config.from_object(Config)
Bootstrap(app)

if __name__ == "__main__":
    app.run(debug=True)