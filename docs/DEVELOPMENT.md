# Development Guide for DAP

This document provides an in-depth guide for developers working on the Data Analytics Pipeline (DAP) CLI application.

## Project Architecture

The project follows a modular architecture, organized into the following main components:

*   **`dap/cli.py`**: The entry point for the CLI, handling command parsing and dispatching using `click`.
*   **`dap/core/`**: Contains core functionalities and cross-cutting concerns like configuration management (`config.py`) and logging (`logging.py`).
*   **`dap/commands/`**: Houses the business logic for each top-level CLI command (e.g., `project.py` for `dap new`, `data.py` for `dap data`).
*   **`dap/utils/`**: Provides utility functions that can be reused across different parts of the application.

## How to Add a New Command

To add a new top-level command (e.g., `dap <new-command>`):

1.  **Create a new command module**: In `dap/commands/`, create a new Python file (e.g., `my_new_command.py`).
2.  **Define a `click` command group/function**: Inside `my_new_command.py`, use `click.group()` or `click.command()` to define your command.
    ```python
    import click

    @click.group()
    def my_new_command():
        """Manage my new feature."""
        pass

    @my_new_command.command()
    @click.argument('name')
    def hello(name):
        """Says hello to NAME."""
        click.echo(f"Hello, {name}!")
    ```
3.  **Import and register the command**: In `dap/cli.py`, import your new command and register it with the main `dap` group:
    ```python
    import click
    from dap.commands.my_new_command import my_new_command

    @click.group()
    def main():
        """A CLI app for managing data analytics projects."""
        pass

    main.add_command(my_new_command)
    ```
4.  **Add tests**: Create a corresponding test file in `tests/commands/` (e.g., `test_my_new_command.py`).

## Configuration Management

Configuration is handled via `dap/core/config.py`. It should support loading settings from:

*   Environment variables
*   A project-specific configuration file (e.g., `dap.toml` or `dap.ini`)
*   Command-line arguments (which should override other sources)

## Release Process

1.  **Update `CHANGELOG.md`**: Document all changes since the last release.
2.  **Update version**: Increment the `version` in `pyproject.toml` according to Semantic Versioning.
3.  **Create a Git tag**: Tag the release commit with `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.
4.  **Build and publish**: (Details to be filled in later, e.g., to PyPI).
