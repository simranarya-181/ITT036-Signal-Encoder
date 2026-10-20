
def encode_nrz_l(bits):
    return [1 if bit == 0 else -1 for bit in bits]


def encode_nrz_i(bits, initial_level=1):
    level = initial_level
    signal = []

    for bit in bits:
        if bit == 1:
            level *= -1
        signal.append(level)

    return signal


def encode_manchester(bits):
    signal = []

    for bit in bits:
        signal.extend([-1, 1] if bit == 0 else [1, -1])

    return signal


def encode_differential_manchester(bits, initial_level=1):
    level = initial_level
    signal = []

    for bit in bits:
        if bit == 0:
            level *= -1

        signal.append(level)

        # Mandatory middle transition
        level *= -1
        signal.append(level)

    return signal


def encode_ami(bits, initial_polarity=1):
    polarity = -initial_polarity
    signal = []

    for bit in bits:
        if bit == 0:
            signal.append(0)
        else:
            polarity *= -1
            signal.append(polarity)

    return signal


ENCODERS = {
    "NRZ-L": encode_nrz_l,
    "NRZ-I": encode_nrz_i,
    "Manchester": encode_manchester,
    "Differential Manchester": encode_differential_manchester,
    "AMI": encode_ami,
}


def encode(bits, scheme):
    """Select an encoder using a dictionary rather than a large if/else."""
    if scheme not in ENCODERS:
        raise ValueError(f"Unknown line-coding scheme: {scheme}")

    return ENCODERS[scheme](bits)
