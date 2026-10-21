# Specification Report: ITT 036 Programming Assignment 1

## 1. Environment & Dependencies
* **Language**: Python 3.10+
* **Libraries Used**: `numpy` (signal sampling & numerical arrays), `matplotlib` (waveform plotting), `random` (data generation), `unittest` / `pytest` (verification).
* **Execution Constraint**: Built entirely in standard Python without restricted environments (e.g., MATLAB, Scilab, GNU Octave).

## 2. Architecture & Algorithms
* `data_generator.py`: Generates uniform random bits, zero-run sequences (4 or 8 zeros), and validates custom binary user input.
* `palindrome.py`: Computes the longest palindromic binary sequence using **Manacher's Algorithm** in optimal $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space complexity.
* `line_coding.py`: Encodes bitstreams (NRZ-L, NRZ-I, Manchester, Differential Manchester, AMI) using a dictionary lookup dispatcher (`ENCODERS`), avoiding monolithic conditional statements.
* `scrambling.py`: Implements North American B8ZS ($000VB0VB$) and European HDB3 ($000V$ / $B00V$) scrambling for AMI.
* `modulation.py`: Implements PCM (4-bit uniform quantization) and Delta Modulation (DM) encoders and decoders.
* `decoding.py` & `main.py`: Reconstructs digital bitstreams by analyzing signal level parameters and voltage transitions.
* `plotting.py`: Visualizes step-post line coding waveforms and staircase modulation plots.

## 3. Assumptions & Default Parameters
1. **Initial Signal State**: NRZ-I and Differential Manchester start at $+1\text{ V}$. AMI / Scrambling initial polarity starts at $+1\text{ V}$.
2. **PCM Encoding**: Uniform 4-bit linear quantization spanning the amplitude range $[-1.0\text{ V}, +1.0\text{ V}]$.
3. **Delta Modulation**: Fixed step size $\Delta = 0.2\text{ V}$ with initial estimate $0.0\text{ V}$.

## 4. Execution Instructions
```bash
# Install dependencies
pip install -r requirements.txt

# Launch interactive CLI encoder/decoder
python main.py

# Run unit tests
python -m unittest tests/test_project.py