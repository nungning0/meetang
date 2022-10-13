import os
from pathlib import Path

IS_TEST = False  # TODO better solution


def expenses_path(create: bool = False):
    if IS_TEST:
        return Path.cwd() / "expenses.csv"

    exp_dir = expenses_dir_path()

    if create:
        exp_dir.mkdir(parents=True, exist_ok=True)

    return exp_dir / "expenses.csv"


def expenses_dir_path() -> Path:
    """
    1. Root user: /var/lib/taro/{db-file}
    2. Non-root user: ${XDG_DATA_HOME}/taro/{db-file} or default to ${HOME}/.local/share/taro

    :return: user data dir path
    """

    docs = Path.home() / 'Documents'
    if docs.exists():
        return docs / 'Expenses'

    if os.environ.get('XDG_DATA_HOME'):
        return Path(os.environ['XDG_DATA_HOME']) / 'expenses'

    return Path.home() / '.local' / 'share' / 'expenses'
