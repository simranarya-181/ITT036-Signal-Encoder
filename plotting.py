
import matplotlib.pyplot as plt


def plot_line_signal(bits, signal, scheme, samples_per_bit):
    """
    Plot a line-coded signal.
    samples_per_bit is 1 for NRZ/AMI and 2 for Manchester schemes.
    """
    x = []
    y = []

    for i, level in enumerate(signal):
        x.extend([i, i + 1])
        y.extend([level, level])

    plt.figure(figsize=(max(9, len(bits) * 0.7), 3.5))
    plt.plot(x, y, linewidth=2, drawstyle="steps-post")
    plt.axhline(0, linewidth=0.8)
    plt.yticks([-1, 0, 1])
    plt.xticks(
        range(0, len(signal) + 1),
        range(0, len(signal) + 1)
    )
    plt.grid(True, alpha=0.3)
    plt.xlabel("Time (bit intervals or half-bit intervals)")
    plt.ylabel("Voltage level")
    plt.title(f"{scheme} Encoding | Input: {''.join(map(str, bits))}")
    plt.tight_layout()
    plt.show()


def plot_staircase(time_values, values, title):
    plt.figure(figsize=(9, 3.5))
    plt.step(time_values, values, where="post")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
