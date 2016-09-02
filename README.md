**Docs to follow**

**Not Complete**

# jupyterhub config file
c.JupyterHub.authenticator_class = 'ldapcreateusers.LocalLDAPCreateUsers'
c.LocalLDAPCreateUsers.server_address = '192.168.33.64'
c.LocalLDAPCreateUsers.server_port = 389
c.LocalLDAPCreateUsers.use_ssl = False
c.LocalLDAPCreateUsers.bind_dn_template = 'uid={username},dc=rbtcloud,dc=dev'
c.LocalLDAPCreateUsers.create_system_users = True

