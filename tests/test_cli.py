from click.testing import CliRunner
from colour_sort import cli


def test_cli(image_path: str) -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, args=[
        'generate', image_path
    ])

    assert result.exit_code == 0
