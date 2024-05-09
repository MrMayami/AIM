# test_aim_cli.py

import pytest
import aim_cli
import os

def test_setup_python():
    # Check if Python is installed
    assert aim_cli.setup_python() is None

def test_create_virtualenv():
    # Check if virtual environment is created
    assert aim_cli.create_virtualenv() is None
    assert os.path.exists("venv")

def test_create_project_structure():
    # Check if project structure is created
    assert aim_cli.create_project_structure() is None
    assert os.path.exists("app")
    assert os.path.exists("app/static")
    assert os.path.exists("app/templates")
    assert os.path.exists("app/__init__.py")
    assert os.path.exists("app/routes.py")
    assert os.path.exists("run.py")

def test_install_flask():
    # Check if Flask is installed
    assert aim_cli.install_flask() is None

def test_install_pyyaml():
    # Check if PyYAML is installed
    assert aim_cli.install_pyyaml() is None

def test_create_workflow_file():
    # Check if workflow file is created
    assert aim_cli.create_workflow_file() is None
    assert os.path.exists(".github/workflows/ci-cd.yml")

def test_integrate_bootstrap():
    # Check if bootstrap integration message is logged
    assert aim_cli.integrate_bootstrap() is None

def test_create_requirements_file():
    # Check if requirements file is created
    assert aim_cli.create_requirements_file() is None
    assert os.path.exists("requirements.txt")

def test_setup():
    # Check if setup completes successfully
    assert aim_cli.setup() is None
