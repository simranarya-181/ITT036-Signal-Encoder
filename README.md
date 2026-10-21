# ITT 036: Digital Signal Encoder & Decoder

An interactive digital communications suite written in Python for line coding, scrambling, analog modulation (PCM & Delta Modulation), and line signal decoding.

## Features
* **Digital Data Generator**: Generates random bit streams, custom zero-run patterns (4 or 8 consecutive zeros), or accepts user-defined bit sequences.
* **Longest Palindrome Finder**: Calculates the longest palindromic binary sequence using Manacher's Algorithm in $\mathcal{O}(N)$ time.
* **Line Coding**: Encodes bitstreams using NRZ-L, NRZ-I, Manchester, Differential Manchester, and AMI[cite: 1].
* **Scrambling**: Implements North American B8ZS ($000VB0VB$) and European HDB3 ($000V$ / $B00V$) scrambling on AMI streams to prevent loss of clock synchronization[cite: 1].
* **Analog Modulation**:
  * **Pulse Code Modulation (PCM)**: 4-bit uniform quantization and binary word encoding[cite: 1].
  * **Delta Modulation (DM)**: Step-tracking encoder and staircase decoder reconstruction[cite: 1].
* **Line Signal Decoder**: Decodes line-coded waveforms back into digital bitstreams by analyzing signal levels and state transitions[cite: 1].
* **Visualization**: Displays step waveforms and staircase plots using Matplotlib[cite: 1].

## Repository Structure
```text
.
├── main.py              # Interactive CLI application and workflow controller[cite: 1]
├── data_generator.py    # Bitstream generation and zero-run insertion[cite: 1]
├── line_coding.py       # Encoder dispatch dictionary and line schemes[cite: 1]
├── scrambling.py        # B8ZS and HDB3 scrambling algorithms[cite: 1]
├── decoding.py          # Voltage level and signal parameter decoders[cite: 1]
├── modulation.py        # PCM and Delta Modulation encoders/decoders[cite: 1]
├── palindrome.py        # Manacher's algorithm for O(N) palindrome detection[cite: 1]
├── plotting.py          # Signal step-plots and staircase rendering[cite: 1]
├── specification.md     # One-page specification report for submission[cite: 1]
├── requirements.txt     # Environment dependencies[cite: 1]
└── tests/
    └── test_project.py  # Unit test suite[cite: 1]