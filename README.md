# trac-invalidate-knownuserscache

This plugin will invalidate known users cache (calling `invalidate_known_users_cache()`) for every login request, which will avoid out of sync between cache and database.

## Background

Even in Trac 1.2.3, [this issue](https://trac.edgewall.org/ticket/12929) still occurs under LDAP integration.  This plugin will workaround it.

## Installation

This is single file plugin, just put `invalidate-knownusercache.py` into your `plugins/` directory and restart trac.

## License

See [LICENSE](LICENSE).
