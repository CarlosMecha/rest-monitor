# REST Monitor

A system monitor that exposes a REST API.

## Configuration

Declare `MONITOR_ACCESS_TOKEN` as environment variable before running the application. The
clients should add the header `Auth-Token: ` with the same token to access.

## Requirements

- Python 2.7
- Bottle
- Psutils
- Virtualenv (Optional)

## Instalation

For now, just copy the code into your server and add a virtual environment for it:
```bash
$ pip install virtualenv
$ virtualenv folder
$ source folder/bin/activate
$ pip install bottle psutil
```

## Run the server

This minimal bottle application runs in the port 3344.
```bash
$ python monitor.py
```

## Query the server

```bash
$ wget -qO - --header 'Auth-Token: mytoken' http://my-server:3344/ | python -m json.tool
```

