from math import gcd


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1) -> None:
        """
        Initialise une fraction avec un numérateur et un dénominateur.

        PRE : den != 0 (le dénominateur ne doit pas être égal à zéro)
        POST : La fraction est créée et simplifiée
        (par exemple, 4/8 devient 1/2)
        RAISES : ValueError si le dénominateur est égal à zéro
        """
        if den == 0:
            raise ValueError(
                "Le dénominateur ne peut pas être zéro.")

        self.num = num
        self.den = den
        self._simplify()

    def _simplify(self):
        """
        Simplifie la fraction en divisant le numérateur et le dénominateur
        par leur plus grand commun diviseur (PGCD).

        PRE : num et den sont des entiers, den != 0
        POST : num et den sont simplifiés
        """
        pgcd = gcd(self.num, self.den)
        self.num //= pgcd
        self.den //= pgcd

        # Etre sûr que le dénominateur est toujours positif
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

    @property
    def numerator(self) -> int:
        """
        Retourne le numérateur de la fraction.

        PRE : Aucune
        POST : Retourne l'attribut `self.num` (le numérateur de la fraction)
        RAISES : Aucune
        """
        return self.num

    @property
    def denominator(self) -> int:
        """
        Retourne le dénominateur de la fraction.

        PRE : Aucune
        POST : Retourne l'attribut `self.den` (le dénominateur de la fraction)
        RAISES : Aucune
        """
        return self.den
# ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle
        de la fraction sous sa forme réduite.

        PRE : Aucune
        POST : Retourne une chaîne de caractères
        au format "numérateur/dénominateur"
            ou "numérateur" si le dénominateur
            est égal à 1 (ex : "3/4" ou "5").
        RAISES : Aucune
        """
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def as_mixed_number(self) -> str:
        """
        Retourne une représentation textuelle de
        la fraction sous forme de nombre mixte.

        Un nombre mixte est la somme d'un entier
        et d'une fraction propre.

        PRE : Aucune
        POST : Retourne une chaîne de caractères au format "entier fraction"
            (ex : "1 2/3") ou uniquement "entier" si la fraction est entière.
        RAISES : Aucune
        """
        if abs(self.num) < self.den:  # Fraction propre
            return str(self)
        elif self.num % self.den == 0:  # Fraction entière
            return str(self.num // self.den)
        else:  # Nombre mixte
            entier = self.num // self.den
            reste = abs(self.num % self.den)
            return f"{entier} {reste}/{self.den}"

# ------------------ Operators overloading ------------------

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Surcharge de l'opérateur + pour l'addition de fractions.

        PRE :
        - `other` doit être une instance de la classe Fraction.
        - Les dénominateurs des fractions doivent être non nuls.

        POST :
        - Retourne une nouvelle fraction simplifiée
        représentant la somme des deux fractions.
        - Ne modifie pas les fractions initiales (`self` et `other`).

        RAISES :
        - TypeError si `other` n'est pas une instance de Fraction.
        - ValueError si le dénominateur de l'une des fractions est nul.
        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opérande doit être une instance de la classe Fraction.")
        if self.den == 0 or other.den == 0:
            raise ValueError(
                "Le dénominateur ne peut pas être égal à zéro.")

        # Calcul de la somme en utilisant un dénominateur commun
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den

        return Fraction(num, den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Surcharge de l'opérateur - pour la soustraction de fractions.

        PRE :
        - `other` doit être une instance de la classe Fraction.
        - Les dénominateurs des fractions doivent être non nuls.

        POST :
        - Retourne une nouvelle fraction simplifiée
        représentant la différence entre les deux fractions.
        - Ne modifie pas les fractions initiales (`self` et `other`).

        RAISES :
        - TypeError si `other` n'est pas une instance de Fraction.
        - ValueError si le dénominateur de l'une des fractions est nul.
        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opérande doit être une instance de la classe Fraction.")
        if self.den == 0 or other.den == 0:
            raise ValueError(
                "Le dénominateur ne peut pas être égal à zéro.")

        # Calcul de la différence en utilisant un dénominateur commun
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den

        return Fraction(num, den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Surcharge de l'opérateur * pour la multiplication de fractions.

        PRE :
        - `other` doit être une instance de la classe Fraction.
        - Les dénominateurs des fractions doivent être non nuls.

        POST :
        - Retourne une nouvelle fraction simplifiée
        représentant le produit des deux fractions.
        - Ne modifie pas les fractions initiales (`self` et `other`).

        RAISES :
        - TypeError si `other` n'est pas une instance de Fraction.
        - ValueError si le dénominateur de l'une des fractions est nul.
        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opérande doit être une instance de la classe Fraction.")
        if self.den == 0 or other.den == 0:
            raise ValueError("Le dénominateur ne peut pas être égal à zéro.")

        # Calcul du produit
        num = self.num * other.num
        den = self.den * other.den

        return Fraction(num, den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Surcharge de l'opérateur / pour la division de fractions.

        PRE :
        - `other` doit être une instance de la classe Fraction.
        - Le numérateur de `other` ne doit pas être égal à zéro.
        - Les dénominateurs des fractions doivent être non nuls.

        POST :
        - Retourne une nouvelle fraction
        simplifiée représentant le quotient des deux fractions.
        - Ne modifie pas les fractions initiales (`self` et `other`).

        RAISES :
        - TypeError si `other` n'est pas une instance de Fraction.
        - ZeroDivisionError si le numérateur de `other` est zéro.
        - ValueError si le dénominateur de l'une des fractions est nul.
        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'opérande doit être une instance de la classe Fraction.")
        if other.num == 0:
            raise ZeroDivisionError(
                "Division par une fraction avec un numérateur égal à zéro.")
        if self.den == 0 or other.den == 0:
            raise ValueError(
                "Le dénominateur ne peut pas être égal à zéro.")

        # Calcul du quotient
        num = self.num * other.den
        den = self.den * other.num

        return Fraction(num, den)

    def __pow__(self, other):
        """
        Surcharge de l'opérateur ** pour élever une fraction à une puissance.

        PRE :
        - `other` doit être un entier (positif, négatif ou nul).
        - Le numérateur et le dénominateur de
        la fraction ne doivent pas être nuls.

        POST :
        - Retourne une nouvelle fraction représentant
        la fraction `self` élevée à la puissance `other`.
        - Si `other` est négatif, la fraction est
        inversée avant l'élévation à la puissance.

        RAISES :
        - TypeError si `other` n'est pas un entier.
        - ValueError si le dénominateur de `self` est zéro.
        """
        if not isinstance(other, int):
            raise TypeError("La puissance doit être un entier.")
        if self.den == 0:
            raise ValueError(
                "Le dénominateur ne peut pas être égal à zéro.")

        # Calcul de la puissance
        if other >= 0:
            return Fraction(self.num ** other, self.den ** other)
        else:
            return Fraction(
                self.den ** abs(other), self.num ** abs(other))

    def __eq__(self, other: 'Fraction') -> bool:
        """
        Surcharge de l'opérateur == pour comparer deux fractions.

        PRE :
        - `other` doit être une instance de la classe Fraction.

        POST :
        - Retourne True si les deux fractions
        sont égales après simplification, sinon False.

        RAISES :
        - TypeError si `other` n'est pas une instance de la classe Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "La comparaison n est que possible avec une autre fraction."
            )

        # Comparaison après simplification
        return self.num * other.den == self.den * other.num

    def __float__(self) -> float:
        """
        Retourne la valeur décimale de la fraction.

        PRE :
        - Le numérateur et le dénominateur doivent être des entiers valides.

        POST :
        - Retourne un nombre à virgule flottante représentant la fraction.

        RAISES :
        - ZeroDivisionError si le dénominateur est égal à zéro.
        """
        if self.den == 0:
            raise ZeroDivisionError(
                "Le dénominateur ne peut pas être zéro.")
        return self.num / self.den

# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

# ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """
        Vérifie si la valeur de la fraction est égale à 0.

        PRE :
        - Le numérateur et le dénominateur doivent être des entiers valides.

        POST :
        - Retourne True si la valeur de la fraction est 0, sinon False.

        RAISES :
        - ZeroDivisionError si le dénominateur est égal à zéro.
        """
        if self.den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être zéro.")
        return self.num == 0

    def is_integer(self) -> bool:
        """
        Vérifie si la fraction est un entier (ex : 8/4, 3, 2/2).

        PRE :
        - Le numérateur et le dénominateur doivent être des entiers valides.
        - Le dénominateur ne doit pas être égal à zéro.

        POST :
        - Retourne True si la fraction représente un entier, sinon False.

        RAISES :
        - ZeroDivisionError si le dénominateur est égal à zéro.
        """
        if self.den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être zéro.")
        return self.num % self.den == 0

    def is_proper(self) -> bool:
        """
        Vérifie si la valeur absolue de la fraction
        est strictement inférieure à 1.

        PRE :
        - Le numérateur et le dénominateur doivent être des entiers valides.
        - Le dénominateur ne doit pas être égal à zéro.

        POST :
        - Retourne True si la valeur absolue
        de la fraction est < 1, sinon False.

        RAISES :
        - ZeroDivisionError si le dénominateur est égal à zéro.
        """
        if self.den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être zéro.")
        return abs(self.num) < abs(self.den)

    def is_unit(self) -> bool:
        """
        Vérifie si le numérateur de la fraction simplifiée est égal à 1.

        PRE :
        - Le numérateur et le dénominateur doivent être des entiers valides.
        - Le dénominateur ne doit pas être égal à zéro.
        - La fraction doit être simplifiée.

        POST :
        - Retourne True si le numérateur simplifié est égal à 1, sinon False.

        RAISES :
        - ZeroDivisionError si le dénominateur est égal à zéro.
        """
        if self.den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être zéro.")
        return self.num == 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """
        Vérifie si deux fractions diffèrent d'une fraction unitaire.

        PRE :
        - `other` doit être une instance valide de la classe Fraction.
        - Le numérateur et le dénominateur des deux fractions
        doivent être des entiers valides.
        - Les deux fractions doivent être simplifiées.

        POST :
        - Retourne True si la différence absolue entre les
        deux fractions est une fraction unitaire
        (dont le numérateur est égal à 1 dans
        sa forme simplifiée), sinon False.

        RAISES :
        - TypeError : Si `other` n'est pas une instance de la classe Fraction.
        - ZeroDivisionError : Si l'une des
        fractions a un dénominateur égal à zéro.
        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "L'argument doit être une instance de la classe Fraction.")
        if self.den == 0 or other.den == 0:
            raise ZeroDivisionError(
                "Le dénominateur d'une fraction ne peut pas être zéro.")

        # Calcul de la différence, en croisant les dénominateurs pour éviter les flottants
        difference = abs(self.num * other.den - other.num * self.den)

        # Vérification si la différence correspond à 1 (c'est-à-dire une fraction unitaire)
        return difference == 1



