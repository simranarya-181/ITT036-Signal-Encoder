from data_generator import get_digital_data, bits_to_string
from palindrome import longest_palindrome
from line_coding import ENCODERS, encode
from scrambling import scramble_b8zs, scramble_hdb3
from decoding import (
    decode_nrz_l,
    decode_nrz_i,
    decode_manchester,
    decode_differential_manchester,
    decode_ami,
)
from modulation import (
    generate_analog_signal,
    pcm_encode,
    pcm_decode,
    delta_encode,
    delta_decode,
)
from plotting import plot_line_signal, plot_staircase


# ==================================================
# DESCRAMBLING SCHEMES
# ==================================================

def descramble_b8zs(signal):
    """Restore B8ZS substitution patterns (000VB0VB) back to eight zeros."""
    result = list(signal)
    i = 0

    while i + 7 < len(result):
        a = result[i + 3]

        if (
            result[i:i + 3] == [0, 0, 0]
            and a != 0
            and result[i + 4] == -a
            and result[i + 5] == 0
            and result[i + 6] == -a
            and result[i + 7] == a
        ):
            result[i:i + 8] = [0] * 8
            i += 8
        else:
            i += 1

    return result


def descramble_hdb3(signal):
    """Restore HDB3 substitution patterns (000V or B00V) back to four zeros."""
    result = list(signal)
    i = 0

    while i + 3 < len(result):
        # Find the previous nonzero pulse before this position.
        previous = 0
        for j in range(i - 1, -1, -1):
            if result[j] != 0:
                previous = result[j]
                break

        # 000V: V must violate the ordinary AMI alternation rule.
        if (
            result[i:i + 3] == [0, 0, 0]
            and result[i + 3] != 0
            and result[i + 3] == previous
        ):
            result[i:i + 4] = [0] * 4
            i += 4
            continue

        # B00V: B alternates normally with the previous pulse,
        # while V repeats B's polarity.
        if (
            result[i] != 0
            and result[i + 1:i + 3] == [0, 0]
            and result[i + 3] == result[i]
            and (previous == 0 or result[i] == -previous)
        ):
            result[i:i + 4] = [0] * 4
            i += 4
            continue

        i += 1

    return result


# ==================================================
# DECODING DISPATCH
# ==================================================

def decode_signal(signal, scheme):
    """Decode the selected line-coded waveform."""

    if scheme == "NRZ-L":
        return decode_nrz_l(signal)

    if scheme == "NRZ-I":
        return decode_nrz_i(signal)

    if scheme == "Manchester":
        return decode_manchester(signal)

    if scheme == "Differential Manchester":
        return decode_differential_manchester(signal)

    if scheme == "AMI":
        return decode_ami(signal)

    if scheme == "AMI-B8ZS":
        return decode_ami(descramble_b8zs(signal))

    if scheme == "AMI-HDB3":
        return decode_ami(descramble_hdb3(signal))

    raise ValueError(f"Unsupported decoding scheme: {scheme}")


# ==================================================
# LINE-CODING WORKFLOW
# ==================================================

def select_line_scheme(bits):
    schemes = list(ENCODERS.keys())

    print("\nAvailable line-coding schemes:")
    for index, scheme in enumerate(schemes, start=1):
        print(f"{index}. {scheme}")

    choice = int(input("Choose a scheme: "))

    if not 1 <= choice <= len(schemes):
        raise ValueError("Invalid scheme selection.")

    scheme = schemes[choice - 1]
    signal = encode(bits, scheme)
    display_scheme = scheme

    samples_per_bit = (
        2 if scheme in {"Manchester", "Differential Manchester"}
        else 1
    )

    print(f"\nEncoded signal ({scheme}):", signal)
    plot_line_signal(bits, signal, scheme, samples_per_bit)

    # Scrambling is available only for AMI.
    if scheme == "AMI":
        choice = input(
            "\nApply scrambling? (yes/no): "
        ).strip().lower()

        if choice in {"yes", "y"}:
            print("1. B8ZS")
            print("2. HDB3")

            scramble_choice = input(
                "Choose scrambling method: "
            ).strip()

            if scramble_choice == "1":
                signal = scramble_b8zs(bits)
                display_scheme = "AMI-B8ZS"

            elif scramble_choice == "2":
                signal = scramble_hdb3(bits)
                display_scheme = "AMI-HDB3"

            else:
                raise ValueError("Invalid scrambling choice.")

            print(f"\nScrambled signal ({display_scheme}):", signal)
            plot_line_signal(bits, signal, display_scheme, 1)

    decode_choice = input(
        "\nWould you like to decode the signal? (yes/no): "
    ).strip().lower()

    if decode_choice in {"yes", "y"}:
        decoded_bits = decode_signal(signal, display_scheme)
        decoded_string = bits_to_string(decoded_bits)
        original_string = bits_to_string(bits)

        print("Decoded bitstream:", decoded_string)
        print(
            "Decoding successful:",
            decoded_string == original_string
        )


# ==================================================
# DIGITAL INPUT WORKFLOW
# ==================================================

def digital_workflow():
    bits = get_digital_data()

    print("\nInput bitstream:", bits_to_string(bits))
    print("Longest palindrome:", longest_palindrome(bits))

    select_line_scheme(bits)


# ==================================================
# ANALOG INPUT WORKFLOW
# ==================================================

def analog_workflow():
    print("\nAnalog input")
    print("1. PCM")
    print("2. Delta Modulation")

    choice = input("Choose a technique: ").strip()

    t, samples = generate_analog_signal()

    plot_staircase(t, samples, "Original analog signal")

    if choice == "1":
        bits, quantized = pcm_encode(samples)
        reconstructed = pcm_decode(bits)
        technique = "PCM"

    elif choice == "2":
        bits, quantized = delta_encode(samples)
        reconstructed = delta_decode(bits)
        technique = "Delta Modulation"

    else:
        raise ValueError("Invalid modulation choice.")

    print(f"\n{technique} bitstream:", bits_to_string(bits))
    print("Number of generated bits:", len(bits))

    plot_staircase(
        range(len(quantized)),
        quantized,
        f"{technique}: Encoded/quantized values",
    )

    plot_staircase(
        range(len(reconstructed)),
        reconstructed,
        f"{technique}: Decoder staircase",
    )

    line_choice = input(
        "\nLine-encode these bits too? (yes/no): "
    ).strip().lower()

    if line_choice in {"yes", "y"}:
        select_line_scheme(bits)


# ==================================================
# MAIN MENU
# ==================================================

def main():
    print("=" * 45)
    print("ITT 036: DIGITAL SIGNAL ENCODER / DECODER")
    print("=" * 45)
    print("1. Digital input")
    print("2. Analog input (PCM / DM)")

    choice = input("Choose input type: ").strip()

    try:
        if choice == "1":
            digital_workflow()
        elif choice == "2":
            analog_workflow()
        else:
            print("Invalid choice.")

    except (ValueError, EOFError) as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()