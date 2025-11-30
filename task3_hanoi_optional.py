"""Tower of Hanoi implementation with state display after each move."""


def move_disk(source: str, target: str, state: dict) -> None:
    """Move top disk from source to target and show current state."""
    disk = state[source].pop()      # Take top disk from source rod
    state[target].append(disk)      # Put it on target rod

    print(f"Move disk from {source} to {target}: {disk}")
    print(f"Intermediate state: {state}")


def hanoi(n: int, source: str, target: str, helper: str, state: dict) -> None:
    """Classic recursive Hanoi solution."""
    if n == 0:
        return

    # Step 1: move n-1 smaller disks to helper
    hanoi(n - 1, source, helper, target, state)

    # Step 2: move biggest remaining disk to target
    move_disk(source, target, state)

    # Step 3: move n-1 disks from helper to target
    hanoi(n - 1, helper, target, source, state)


def main() -> None:
    """Read n, set up rods and run the algorithm."""
    n = int(input("Enter number of disks: "))

    # A starts with all disks: biggest at index 0, smallest at the end
    state = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": []
    }

    print(f"Initial state: {state}")
    hanoi(n, "A", "C", "B", state)
    print(f"Final state: {state}")


if __name__ == "__main__":
    main()
