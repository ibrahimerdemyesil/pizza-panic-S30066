"""Entry point for `python -m highrev`."""

from pathlib import Path

from kedro.framework.project import configure_project

from .pipeline_registry import register_pipelines  # noqa: F401


def main():
    from kedro.framework.cli.utils import find_run_command

    package_name = Path(__file__).parent.name
    configure_project(package_name)
    run = find_run_command(package_name)
    run()


if __name__ == "__main__":
    main()
