from setuptools import setup

setup(
    name='jupyterhub-ldapacreateusers',
    version='0.1',
    description='Add on for the jupyterhub-ldapauthenticator to create system users',
    long_description='This module requires the jupyterhub-ldapauthenticator module and does nothing\
                       by itself. jupyterhub-ldapcreateusers allows jupyterhub to create system\
                       accounts for LDAP authenticated users.',
    url='https://github.com/benhosmer/jupyterhub-ldapcreateusers',
    author='Ben Hosmer',
    author_email='ben@radarearth.com',
    license='Apache 2',
    packages=['ldapcreateusers'],
    install_requires=[
        'jupyterhub-ldapauthenticator',
    ]
)
