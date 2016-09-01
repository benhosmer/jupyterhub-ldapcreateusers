from jupyterhub.auth import Authenticator, LocalAuthenticator
from ldapauthenticator import LDAPAuthenticator

class LocalLDAPCreateUsers(LocalAuthenticator, LDAPAuthenticator):

    """Create local user accounts based on LDAP authentication"""
    pass

