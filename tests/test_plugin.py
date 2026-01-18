"""Test a settings module."""

from __future__ import annotations

import pytest
from pydantic import Field
from scruby import Scruby, ScrubyModel
from scruby import settings as scruby_settings

from scruby_full_text import FullText
from scruby_full_text import settings as full_text_settings

pytestmark = pytest.mark.asyncio(loop_scope="module")

# Full database deletion.
# Hint: The main purpose is tests.
Scruby.napalm()

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

    async def test_find_one(self) -> None:
        """Test a `find_one` method."""
        # Get collection `Car`
        car_coll = await Scruby.collection(Car)
        # Create cars.
        for num in range(1, 10):
            car = Car(
                brand="Mazda",
                model=f"EZ-6 {num}",
                year=2025,
                power_reserve=600,
            )
            await car_coll.add_doc(car)
        # Find a car
        car: Car | None = await car_coll.plugins.fullText.find_one(
            lang_morphology=full_text_settings.LANG_FULL_TEXT_SEARCH.get("English"),
            full_text_filter=("brand", "SONY"),
        )

        assert car is None

        car_2: Car | None = await car_coll.plugins.fullText.find_one(
            lang_morphology=full_text_settings.LANG_FULL_TEXT_SEARCH.get("English"),
            full_text_filter=("model", "EZ-6 9"),
        )

        assert car_2.model == "EZ-6 9"
        #
        # Full database deletion.
        # Hint: The main purpose is tests.
        Scruby.napalm()

    async def test_find_many(self) -> None:
        """Test a `find_many` method."""
        # Get collection `Car`
        car_coll = await Scruby.collection(Car)
        # Create cars.
        for num in range(1, 10):
            car = Car(
                brand="Mazda",
                model=f"EZ-6 {num}",
                year=2025,
                power_reserve=600,
            )
            await car_coll.add_doc(car)
        # Find a car
        car_list: list[Car] | None = await car_coll.plugins.fullText.find_many(
            lang_morphology=full_text_settings.LANG_FULL_TEXT_SEARCH.get("English"),
            full_text_filter=("brand", "SONY"),
        )
        assert car_list is None

        car_list_2: list[Car] | None = await car_coll.plugins.fullText.find_many(
            lang_morphology=full_text_settings.LANG_FULL_TEXT_SEARCH.get("English"),
            full_text_filter=("brand", "Mazda"),
        )
        assert car_list_2 is not None
        assert len(car_list_2 or []) == 9
        #
        # Full database deletion.
        # Hint: The main purpose is tests.
        Scruby.napalm()
