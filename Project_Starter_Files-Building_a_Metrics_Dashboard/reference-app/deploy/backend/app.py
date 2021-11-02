from flask import Flask, render_template, request, jsonify

from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

# from jaeger_client import Config
# from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
# from opentelemetry import trace
# from opentelemetry.exporter import jaeger
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
# from opentelemetry.instrumentation.flask import FlaskInstrumentor
# from opentelemetry.instrumentation.requests import RequestsInstrumentor
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import (
#     ConsoleSpanExporter,
#     SimpleExportSpanProcessor,
# )

# trace.set_tracer_provider(TracerProvider())
# trace.get_tracer_provider().add_span_processor(
#     SimpleExportSpanProcessor(ConsoleSpanExporter())
# )

# app = Flask(__name__)
# FlaskInstrumentor().instrument_app(app)
# RequestsInstrumentor().instrument()


# import pymongo
# from flask_pymongo import PyMongo

app = Flask(__name__)
metrics = GunicornInternalPrometheusMetrics(app)
# static information as metric
metrics.info('app_info', 'Backend info', version='1.0.3')

# app.config['MONGO_DBNAME'] = 'example-mongodb'
# app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

# mongo = PyMongo(app)

# def init_tracer(service):
#     logging.getLogger('').handlers = []
#     logging.basicConfig(format='%(message)s', level=logging.DEBUG)

#     config = Config(
#         config={
#             'sampler': {
#                 'type': 'const',
#                 'param': 1,
#             },
#             'logging': True,
#         },
#         service_name=service,
#     )

#     # this call also sets opentracing.tracer
#     return config.initialize_tracer()

# tracer = init_tracer('first-service')

@app.route('/')
def homepage():
    # with tracer.start_span('get-python-jobs') as span:
    #     homepages = []
    #     res = requests.get('https://jobs.github.com/positions.json?description=python')
    #     span.set_tag('first-tag', len(res.json()))
    #     for result in res.json():
    #         try:
    #             homepages.append(requests.get(result['company_url']))
    #         except:
    #             return "Unable to get site for %s" % result['company']

    return "Hello World"


@app.route('/api')
def my_api():
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
