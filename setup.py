from setuptools import setup

setup(
    name='jupyterhub-ldapacreateusers',
    version='0.1',
    description='Add on for the ldapauthenticator to create users',
    url='https://github.com/',
    author='Ben Hosmer',
    author_email='ben@radarearth.com',
    license='Apache 2',
    packages=['ldapcreateusers'],
    install_requires=[
        'jupyterhub-ldapauthenticator',
    ]
)
