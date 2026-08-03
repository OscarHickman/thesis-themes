# oh-mpl-paper

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

Publication-ready Matplotlib styles, one function call away. Every academic
project ends up rewriting the same 40 lines of `rcParams` boilerplate to get
figures that satisfy a journal's font, size, and line-weight requirements —
`oh-mpl-paper` bundles that boilerplate as a handful of named, tested
`.mplstyle` presets and a two-line API.

## Installation

```bash
pip install git+https://github.com/OscarHickman/thesis-themes.git
```

## Usage

```python
import oh_mpl_paper as p
import matplotlib.pyplot as plt

p.setconfig("nature")          # sets all rcParams for the chosen style

plt.plot(x, y)
plt.savefig("figure.pdf")      # sized and styled for the target venue

print(p.available())           # ['base', 'ieee', 'k.wang', 'nature', 'poster', 'presentation']
```

Calling `setconfig` with an unrecognised name raises a `ValueError` listing
every style currently bundled with the package.

## Available styles

| Style          | Use case                                                                 |
|----------------|---------------------------------------------------------------------------|
| `base`         | Generic scientific-paper defaults (Type 42 fonts, colorblind-safe cycle). |
| `nature`       | Single-column Nature-family figures, 89mm wide, 8pt sans-serif fonts.    |
| `ieee`         | IEEE transactions single-column format, 3.5in wide, Times New Roman.     |
| `k.wang`       | SaUCE/`sauce_xi` MNRAS paper-figures house style (single-column, serif + Computer Modern math, muted inward ticks). |
| `presentation` | 16:9 slide decks — large fonts, thick lines, transparent background.    |
| `poster`       | A0 conference posters — very large fonts, thick lines for ~2m viewing.   |

All styles embed Type 42 (TrueType) fonts in PDF/PS output so text stays
editable in Illustrator or Inkscape, and default to a colorblind-safe
categorical color cycle.

## Development

```bash
pip install -e ".[test]"
pytest
```

## Releasing

Pushing a tag of the form `vX.Y.Z` triggers `.github/workflows/publish.yml`,
which builds the package and publishes it to PyPI via
[Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (no API
token stored in this repo). The tag's version must match the `version`
field in `pyproject.toml` or the workflow fails before publishing.

```bash
# bump version in pyproject.toml, commit, then:
git tag v0.1.1
git push origin v0.1.1
```

PyPI-side setup (one-time, done outside this repo): add a trusted publisher
on the `oh-mpl-paper` project pointing at this GitHub repo, workflow file
`publish.yml`, and environment name `pypi`.
