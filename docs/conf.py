"""Sphinx config."""

import requests

copyright = "@webknjaz"
html_theme = 'furo'
project = 'Lokiverse'


def _identify_py38_eol_date():
    py38_lifecycle_details = requests.get(
        'https://endoflife.date/api/python/3.8.json',
        headers={'Accept': 'application/json'},
        timeout=5,
    )
    return py38_lifecycle_details.json()['eol']


def setup(app):
    app.config.rst_epilog = f"""
    .. |py38_eol_date| replace:: {_identify_py38_eol_date()}
    """
