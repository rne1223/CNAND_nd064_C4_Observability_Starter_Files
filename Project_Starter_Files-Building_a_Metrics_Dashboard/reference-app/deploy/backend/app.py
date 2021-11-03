from flask import Flask, render_template, request, jsonify
import logging

from os import getenv
JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')

from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from jaeger_client import Config
from flask_opentracing import FlaskTracing
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


# import pymongo
# from flask_pymongo import PyMongo

app = Flask(__name__)
metrics = GunicornInternalPrometheusMetrics(app)
# static information as metric
metrics.info('app_info', 'Backend info', version='1.0.3')

config = Config(
    config={ 'sampler': {'type': 'const', 'param': 1},
            'logging': True,
            'reporter_batch_size': 1,}, 
            service_name="backend")

jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)
# app.config['MONGO_DBNAME'] = 'example-mongodb'
# app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

# mongo = PyMongo(app)

def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    # config = Config(config={'logging': True}, service_name=service, validate=True)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'local_agent':{'reporting_host': JAEGER_HOST},
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('backend')

@app.route('/')
@endpoint_counter
def homepage():
    with tracer.start_span('homepage'):
        hello = "Hello world"

    return hello 


@app.route('/api')
@endpoint_counter
def my_api():
    with tracer.start_span('api'):
        answer = "something"

    return jsonify(repsonse=answer)

# @app.route('/star', methods=['POST'])
# def add_star():
#   star = mongo.db.stars
#   name = request.json['name']
#   distance = request.json['distance']
#   star_id = star.insert({'name': name, 'distance': distance})
#   new_star = star.find_one({'_id': star_id })
#   output = {'name' : new_star['name'], 'distance' : new_star['distance']}
#   return jsonify({'result' : output})

if __name__ == "__main__":
    app.run()
