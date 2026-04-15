class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0.0

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    """getters and setters"""
    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Age update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def get_height(self) -> float:
        return self._height
    
    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else: 
            self._age = value
            print(f"Age updated: {value} days")

def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")

    rose.set_height(-1)
    rose.set_age(-1)
    print("")

    print(f"Current state:", end = "")
    rose.show()

if __name__ == "__main__":
    main()
