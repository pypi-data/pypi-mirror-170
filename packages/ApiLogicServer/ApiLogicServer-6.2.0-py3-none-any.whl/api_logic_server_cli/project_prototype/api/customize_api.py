import logging

import util
from typing import List

import safrs
import sqlalchemy
from flask import request, jsonify
from safrs import jsonapi_rpc, SAFRSAPI
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import object_mapper

from database import models

from logic_bank.rule_bank.rule_bank import RuleBank

# called by api_logic_server_run.py, to customize api (new end points, services).
# separate from expose_api_models.py, to simplify merge if project recreated

app_logger = logging.getLogger("api_logic_server_app")


def expose_services(app, api, project_dir, swagger_host: str, PORT: str):
    """ Customize API - new end points for services """
    
    app_logger.debug("api/customize_api.py - expose custom services")

    @app.route('/hello_world')
    def hello_world():  # test it with: http://api_logic_server_host:api_logic_server_port/hello_world?user=ApiLogicServer
        """
        This is inserted to illustrate that APIs not limited to database objects, but are extensible.

        See: https://valhuber.github.io/ApiLogicServer/API-Customize/

        See: https://github.com/thomaxxl/safrs/wiki/Customization
        """
        user = request.args.get('user')
        return jsonify({"result": f'hello, {user}'})


    @app.route('/server_log')
    def server_log():
        """
        Used by test/api_logic_server_behave/features/steps/test_utils.py - enables client app to log msg into server

        Special support for the msg parameter -- Rules Report
        """
        return util.server_log(request, jsonify)