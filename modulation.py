
import numpy as np


def generate_analog_signal(sample_count=32):
    """Generate a sampleable sine wave for demonstration."""
    t = np.linspace(0, 1, sample_count, endpoint=False)
    signal = np.sin(2 * np.pi * 3 * t)
    return t, signal


def pcm_encode(samples, bits_per_sample=4):
    """Uniform PCM quantization and fixed-width binary encoding."""
    if bits_per_sample < 1:
        raise ValueError("bits_per_sample must be positive.")

    levels = 2 ** bits_per_sample
    minimum, maximum = -1.0, 1.0
    clipped = np.clip(np.asarray(samples), minimum, maximum)

    indices = np.rint(
        (clipped - minimum) / (maximum - minimum) * (levels - 1)
    ).astype(int)

    quantized = minimum + indices * (
        (maximum - minimum) / (levels - 1)
    )

    bitstream = [
        int(bit)
        for index in indices
        for bit in format(index, f"0{bits_per_sample}b")
    ]

    return bitstream, quantized.tolist()


def pcm_decode(bitstream, bits_per_sample=4):
    """Recover quantized amplitudes from fixed-width PCM words."""
    if bits_per_sample < 1:
        raise ValueError("bits_per_sample must be positive.")

    if len(bitstream) % bits_per_sample != 0:
        raise ValueError("PCM bitstream has an incomplete sample.")

    levels = 2 ** bits_per_sample
    result = []

    for start in range(0, len(bitstream), bits_per_sample):
        word = bitstream[start:start + bits_per_sample]
        index = int("".join(map(str, word)), 2)

        result.append(-1.0 + index * (2.0 / (levels - 1)))

    return result


def delta_encode(samples, step_size=0.2):
    """Encode whether each sample rises or falls relative to the estimate."""
    if step_size <= 0:
        raise ValueError("step_size must be positive.")

    estimate = 0.0
    bits = []
    reconstructed = []

    for sample in samples:
        if sample >= estimate:
            bit = 1
            estimate += step_size
        else:
            bit = 0
            estimate -= step_size

        bits.append(bit)
        reconstructed.append(estimate)

    return bits, reconstructed


def delta_decode(bitstream, step_size=0.2):
    """Reconstruct a staircase from the delta modulation bits."""
    if step_size <= 0:
        raise ValueError("step_size must be positive.")

    estimate = 0.0
    reconstructed = []

    for bit in bitstream:
        if bit not in (0, 1):
            raise ValueError("Bits must be 0 or 1.")

        estimate += step_size if bit == 1 else -step_size
        reconstructed.append(estimate)

    return reconstructed
