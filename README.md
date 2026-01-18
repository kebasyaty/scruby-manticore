<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/scruby-full-text">
      <img
        id="logo"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/scruby-full-text/main/assets/logo.svg">
    </a>
  </p>
  <p>
    <h1>scruby - full text</h1>
    <h3>Full-text search with Manticore Search.</h3>
    <p align="center">
      <a href="https://github.com/kebasyaty/scruby-full-text/actions/workflows/test.yml" alt="Build Status"><img src="https://github.com/kebasyaty/scruby-full-text/actions/workflows/test.yml/badge.svg" alt="Build Status"></a>
      <a href="https://kebasyaty.github.io/scruby-full-text/" alt="Docs"><img src="https://img.shields.io/badge/docs-available-brightgreen.svg" alt="Docs"></a>
      <a href="https://pypi.python.org/pypi/scruby-full-text/" alt="PyPI pyversions"><img src="https://img.shields.io/pypi/pyversions/scruby-full-text.svg" alt="PyPI pyversions"></a>
      <a href="https://pypi.python.org/pypi/scruby-full-text/" alt="PyPI status"><img src="https://img.shields.io/pypi/status/scruby-full-text.svg" alt="PyPI status"></a>
      <a href="https://pypi.python.org/pypi/scruby-full-text/" alt="PyPI version fury.io"><img src="https://badge.fury.io/py/scruby-full-text.svg" alt="PyPI version fury.io"></a>
      <br>
      <a href="https://pyrefly.org/" alt="Types: Pyrefly"><img src="https://img.shields.io/badge/types-Pyrefly-FFB74D.svg" alt="Types: Pyrefly"></a>
      <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
      <a href="https://pypi.org/project/scruby-full-text"><img src="https://img.shields.io/pypi/format/scruby-full-text" alt="Format"></a>
      <a href="https://pepy.tech/projects/scruby-full-text"><img src="https://static.pepy.tech/badge/scruby-full-text" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/scruby-full-text/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/scruby-full-text" alt="GitHub license"></a>
    </p>
    <p align="center">
      Scruby-Full-Text is a plugin for the <a href="https://github.com/kebasyaty/scruby" alt="Scruby">Scruby</a> project.
    </p>
  </p>
</div>

##

<br>

## Documentation

Online browsable documentation is available at [https://kebasyaty.github.io/scruby-full-text/](https://kebasyaty.github.io/scruby-full-text/ "Documentation").

## Requirements

[View the list of requirements](https://github.com/kebasyaty/scruby-full-text/blob/v0/REQUIREMENTS.md "Requirements").

## Installation

```shell
uv add scruby-full-text
```

## Install Manticore Search

For more information, see the <a href="https://manticoresearch.com/install/" alt="Install">documentation</a>.

- **Fedora 42 or later**

```shell
# Install the repository:
sudo tee /etc/yum.repos.d/manticore.repo << "EOF" > /dev/null
[manticore]
name=Manticore Repository
baseurl=http://repo.manticoresearch.com/repository/manticoresearch/release/centos/10/$basearch
gpgcheck=1
enabled=1
gpgkey=https://repo.manticoresearch.com/GPG-KEY-SHA256-manticore
EOF

# Install Manticore Search:
sudo dnf install manticore manticore-extra
# Install English, German, and Russian lemmatizers:
sudo dnf install manticore-language-packs

# Run Manticore Search:
sudo systemctl start manticore
sudo systemctl enable manticore
sudo systemctl status manticore --no-pager -l
```

## Usage

See more examples here [https://kebasyaty.github.io/scruby-full-text/latest/pages/usage/](https://kebasyaty.github.io/scruby-full-text/latest/pages/usage/ "Examples").

```python
import anyio
from typing import Any
from pydantic import Field
from scruby import Scruby, ScrubyModel
from scruby import settings as scruby_settings
from scruby_full_text import FullText
from scruby_full_text import settings as full_text_settings
from pprint import pprint as pp

# Plugins connection.
scruby_settings.PLUGINS = [
    FullText,
]


class Car(ScrubyModel):
    brand: str = Field(strict=True, frozen=True)
    model: str = Field(strict=True, frozen=True)
    year: int = Field(strict=True, frozen=True)
    power_reserve: int = Field(strict=True, frozen=True)
    description: str = Field(strict=True)
    # key is always at bottom
    key: str = Field(
        strict=True,
        frozen=True,
        default_factory=lambda data: f"{data['brand']}:{data['model']}",
    )


def main() -> None:
    # Get collection `Car`
    car_coll = await Scruby.collection(Car)
    # Create cars.
    for num in range(1, 10):
        car = Car(
            brand="Mazda",
            model=f"EZ-6 {num}",
            year=2025,
            power_reserve=600,
            description="Electric cars are the future of the global automotive industry.",
        )
        await car_coll.add_doc(car)

    # Find one car
    car = await car_coll.plugins.fullText.find_one(
        morphology=full_text_settings.MORPHOLOGY.get("English"),  # 'English' or 'en'
        full_text_filter=("model", "EZ-6 9"),
        # filter_fn=lambda doc: doc.brand == "Mazda",
    )
    if car is not None:
      pp(car)
    else:
      print("Not Found")

    # Fand many cars
    car_list = await car_coll.plugins.fullText.find_many(
        morphology=full_text_settings.MORPHOLOGY.get("en"),  # 'en' or 'English'
        full_text_filter=("description", "future of automotive"),
        # filter_fn=lambda doc: doc.brand == "Mazda",
    )
    if car_list is not None:
      pp(car_list)
    else:
      print("Not Found")

    # Full database deletion.
    # Hint: The main purpose is tests.
    Scruby.napalm()


if __name__ == "__main__":
    anyio.run(main)
```

## Changelog

[View the change history](https://github.com/kebasyaty/scruby-full-text/blob/v0/CHANGELOG.md "Changelog").

## License

This project is licensed under the [MIT](https://github.com/kebasyaty/scruby-full-text/blob/main/MIT-LICENSE "MIT").

This project is licensed under the [GPL-3.0-or-later](https://github.com/kebasyaty/scruby-full-text/blob/main/GPL-3.0-LICENSE "GPL-3.0-or-later").
