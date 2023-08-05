# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ssh_assets',
 'ssh_assets.authorized_keys',
 'ssh_assets.bin',
 'ssh_assets.bin.ssh_assets',
 'ssh_assets.bin.ssh_assets.groups',
 'ssh_assets.bin.ssh_assets.keys',
 'ssh_assets.configuration',
 'ssh_assets.keys',
 'ssh_assets.token']

package_data = \
{'': ['*']}

install_requires = \
['cli-toolkit>=2.1.5,<3.0.0']

entry_points = \
{'console_scripts': ['ssh-assets = ssh_assets.bin.ssh_assets.main:main']}

setup_kwargs = {
    'name': 'ssh-assets',
    'version': '1.5.1',
    'description': 'SSH asset and key management tools',
    'long_description': 'None',
    'author': 'Ilkka Tuohela',
    'author_email': 'hile@iki.fi',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
