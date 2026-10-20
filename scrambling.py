
def scramble_b8zs(bits, initial_polarity=1):
    """Encode bits using AMI with B8ZS substitution.

    Returns one signal level per input bit.
    """
    signal = []
    polarity = -initial_polarity
    i = 0

    while i < len(bits):
        if bits[i:i + 8] == [0] * 8:
            # B8ZS: 000VB0VB
            # V = bipolar violation; B = normal AMI pulse.
            last = polarity
            signal.extend([0, 0, 0, last, -last, 0, -last, last])
            polarity = last
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
    """Encode bits using AMI with HDB3 substitution."""
    signal = []
    polarity = -initial_polarity
    pulse_count = 0
    i = 0

    while i < len(bits):
        if bits[i:i + 4] == [0] * 4:
            if pulse_count % 2 == 1:
                # 000V: violation has the same polarity
                # as the preceding nonzero pulse.
                violation = polarity
                signal.extend([0, 0, 0, violation])
                polarity = violation
            else:
                # B00V: B is a balancing pulse and V
                # repeats its polarity as a violation.
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
