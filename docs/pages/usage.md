#### Example of using the plugin

```py title="main.py" linenums="1"
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
    )
    if car is not None:
      pp(car)
    else:
      print("Not Found")

    # Fand many cars
    car_list = await car_coll.plugins.fullText.find_many(
        morphology=full_text_settings.MORPHOLOGY.get("en"),  # 'en' or 'English'
        full_text_filter=("description", "future of automotive"),
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
