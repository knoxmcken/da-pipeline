import os
import click

@click.command()
@click.argument('project_name')
def new(project_name):
    """Creates a new data analytics project with a standardized directory structure."""
    # Base name for the project directory should be the project name
    # Every new project by default should be contained within a direcotry called projects. For example, project/project-1, project/project-2, etc.
    base_dir = os.path.join('projects', project_name)
    dirs = ['data', 'notebooks', 'src', 'config']

    try:
        os.makedirs(base_dir)
        click.echo(f"Created project directory: {base_dir}")

        for d in dirs:
            dir_path = os.path.join(base_dir, d)
            os.makedirs(dir_path)
            # Create a .gitkeep file to ensure the directory is tracked by git
            with open(os.path.join(dir_path, '.gitkeep'), 'w') as f:
                pass
        
        # Create a basic README.md in the new project
        with open(os.path.join(base_dir, 'README.md'), 'w') as f:
            f.write(f"# {project_name}\n\nThis is a new data analytics project.\n")

        click.echo(f"Successfully created project '{project_name}' with the following structure:")
        click.echo(f"- {base_dir}/")
        for d in dirs:
            click.echo(f"  - {d}/")

    except FileExistsError:
        raise click.ClickException(f"Directory '{base_dir}' already exists.")
    except Exception as e:
        raise click.ClickException(f"An unexpected error occurred: {e}")
