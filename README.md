# ldapcreateusers

This module extends the Jupyterhub [ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator/)
and allows authenticated users through LDAP to have accounts created for them on the system
that Jupyterhub is running on.

It uses the LocalAuthenticator found in Jupyterhub, but authenticates users through LDAP.

The [getting started](https://github.com/jupyterhub/jupyterhub/blob/master/docs/source/getting-started.md) guide has more details.


## Configuration Settings

The settings are similar to those used in the [ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator/):

    # jupyterhub config file

    c.JupyterHub.authenticator_class = 'ldapcreateusers.LocalLDAPCreateUsers'
    c.LocalLDAPCreateUsers.server_address = 'some.ldap.server'
    c.LocalLDAPCreateUsers.server_port = 389
    c.LocalLDAPCreateUsers.use_ssl = False
    c.LocalLDAPCreateUsers.bind_dn_template = 'uid={username},dc=yourdomain,dc=com'
    c.LocalLDAPCreateUsers.create_system_users = True

## Requirements

This module does nothing by itself. It simply extends the `ldapauthenticator` class and allows local
user accounts on the system to be created.

This module has been tested with Python 3.4. It depends on [jupyterhub](https://github.com/jupyterhub/jupyterhub) and [ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator/)


## Installation

You can install using pip `$ pip install jupyterhub-ldapcreateusers`

