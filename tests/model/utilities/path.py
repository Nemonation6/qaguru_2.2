from pathlib import Path

import tests


def path_to(relative_path):
    return str(Path(tests.__file__).parent.joinpath(relative_path).absolute())
