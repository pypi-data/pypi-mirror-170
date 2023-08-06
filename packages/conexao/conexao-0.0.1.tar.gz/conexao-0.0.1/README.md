# Conexao

A connection helper. Current features:

- Management of multiple remote MongoDB connection profiles.
- Faster permanent remote Docker connections.
- SSH port forward proxies.

## Configuration

Add a JSON file to `~/.config/conexao/config.json`.


## Docker

Opens a permanent SSH forward for faster remote Docker command execution.
Based on:
https://forums.docker.com/t/setting-docker-host-to-ssh-results-in-slow-workflow-can-ssh-connection-be-reused/98754

    conexao docker <host>


## MongoDB

```
from conexao.mongo import create_client

c = create_client('profileName')
```


## Limitations

This program uses a Python Shelve to store SSH PIDs of all running forwards. Shelve isn't concurrent safe, so avoid calling this program multiple times in parallel. Once the program returns it should be safe to call it again to add more connections.