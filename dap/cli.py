import click
from dap.commands.project import new

@click.group()
def main():
    """A CLI app for managing data analytics projects."""
    pass

main.add_command(new)

if __name__ == "__main__":
    main()
