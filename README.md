# ITT036: Digital Signal Encoder and Decoder
# PROJECT REPORT
A menu-driven Python program demonstrating binary-data generation, longest-palindrome detection, digital line coding, AMI scrambling options, PCM and Delta Modulation, decoding, and signal visualization.

---

## 1. Purpose and Scope
A menu-driven Python program demonstrating binary-data generation, longest-palindrome detection, digital line coding, AMI scrambling options, PCM and Delta Modulation, decoding, and signal visualization[cite: 1].

---

## 2. Language and Libraries
* **Language**: Python 3[cite: 1]
* **Libraries**: NumPy for numerical arrays/calculations; Matplotlib for signal plots; pytest for automated tests[cite: 1].
* **Architecture**: The implementation is separated into modules for data generation, palindrome processing, line coding, scrambling, modulation, decoding, plotting, and the main workflow[cite: 1].
* **Version Note**: Confirm package versions in the local environment if the submission requires exact version numbers[cite: 1].

---

## 3. Main Functionality
* **Digital Workflow**: Generates a bit sequence, reports its longest palindromic substring, and lets the user select NRZ-L, NRZ-I, Manchester, Differential Manchester, or AMI[cite: 1]. AMI offers B8ZS or HDB3 scrambling[cite: 1].
* **Analog Workflow**: Generates an analog signal and demonstrates PCM and Delta Modulation encoding/reconstruction, with plots for the resulting signals[cite: 1].

---

## 4. Assumptions and Conventions
* **Input Representation**: Input data is represented as binary values 0 and 1[cite: 1].
* **Line-Code Levels**: Line-code encoders use discrete signal levels (typically -1, 0, +1)[cite: 1].
* **Manchester Scheme**: Manchester-family encoders represent each bit using two half-bit levels[cite: 1].
* **Decoder Alignment**: Decoder initial-level/polarity settings must match the encoder settings[cite: 1].
* **Reconstruction**: PCM reconstruction is quantized/approximate, and Delta Modulation reconstructs a staircase approximation[cite: 1].
* **Polarity Rules**: B8ZS/HDB3 behavior depends on pulse-polarity conventions; verify these cases with reference vectors before claiming exhaustive correctness[cite: 1].

---

## 5. How to Run
* **Terminal Launch**: Open a terminal in the project folder and run `python main.py`[cite: 1].
* **Automated Tests**: To execute automated tests, run `python -m pytest -v`[cite: 1].
* **Dependencies**: Install dependencies if missing, for example `python -m pip install numpy matplotlib pytest`[cite: 1].
* **Requirements File**: If the project includes a requirements file, prefer `python -m pip install -r requirements.txt`[cite: 1].

---

## 6. Testing Status
The reported test run passed six tests: random-bit generation, zero-run behavior, palindrome detection, selected basic line decoders, PCM, and Delta Modulation[cite: 1]. This is not exhaustive coverage of all inputs or all scrambling/descrambling patterns[cite: 1].

---

## 7. Repository Structure
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