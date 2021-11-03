from flask import Flask, render_template, request
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

app = Flask(__name__)
metrics = GunicornInternalPrometheusMetrics(app)
# # static information as metric
metrics.info('app_info', 'FrontEnd info', version='1.0.3')

@app.route('/')
def homepage():
    return render_template("main.html")


if __name__ == "__main__":
    app.run()