"""Tests for oh_mpl_paper style loading and rendering."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pytest

import oh_mpl_paper as p


@pytest.fixture(autouse=True)
def _reset_style():
    yield
    plt.style.use("default")


def test_available_returns_bundled_styles():
    names = p.available()
    assert isinstance(names, list)
    assert names == sorted(names)
    for expected in ("base", "nature", "ieee", "presentation", "poster", "k.wang"):
        assert expected in names


@pytest.mark.parametrize("style_name", p.available())
def test_setconfig_loads_every_bundled_style(style_name):
    p.setconfig(style_name)
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 0])
    plt.close(fig)


def test_setconfig_raises_valueerror_for_unknown_style():
    with pytest.raises(ValueError) as exc_info:
        p.setconfig("not-a-real-style")
    message = str(exc_info.value)
    assert "not-a-real-style" in message
    for name in p.available():
        assert name in message


def test_sample_grid_pdf_per_style(tmp_path: Path):
    """Render a line/scatter/bar grid per style for visual inspection."""
    rng = np.random.default_rng(0)
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    scatter_y = y + rng.normal(scale=0.1, size=x.shape)
    categories = ["A", "B", "C", "D"]
    values = [3, 7, 4, 6]

    for style_name in p.available():
        p.setconfig(style_name)
        fig, axes = plt.subplots(1, 3)
        axes[0].plot(x, y, label="sin(x)")
        axes[0].legend()
        axes[0].set_title("Line")

        axes[1].scatter(x, scatter_y, s=10)
        axes[1].set_title("Scatter")

        axes[2].bar(categories, values)
        axes[2].set_title("Bar")

        out_path = tmp_path / f"sample_{style_name}.pdf"
        fig.savefig(out_path)
        plt.close(fig)

        assert out_path.is_file()
        assert out_path.stat().st_size > 0
