from fraction import Fraction


def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    print(f"f1: {f1}")
    print(f"f2: {f2}")

    # Addition
    print(f"Addition: {f1} + {f2} = {f1 + f2}")

    # Soustraction
    print(f"Soustraction: {f1} - {f2} = {f1 - f2}")

    # Multiplication
    print(f"Multiplication: {f1} * {f2} = {f1 * f2}")

    # Division
    print(f"Division: {f1} / {f2} = {f1 / f2}")

    # Nombre mixte
    f3 = Fraction(7, 3)
    print(f"Nombre mixte de {f3}: {f3.as_mixed_number()}")

    # Comparaison
    f4 = Fraction(2, 4)
    print(f"{f1} == {f4}: {f1 == f4}")


if __name__ == "__main__":
    main()