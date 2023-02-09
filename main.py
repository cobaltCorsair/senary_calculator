class Senary:
    """Class that implements operations on numbers in the senary numeral system."""

    def __init__(self, value: int):
        """Initialize the Senary object with a decimal value."""
        self.value = value

    def __add__(self, other: 'Senary') -> 'Senary':
        """Add two senary numbers and return the result as a Senary object."""
        return Senary(self.value + other.value)

    def __sub__(self, other: 'Senary') -> 'Senary':
        """Subtract two senary numbers and return the result as a Senary object."""
        return Senary(self.value - other.value)

    def __int__(self) -> int:
        """Convert the Senary object to a decimal integer."""
        return self.value

    @staticmethod
    def from_senary(senary_str: str) -> 'Senary':
        """Convert a senary string to a Senary object."""
        # Check if the senary string is negative
        negative = False
        if senary_str[0] == "-":
            negative = True
            senary_str = senary_str[1:]
        # Convert the senary string to a decimal integer
        decimal = 0
        for i, char in enumerate(reversed(senary_str)):
            decimal += int(char) * (6 ** i)
        # If the senary string was negative, negate the decimal value
        if negative:
            decimal = -decimal
        # Return the decimal value as a Senary object
        return Senary(decimal)

    def to_senary(self) -> str:
        """Convert the Senary object to a senary string."""
        senary = ""
        value = self.value
        if value < 0:
            senary = "-"
            value = abs(value)
        while value > 0:
            senary = str(value % 6) + senary
            value = value // 6
        if senary[-1] == "-":
            return str(-int(senary[:-1]))
        else:
            return senary


class SenaryCalculator:
    """Class that implements a menu for performing operations on numbers in the senary numeral system."""

    def __init__(self):
        """Initialize the SenaryCalculator object."""
        self.menu = """
        Senary Calculator

        1. Add two senary numbers
        2. Subtract two senary numbers
        3. Convert a senary string to a decimal integer
        4. Convert a decimal integer to a senary string
        5. Exit

        Enter your choice (1-5): """

    def handle_input_error(self) -> None:
        """Handle input errors."""
        print("Invalid input. Try again.")

    def add_senary_numbers(self) -> None:
        """Add two senary numbers."""
        try:
            a = Senary.from_senary(input("Enter the first senary number: "))
            b = Senary.from_senary(input("Enter the second senary number: "))
            print("The result is:", (a + b).to_senary())
        except ValueError:
            self.handle_input_error()

    def subtract_senary_numbers(self) -> None:
        """Subtract two senary numbers."""
        try:
            a = Senary.from_senary(input("Enter the first senary number: "))
            b = Senary.from_senary(input("Enter the second senary number: "))
            print("The result is:", (a - b).to_senary())
        except ValueError:
            self.handle_input_error()

    def convert_senary_to_decimal(self) -> None:
        """Convert a senary string to a decimal integer."""
        try:
            senary_str = input("Enter a senary number: ")
            decimal = int(Senary.from_senary(senary_str))
            print("The equivalent decimal number is:", decimal)
        except ValueError:
            self.handle_input_error()

    def convert_decimal_to_senary(self) -> None:
        """Convert a decimal integer to a senary string."""
        try:
            decimal = int(input("Enter a decimal number: "))
            senary = Senary(decimal).to_senary()
            print("The equivalent senary number is:", senary)
        except ValueError:
            self.handle_input_error()

    def run(self) -> None:
        """Run the SenaryCalculator menu."""
        while True:
            # Display the menu
            choice = input(self.menu)

            # Validate the choice
            try:
                choice = int(choice)
                if choice < 1 or choice > 5:
                    raise ValueError
            except ValueError:
                print("Invalid option. Try again.")
                continue

            # Perform the selected operation
            if choice == 1:
                self.add_senary_numbers()
            elif choice == 2:
                self.subtract_senary_numbers()
            elif choice == 3:
                self.convert_senary_to_decimal()
            elif choice == 4:
                self.convert_decimal_to_senary()
            elif choice == 5:
                print("Exiting the program.")
                break


# calculator = SenaryCalculator()
# calculator.run()
