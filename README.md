# Deaconn
[![Deaconn To Production Action](https://github.com/Deaconn-net/back-bone/actions/workflows/to_prod.yml/badge.svg)](https://github.com/Deaconn-net/back-bone/actions/workflows/to_prod.yml)

## Description
The source code of [Deaconn](https://deaconn.net/) that uses Django, a web framework.

**Warning** - This repository was private and I made some silly commits testing things.

## Development Server
You may run Deaconn with a web development server included with Python and Django!

Use the `deaconn/exec_with_envs.sh` Bash/Shell file I created like the following.

```bash
# Make sure we're in back-bone/deaconn directory (manage.py must be included).
cd deaconn/

# Run Django web application with 'exec_with_envs.sh' that sets a couple needed environmental variables.
# Note - Web server listens @ 0.0.0.0:8000.
./exec_with_envs.sh "python3 manage.py runserver 0.0.0.0:8000"
```

## Credits
* [Christian Deacon](https://deaconn.net/)