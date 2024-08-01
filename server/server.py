import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from apis.trending_resource import *
from apis.today_resource import *
from apis.realtime_resource import *
from apis.suggestions_resource import *
from apis.countries_resource import *
from apis.filter_resource import *
from flask_apscheduler import APScheduler
from dotenv import load_dotenv
from database.db_utils import create_schema
from database.google_trends.countries import add_country_from_file
from tasks import *



def create_app():
    app = Flask(__name__)
    app.config['SCHEDULER_API_ENABLED'] = True
    CORS(app)

    api = Api(app)
    api.add_resource(Trending, '/trending')
    api.add_resource(Realtime, '/realtime')
    api.add_resource(Today, '/today')
    api.add_resource(Suggestion, '/suggestion')
    api.add_resource(Countries, '/countries')
    api.add_resource(Filter, '/filter')


    scheduler = APScheduler()
    scheduler.add_job(id='1', func=store_and_send_searches, trigger='cron', minute='00', second='01')
    scheduler.add_job(id='2', func=send_diagnostic_email, trigger='cron', minute='30')
    scheduler.add_job(id='3', func=send_diagnostic_email, trigger='cron', minute='45')
    scheduler.start()

    return app


if __name__ == '__main__':
    create_schema()
    add_country_from_file()
    app = create_app()
    load_dotenv()
    app.run(debug=False, host=os.getenv('HOST'), port=5000, threaded=True)
