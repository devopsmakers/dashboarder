from flask import redirect, Blueprint
from werkzeug.contrib.cache import SimpleCache

import os
import sys
import random
import yaml

cache = SimpleCache()
appbp = Blueprint("appbp", __name__, url_prefix=os.environ.get("URL_PREFIX"))


def get_config():
    """Safely returns the config YAML as a Python dict"""
    with open("config.yml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            sys.exit(e)


def get_dashboards():
    """Safely returns the dashboard urls YAML as a Python dict"""
    with open("dashboards.yml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except Exception as e:
            sys.exit(e)


def get_dashboard_url():
    """Return the dashboard_url and manage the next url"""
    config = get_config()
    dashboards = get_dashboards()

    dashboard_url = cache.get("dashboard_url")
    next_dashboard_url = cache.get("next_dashboard_url")

    if dashboard_url is None and next_dashboard_url is None:
        cache.set("next_dashboard_url", dashboards["urls"][0])
        next_dashboard_url = cache.get("next_dashboard_url")

    if dashboard_url is None:
        cache.set("dashboard_url", cache.get("next_dashboard_url"),
                  timeout=config["ttl"])
        dashboard_url = cache.get("dashboard_url")

        if config["sort"] == "random":
            next_url = random.choice(dashboards["urls"])
            while next_dashboard_url == next_url:
                next_url = random.choice(dashboards["urls"])
        else:
            url_list = dashboards["urls"]
            curr_idx = url_list.index(dashboard_url)
            next_url = url_list[(curr_idx + 1) % len(url_list)]

        cache.set("next_dashboard_url", next_url)

    return dashboard_url


@appbp.route("/")
def index():
    """returns a 302 redirect to a url from dashboards.yml"""
    return redirect(get_dashboard_url(), code=302)


@appbp.route("/ping")
def ping():
    """ping endpoint for SD / aliveness checks"""
    return "pong"
