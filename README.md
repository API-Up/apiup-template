API
=================================================

Set Up
-------------------------------------------------

1. Download API CLI

on Linux
```shell
curl -L -o apiup https://github.com/api-up/apiup-cli/releases/download/latest/apiup-linux-x64-latest ; chmod +x apiup
```

on MacOS
```shell
curl -L -o apiup https://github.com/api-up/apiup-cli/releases/download/latest/apiup-macos-arm64-latest ; chmod +x apiup
```

on Windows 10+
```shell
curl -L -o apiup https://github.com/api-up/apiup-cli/releases/download/latest/apiup-windows-x64-latest.exe
```

2. Examine, test and/or delete the `sample` app


Requirements
-------------------------------------------------

- [Docker 28.2.2+](https://www.docker.com/products/docker-desktop/)
- [Python 3.14+](https://www.python.org/downloads/)


Getting started
-------------------------------------------------

```shell
apiup check  # Check if the Env has the requirements to run the API
apiup models  # Generate models from YAML schemas
apiup start  # Start the API
apiup ping  # Ping the API to check it is running
apiup create_admin  # To create the first user and other admins
apiup admin  # Open the Admin UI
apiup stop  # Stop the resources
```


Development
-------------------------------------------------

```shell
apiup models  # Generate models from YAML schemas
apiup format  # Format the source code
apiup lint  # Format and Lint the source code
apiup compile  # Check for syntax errors
apiup tests  # Run unit tests
apiup coverage  # Run test coverage
apiup build  # Build the Docker image
apiup rebuild  # Rebuild the Docker image (no cache)
apiup ci  # Run all: format lint build tests
apiup info  # Check the API resources

apiup db_changes  # Check the differences between the current schema and the DB
apiup db_migrate  # Update the database schema with the current one
apiup db_clean  # Drop the dev database, for a fresh start

apiup python  # Start the Python shell
```


Operation
-------------------------------------------------

```shell
apiup version
apiup upgrade
```


Development Integration
-------------------------------------------------

```shell
# To use Git hooks for CI
pip install pre-commit
pre-commit install  # to run CI before any Git commit
pre-commit uninstall  # to remove the Git CI hooks
```


Next steps
-------------------------------------------------

- Add Python dependencies to the `requirements-app.txt` file
- Customize your Docker image in `Dockerfile` (keep the base image though)
- Implement Commands and Tasks inside the apps folder, in subfolders, like the `sample` app

- [Project Structure](https://docs.apiup.ai/getting_started/#project-structure)
- [Quick Reference](https://docs.apiup.ai/quick_reference/)
- [Full Documentation](https://docs.apiup.ai/commands/)
