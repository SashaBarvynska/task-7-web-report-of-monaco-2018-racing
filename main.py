import src.routes
from config import Config
from src.app import app

if __name__ == '__main__':
    app.config.from_object(Config).run()
