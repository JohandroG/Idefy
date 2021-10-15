from idefy_app import app
from idefy_app.controllers import users_controller
from idefy_app.controllers import categories_controller
from idefy_app.controllers import ideas_controller


if __name__ == "__main__":
    app.run( debug = True )
