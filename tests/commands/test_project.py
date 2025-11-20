from click.testing import CliRunner
from dap.commands.project import new
from pathlib import Path
import os

def test_new_project_creation():
    """
    Test that the `dap new` command successfully creates a project directory
    with the correct subdirectories and files.
    """
    runner = CliRunner()
    project_name = "test-project"
    with runner.isolated_filesystem():
        result = runner.invoke(new, [project_name])

        assert result.exit_code == 0, result.output
        assert f"Successfully created project '{project_name}'" in result.output

        project_path = Path('projects') / project_name
        assert project_path.is_dir()

        expected_dirs = ['data', 'notebooks', 'src', 'config']
        for d in expected_dirs:
            dir_path = project_path / d
            assert dir_path.is_dir()
            assert (dir_path / '.gitkeep').is_file()
        
        readme_path = project_path / 'README.md'
        assert readme_path.is_file()
        with open(readme_path, 'r') as f:
            content = f.read()
            assert f"# {project_name}" in content

def test_new_project_fails_if_exists():
    """
    Test that `dap new` fails if the project directory already exists.
    """
    runner = CliRunner()
    project_name = "test-project"
    with runner.isolated_filesystem():
        # Create the directory first
        os.makedirs(os.path.join('projects', project_name))

        result = runner.invoke(new, [project_name])

        assert result.exit_code == 1
        assert f"Error: Directory 'projects/{project_name}' already exists." in result.output
