def scramble_b8zs(bits, initial_polarity=1):
    """Encode bits using AMI with B8ZS substitution (000VB0VB)."""
    signal = []
    polarity = -initial_polarity
    i = 0

    while i < len(bits):
        if bits[i:i + 8] == [0] * 8:
            p = polarity
            # 000VB0VB sequence relative to preceding pulse p:
            # V = p, B = -p, 0 = 0, V = -p, B = p
            signal.extend([0, 0, 0, p, -p, 0, -p, p])
            polarity = p
            i += 8
        elif bits[i] == 0:
            signal.append(0)
            i += 1
        else:
            polarity *= -1
            signal.append(polarity)
            i += 1

    return signal


def scramble_hdb3(bits, initial_polarity=1):
    """Encode bits using AMI with HDB3 substitution (000V or B00V)."""
    signal = []
    polarity = -initial_polarity
    pulse_count = 0
    i = 0

    while i < len(bits):
        if bits[i:i + 4] == [0] * 4:
            if pulse_count % 2 == 1:
                # 000V: Violation pulse matches previous pulse polarity
                violation = polarity
                signal.extend([0, 0, 0, violation])
                polarity = violation
            else:
                # B00V: Balancing pulse alternates, Violation matches B
                balancing = -polarity
                signal.extend([balancing, 0, 0, balancing])
                polarity = balancing

            pulse_count = 0
            i += 4
        elif bits[i] == 0:
            signal.append(0)
            i += 1
        else:
            polarity *= -1
            signal.append(polarity)
            pulse_count += 1
            i += 1

    return signal