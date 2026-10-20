
def decode_nrz_l(signal):
    return [0 if level > 0 else 1 for level in signal]


def decode_nrz_i(signal, initial_level=1):
    bits = []
    previous = initial_level

    for level in signal:
        bits.append(1 if level != previous else 0)
        previous = level

    return bits


def decode_manchester(signal):
    if len(signal) % 2:
        raise ValueError("Manchester signal needs pairs of levels.")

    bits = []

    for i in range(0, len(signal), 2):
        first, second = signal[i], signal[i + 1]

        if first == -1 and second == 1:
            bits.append(0)
        elif first == 1 and second == -1:
            bits.append(1)
        else:
            raise ValueError("Invalid Manchester symbol.")

    return bits


def decode_differential_manchester(signal, initial_level=1):
    if len(signal) % 2:
        raise ValueError(
            "Differential Manchester signal needs pairs of levels."
        )

    bits = []
    previous = initial_level

    for i in range(0, len(signal), 2):
        first, second = signal[i], signal[i + 1]

        if first not in (-1, 1) or second not in (-1, 1):
            raise ValueError("Invalid signal level.")

        if first == second:
            raise ValueError("Missing middle transition.")

        bits.append(1 if first == previous else 0)
        previous = second

    return bits


def decode_ami(signal):
    return [0 if level == 0 else 1 for level in signal]
