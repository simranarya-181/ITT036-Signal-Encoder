
import random


def generate_random_bits(length):
    """Generate a random sequence of 0s and 1s."""
    if length <= 0:
        raise ValueError("Length must be positive.")

    return [random.randint(0, 1) for _ in range(length)]


def generate_bits_with_zeros(length, zero_count):
    """Generate bits containing a guaranteed run of consecutive zeros."""
    if length < zero_count:
        raise ValueError("Length must be at least zero_count.")

    bits = generate_random_bits(length)

    start = random.randint(0, length - zero_count)
    bits[start:start + zero_count] = [0] * zero_count

    return bits


def bits_to_string(bits):
    """Convert a list of bits into a readable bitstream."""
    return "".join(map(str, bits))


def get_digital_data():
    print("\nDigital Data Generator")
    print("1. Completely random data")
    print("2. Data containing four consecutive zeros")
    print("3. Data containing eight consecutive zeros")
    print("4. Enter your own bitstream")

    choice = input("Choose an option: ").strip()

    if choice == "4":
        data = input("Enter bits (e.g. 10110001): ").strip()

        if not data or any(bit not in "01" for bit in data):
            raise ValueError("Enter a non-empty string containing only 0 and 1.")

        return [int(bit) for bit in data]

    if choice not in {"1", "2", "3"}:
        raise ValueError("Invalid data-generation option.")

    length = int(input("Enter the bitstream length: "))

    if choice == "1":
        return generate_random_bits(length)

    zero_count = 4 if choice == "2" else 8
    return generate_bits_with_zeros(length, zero_count)
