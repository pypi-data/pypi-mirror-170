# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['random']
install_requires = \
['Moe>=0.15.3,<0.16.0']

entry_points = \
{'console_scripts': ['moe = moe.cli:main'], 'moe.plugins': ['random = random']}

setup_kwargs = {
    'name': 'moe-random',
    'version': '0.1.1',
    'description': 'Plugin for moe to output a random item from your music library.',
    'long_description': '# moe_random\nAdds a `random` command to Moe to output a random item from your library.\n',
    'author': 'Jacob Pavlock',
    'author_email': 'jtpavlock@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MoeMusic/moe_random',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
