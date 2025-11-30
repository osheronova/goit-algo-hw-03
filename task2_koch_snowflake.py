import turtle


def koch_side(length: float, level: int) -> None:
    """Draw one side of the Koch snowflake using recursion."""
    if level == 0:
        turtle.forward(length)
        return

    length /= 3.0

    # Same pattern repeated at a smaller scale
    koch_side(length, level - 1)
    turtle.left(60)
    koch_side(length, level - 1)
    turtle.right(120)
    koch_side(length, level - 1)
    turtle.left(60)
    koch_side(length, level - 1)


def koch_snowflake(length: float, level: int) -> None:
    """Draw full snowflake (3 Koch sides forming a triangle)."""
    for _ in range(3):
        koch_side(length, level)
        turtle.right(120)


def main() -> None:
    """Ask user for recursion level and draw the snowflake."""
    level = int(input("Enter recursion level (e.g. 0–6): "))

    turtle.speed(0)        # Fast drawing
    turtle.penup()
    turtle.goto(-150, 80)  # Simple starting position
    turtle.pendown()

    koch_snowflake(300, level)

    turtle.hideturtle()
    turtle.done()          # Keep the window open


if __name__ == "__main__":
    main()
