# Regulars SELinux policies 

This repo contains custom SELinux policies from
[regulars](https://regulars.win/) server and some extra files related to
security and access policies of the server. I hope this would be useful for
anyone who is trying to maintain their own Xonotic server, or perhaps someone
else.

## SELinux modules

- xonotic &mdash; module with rules for darkplaces engine
- teleport &mdash; module with rules for [teleport](https://en.wikipedia.org/wiki/Teleport_(software)) server
- drcon &mdash; module for drcon tool, it gives server admin ability to provide access
to rcon without  revealing rcon password, something that can be achieved via SUID/SGID binaries as well.
- xonadm &mdash; module that adds a restricted SELinux user, that can do basic operations. 
