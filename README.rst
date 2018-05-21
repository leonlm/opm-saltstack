opm-saltstack
==============

Plug and play continuous integration with Django REST framework and SaltStack


Installation
------------

Downloading the source and running::

    $ python setup.py install

Latest git version::

    $ pip install -e git+git://github.com/leonlm/opm-saltstack.git#egg=opm-saltstack



Usage
-----

Add ``'opm_saltstack'`` to your ``INSTALLED_APPS`` list.

Add ``settings.py``

- ``SALTSTACK``

SALTSTACK = {
    'URL': 'http://salt_server_ip:port',

    'USERNAME': 'username',

    'PASSWORD': 'password',

    'EAUTH': 'pam'

}



Settings
--------


Changelog
---------

