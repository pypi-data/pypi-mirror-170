# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hhru']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'hhru',
    'version': '0.0.1',
    'description': 'HH.ru API library for Python.',
    'long_description': 'None',
    'author': 'Kirill Zhosul',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
