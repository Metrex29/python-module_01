class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = float(height) if height >= 0 else 0.0
        self._age: int = int(age) if age >= 0 else 0

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = float(height)
        else:
            print(f"{self.name}: Error, height can't be negative")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = int(age)
        else:
            print(f"{self.name}: Error, age can't be negative")

    def grow(self, amount: float = 0.8) -> None:
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(
                f"Tree {self.name} now produces a shade "
                f"of {self._height:.1f}cm "
                f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
