#!/usr/bin/env python

from trac.core import *
from trac.web.api import IAuthenticator

class InvalidateKnownUserCacheAuthenticator(Component):
    implements(IAuthenticator)

    def authenticate(self, req):
        self.env.invalidate_known_users_cache()
        return None
