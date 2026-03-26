class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
    
    def grow(self, amount: float) -> None:
        self.height += amount
    
    def age_plant(self) -> None:
        self.age += 1


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    initial: float = rose.height
    
    for day in range(1,8):
        print(f"=== Day {day} ===")
        rose.show()
        if(day < 7):
            rose.grow(0.8)
            rose.age_plant()
    total_growth: float = rose.height - initial
    print(f"Growth this week: {round(total_growth)}cm")



if __name__ == "__main__":
    main()    