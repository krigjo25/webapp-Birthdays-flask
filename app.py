#   Entry point for the application

#   Importing responsories
from flask import Flask
from flask_session import Session

#   Importing custom responsories
from lib.views.birthday import Index
from lib.config.app_config import DevelopmentConfig

#   Application Configurations
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
Session(app)

@app.after_request
def after_request(response):
    """ Ensures that the responses are not cached """

    response.headers['Expires'] = 0
    response.headers['Pragma'] = "no-cache"
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    return response

#   The url rules
app.add_url_rule("/", view_func=Index.as_view(name="index.html"))

#   Run program
if __name__ == '__main__':
    app.run()
