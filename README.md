# trac-invalidate-knownuserscache

## Overview

This plugin will invalidate known users cache (calling `invalidate_known_users_cache()`) for every login request to avoid out of sync.

## Background

Even in Trac 1.2.3, [this issue](https://trac.edgewall.org/ticket/12929) still occur under LDAP integration.  This plugin will workaround it.

## Installation

This is single file plugin, just put `invalidate-knownusercache.py` into your `plugins/` directory and restart trac.

## License

See [LICENSE](LICENSE).
