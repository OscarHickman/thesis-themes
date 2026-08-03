"""oh_mpl_paper: publication-ready Matplotlib styles for scientific papers.

Usage
-----
>>> import oh_mpl_paper as p
>>> import matplotlib.pyplot as plt
>>> p.setconfig("nature")
>>> plt.plot(x, y)
>>> plt.show()
"""
from __future__ import annotations

from pathlib import Path
from typing import List

import matplotlib.pyplot as plt

__version__ = "0.1.0"

_STYLES_DIR = Path(__file__).resolve().parent / "styles"


def available() -> List[str]:
    """Return the sorted list of valid style names for :func:`setconfig`."""
    return sorted(f.stem for f in _STYLES_DIR.glob("*.mplstyle"))


def setconfig(config_name: str) -> None:
    """Apply the named publication style globally via ``plt.style.use``.

    Parameters
    ----------
    config_name:
        Name of a style bundled under ``oh_mpl_paper/styles/`` (without the
        ``.mplstyle`` extension), e.g. ``"nature"``, ``"ieee"``, ``"k.wang"``.

    Raises
    ------
    ValueError
        If ``config_name`` does not match any bundled style. The error lists
        every currently available style.
    """
    style_path = _STYLES_DIR / f"{config_name}.mplstyle"
    if not style_path.is_file():
        raise ValueError(
            f"Unknown style {config_name!r}. Available styles: {available()}"
        )
    plt.style.use(str(style_path))


__all__ = ["setconfig", "available", "__version__"]
