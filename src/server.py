#!/usr/bin/python3

import os
import argparse
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()
parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, help='port do servidor')
parser.add_argument('netfile', type=str, help='arquivo de redes')
parser.add_argument('ixfile', type=str, help='arquivo de IXPs')
parser.add_argument('netixlanfile', type=str, help='arquivo de associacoes')

args = parser.parse_args()

net = {}
ix = {}
netixlan = {}

with open(args.netfile, 'r') as f:
    net = f.read()

with open(args.ixfile, 'r') as f:
    ix = f.read()

with open(args.netixlanfile, 'r') as f:
    netixlan = f.read()

@app.route('/test')
def test():
    return 'test'

# declarar as rotas para o servidor
@app.route('/api/ix')
def ixps():
    pass

@app.route('/api/ixnets/<ix_id>')
def ixp_ids(ix_id):
    pass

@app.route('/api/netname/<net_id>')
def net_name(net_id):
    pass

app.run(host='0.0.0.0', port=args.port)