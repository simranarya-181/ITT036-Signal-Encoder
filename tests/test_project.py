
from data_generator import generate_random_bits, generate_bits_with_zeros
from palindrome import longest_palindrome
from line_coding import encode
from decoding import decode_nrz_l, decode_nrz_i, decode_manchester
from modulation import pcm_encode, pcm_decode, delta_encode, delta_decode


def test_random_bits():
    bits = generate_random_bits(100)
    assert len(bits) == 100
    assert all(bit in (0, 1) for bit in bits)


def test_zero_runs():
    assert "0000" in "".join(map(str, generate_bits_with_zeros(20, 4)))
    assert "00000000" in "".join(
        map(str, generate_bits_with_zeros(20, 8))
    )


def test_palindrome():
    assert longest_palindrome([1, 0, 1, 1, 0, 1]) == "101101"


def test_basic_line_decoders():
    bits = [1, 0, 1, 1, 0, 0, 1]

    assert decode_nrz_l(encode(bits, "NRZ-L")) == bits
    assert decode_nrz_i(encode(bits, "NRZ-I")) == bits
    assert decode_manchester(encode(bits, "Manchester")) == bits


def test_pcm():
    samples = [-1.0, -0.5, 0.0, 0.5, 1.0]
    bits, _ = pcm_encode(samples, bits_per_sample=4)
    decoded = pcm_decode(bits, bits_per_sample=4)

    assert len(decoded) == len(samples)
    assert all(-1 <= sample <= 1 for sample in decoded)


def test_delta_modulation():
    samples = [-0.5, 0.0, 0.5, 0.25, -0.25]
    bits, _ = delta_encode(samples, step_size=0.2)
    decoded = delta_decode(bits, step_size=0.2)

    assert len(decoded) == len(samples)
