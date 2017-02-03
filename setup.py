"""
Flask-Plugins
-------------

Flask-Plugins makes it possible, to create plugins for your
application. In addition to the plugin system, it also provides a simple
event system which can be used by plugins to extend your application without
the need to modify your core code.


And Easy to Setup
`````````````````

First of all, you have to install it:

.. code:: bash

    $ pip install flask-plugins

and then you need to initialize it somewhere in your code.

.. code:: python

    from spotipo_plugins import PluginManager

    plugin_manager = PluginManager(app)

Want to use the factory pattern? No problem!

.. code:: python

    from spotipo_plugins import PluginManager

    plugin_manager = PluginManager()
    plugin_manager.init_app(app)

Resources
`````````

* `source <ttps://github.com/Nibblecomm/spotipo-plugins>`_
* `docs <https://flask-plugins.readthedocs.org/en/latest>`_
* `issues <ttps://github.com/Nibblecomm/spotipo-plugins/issues>`_

"""
from setuptools import setup
import re
import ast


def _get_version():
    version_re = re.compile(r'__version__\s+=\s+(.*)')

    with open('spotipo_plugins/__init__.py', 'rb') as fh:
        version = ast.literal_eval(
            version_re.search(fh.read().decode('utf-8')).group(1))

    return str(version)


setup(
    name='Spotipo-Plugins',
    version=_get_version(),
    url='https://github.com/Nibblecomm/spotipo-plugins',
    license='BSD',
    author='Rakesh Mukundan',
    author_email='rakesh@nibblecomm.com',
    description='Create plugins for spotipo',
    long_description=__doc__,
    packages=['spotipo_plugins'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.6',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose>=1.0',
    ],
    classifiers=[
        'Development Status :: Beta',
        'Framework :: Flask',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
