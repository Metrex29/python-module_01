class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age_current: int = age
        pass
    
    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_current} days old"
    
    
    def grow(self, amount: int) -> None:
        self.height += amount

    def age(self) -> None:
        self.age_current +=1

if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    initial_height: int = rose.height

print(f"=== Day 1 ===")
print(rose.get_info())
for _ in range(6):
    rose.grow(1)
    rose.age()
print(f"=== Day 7 ===")
print(rose.get_info())

total_growth: int = rose.height - initial_height
print(f"Growth this week: +{total_growth}cm")
