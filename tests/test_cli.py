import os
from click.testing import CliRunner
from PIL import Image
import py
import _pytest
from colour_sort import cli
from colour_sort import image


def test_generate(
        tmpdir: py._path.local.LocalPath,
        monkeypatch: _pytest.monkeypatch.MonkeyPatch,
        image_path: str
    ) -> None:

    runner = CliRunner()
    filename = os.path.join(tmpdir, 'tmp.png')

    def identity(argument: Image.Image, *args, **kwargs) -> Image.Image: #pylint: disable=unused-argument
        return argument

    monkeypatch.setattr(image, 'as_sorted', identity)

    result = runner.invoke(cli.main, args=[
        'generate', image_path, filename,
        '--filetype', 'png'
    ])

    assert result.exit_code == 0
    assert os.path.isfile(filename)
