import os
import py
from click.testing import CliRunner
from PIL import Image
import pytest

from colour_sort import cli


@pytest.fixture
def image(tmpdir: py._path.local.LocalPath) -> str:
    path = os.path.join(tmpdir, 'image.png')
    with Image.new('RGB', (20, 20)) as image:
        image.save(path)
    return path


def test_cli(image: str) -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, args=[
        'generate', image
    ])

    assert result.exit_code == 0
