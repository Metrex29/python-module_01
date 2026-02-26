class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        pass

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


rose: Plant = Plant("Rose", 25, 30)
sunflower: Plant = Plant("Sunflower", 80, 45)
cactus: Plant = Plant("Cactus", 15, 120)


if __name__ == "__main__":
    print(f"""=== Garden Plant Registry ===
{rose}
{sunflower}
{cactus}""")
