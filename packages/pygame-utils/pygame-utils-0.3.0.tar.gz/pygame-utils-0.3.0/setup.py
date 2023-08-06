# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pygame_utils']

package_data = \
{'': ['*']}

install_requires = \
['pygame>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'pygame-utils',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Nathan Strong',
    'author_email': 'nathanstrong777@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
