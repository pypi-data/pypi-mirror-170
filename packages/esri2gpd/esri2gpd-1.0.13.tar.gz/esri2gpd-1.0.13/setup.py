# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esri2gpd', 'esri2gpd.tests']

package_data = \
{'': ['*']}

install_requires = \
['arcgis2geojson>=2.0.1,<3.0.0', 'geopandas>=0.6', 'requests>=2,<3']

setup_kwargs = {
    'name': 'esri2gpd',
    'version': '1.0.13',
    'description': 'Scrape features from the ArcGIS Server REST API and return a geopandas GeoDataFrame',
    'long_description': None,
    'author': 'Nick Hand',
    'author_email': 'nick.hand@phila.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0.0',
}


setup(**setup_kwargs)
