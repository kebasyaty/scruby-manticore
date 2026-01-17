"""Test a settings module."""

from __future__ import annotations

import pytest
from pydantic import Field
from scruby import Scruby, ScrubyModel
from scruby import settings as scruby_settings

from scruby_full_text import FullText
from scruby_full_text import settings as full_text_settings

pytestmark = pytest.mark.asyncio(loop_scope="module")

# Plugins connection.
scruby_settings.PLUGINS = [
    FullText,
]


class Car(ScrubyModel):
    """Car model."""

    brand: str = Field(strict=True, frozen=True)
    model: str = Field(strict=True, frozen=True)
    year: int = Field(strict=True)
    power_reserve: int = Field(strict=True)
    # key is always at bottom
    key: str = Field(
        strict=True,
        frozen=True,
        default_factory=lambda data: f"{data['brand']}:{data['model']}",
    )


class TestPositive:
    """Positive tests."""

    async def test_create_instance(self) -> None:
        """Create instance of plugin."""
        # Get collection `Car`
        car_coll = await Scruby.collection(Car)
        # Find a car
        car: Car | None = await car_coll.plugins.fullText.find_one(
            lang_morphology=full_text_settings.LANG_FULL_TEXT_SEARCH.get("English"),
            full_text_filter={"brand": "???", "model": "???"},
        )

        assert car is None

        # Full database deletion.
        # Hint: The main purpose is tests.
        Scruby.napalm()
