class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._grow_age: int = 0
            self._grow_show: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._grow_age} age, {self._grow_show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = float(height) if height >= 0 else 0.0
        self._age: int = int(age) if age >= 0 else 0
        self._stats: Plant.Stats = self.Stats()

    def grow(self, amount: float = 0.8) -> None:
        self._stats._grow_count += 1
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._age += days
        self._stats._grow_age += 1

    def show(self) -> None:
        self._stats._grow_show += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    @staticmethod
    def older_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._stats: Tree.Stats = self.Stats()
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        self._stats._shade_count += 1
        print(
            f"Tree {self.name} now produces a shade "
            f"of {self._height:.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str,
        height: float,
        age: int,
        season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: int = 0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def display_plant_stats(plant: Plant) -> None:
    plant._stats.display()


def main() -> None:
    # Bloque de pruebas según el ejemplo de Analytics
    print("Garden statistics ===")
    print("Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_year(400)}")

    print("\nFlower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)
    
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_plant_stats(rose)

    print("\nTree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_stats(sunflower)

    print("\nAnonymous")
    anon = Plant.anonymous_plant()
    anon.show()
    print("[statistics for Unknown plant]")
    display_plant_stats(anon)


if __name__ == "__main__":
    main()
