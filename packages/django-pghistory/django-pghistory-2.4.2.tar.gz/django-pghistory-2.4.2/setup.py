# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pghistory', 'pghistory.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django-pgtrigger>=3.2.0', 'django>=2']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['importlib_metadata>=4']}

setup_kwargs = {
    'name': 'django-pghistory',
    'version': '2.4.2',
    'description': 'History tracking for Django and Postgres',
    'long_description': 'django-pghistory\n################\n\n``django-pghistory`` provides automated and customizable history\ntracking for Django models using\n`Postgres triggers <https://www.postgresql.org/docs/12/sql-createtrigger.html>`__.\nUsers can configure a number of event trackers to snapshot every model\nchange or to fire specific events when certain changes occur in the database.\n\nIn contrast with other Django auditing and history tracking apps\n(seen `here <https://djangopackages.org/grids/g/model-audit/>`__),\n``django-pghistory`` has the following advantages:\n\n1. No instrumentation of model and queryset methods in order to properly\n   track history. After configuring your model, events will be tracked\n   automatically with no other changes to code. In contrast with\n   apps like\n   `django-reversion <https://django-reversion.readthedocs.io/en/stable/>`__,\n   it is impossible for code to accidentally bypass history tracking, and users\n   do not have to use a specific model/queryset interface to ensure history\n   is correctly tracked.\n2. Bulk updates and all other modifications to the database that do not fire\n   Django signals will still be properly tracked.\n3. Historical event modeling is completely controlled by the user and kept\n   in sync with models being tracked. There are no cumbersome generic foreign\n   keys and little dependence on unstructured JSON fields for tracking changes,\n   making it easier to use the historical events in your application (and\n   in a performant manner).\n4. Changes to multiple objects in a request (or any level of granularity)\n   can be grouped together under the same context. Although history tracking\n   happens in Postgres triggers, application code can still attach metadata\n   to historical events, such as the URL of the request, leading to a more\n   clear and useful audit trail.\n\nTo get started, read the `django-pghistory docs\n<https://django-pghistory.readthedocs.io/>`__. The docs covers how to\nset up and configure automated event tracking in your application, along\nwith how to aggregate events for objects and visualize them in your\nadmin/application.\n\nDocumentation\n=============\n\n`View the django-pghistory docs here\n<https://django-pghistory.readthedocs.io/>`_.\n\nInstallation\n============\n\nInstall django-pghistory with::\n\n    pip3 install django-pghistory\n\nAfter this, add ``pghistory`` and ``pgtrigger`` to the ``INSTALLED_APPS``\nsetting of your Django project.\n\nContributing Guide\n==================\n\nFor information on setting up django-pghistory for development and\ncontributing changes, view `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.\n\nPrimary Authors\n===============\n\n- @wesleykendall (Wes Kendall, wesleykendall@protonmail.com)\n\nOther Contributors\n==================\n\n- @shivananda-sahu\n- @asucrews\n- @Azurency\n- @dracos\n- @adamchainz\n- @eeriksp\n',
    'author': 'Wes Kendall',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Opus10/django-pghistory',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4',
}


setup(**setup_kwargs)
