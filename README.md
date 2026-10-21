# PROJECT REPORT
# ITT036: Digital Signal Encoder and Decoder

A menu-driven Python program demonstrating binary-data generation, longest-palindrome detection, digital line coding, AMI scrambling options, PCM and Delta Modulation, decoding, and signal visualization.

---

## 1. Purpose and Scope
A menu-driven Python program demonstrating binary-data generation, longest-palindrome detection, digital line coding, AMI scrambling options, PCM and Delta Modulation, decoding, and signal visualization.

---

## 2. Language and Libraries
* **Language**: Python 3
* **Libraries**: NumPy for numerical arrays/calculations; Matplotlib for signal plots; pytest for automated tests.
* **Architecture**: The implementation is separated into modules for data generation, palindrome processing, line coding, scrambling, modulation, decoding, plotting, and the main workflow.
* **Version Note**: Confirm package versions in the local environment if the submission requires exact version numbers.

---

## 3. Main Functionality
* **Digital Workflow**: Generates a bit sequence, reports its longest palindromic substring, and lets the user select NRZ-L, NRZ-I, Manchester, Differential Manchester, or AMI. AMI offers B8ZS or HDB3 scrambling.
* **Analog Workflow**: Generates an analog signal and demonstrates PCM and Delta Modulation encoding/reconstruction, with plots for the resulting signals.

---

## 4. Assumptions and Conventions
* **Input Representation**: Input data is represented as binary values 0 and 1.
* **Line-Code Levels**: Line-code encoders use discrete signal levels (typically -1, 0, +1).
* **Manchester Scheme**: Manchester-family encoders represent each bit using two half-bit levels.
* **Decoder Alignment**: Decoder initial-level/polarity settings must match the encoder settings.
* **Reconstruction**: PCM reconstruction is quantized/approximate, and Delta Modulation reconstructs a staircase approximation.
* **Polarity Rules**: B8ZS/HDB3 behavior depends on pulse-polarity conventions; verify these cases with reference vectors before claiming exhaustive correctness.

---

## 5. How to Run
* **Terminal Launch**: Open a terminal in the project folder and run `python main.py`.
* **Automated Tests**: To execute automated tests, run `python -m pytest -v`.
* **Dependencies**: Install dependencies if missing, for example `python -m pip install numpy matplotlib pytest`.
* **Requirements File**: If the project includes a requirements file, prefer `python -m pip install -r requirements.txt`.

---

## 6. Testing Status
The reported test run passed six tests: random-bit generation, zero-run behavior, palindrome detection, selected basic line decoders, PCM, and Delta Modulation. This is not exhaustive coverage of all inputs or all scrambling/descrambling patterns.

---

## 7. References
* **Course Material**: Class Notes and Lecture Presentations (Digital Transmission, Line Coding, Scrambling, and Modulation concepts).
* **Python Documentation**: docs.python.org/3/
* **NumPy Documentation**: numpy.org/doc/
* **Matplotlib Documentation**: matplotlib.org/stable/
* **pytest Documentation**: docs.pytest.org/

---

## 8. Repository Structure
```text
.
├── main.py              # Interactive CLI application and workflow controller
├── data_generator.py    # Bitstream generation and zero-run insertion
├── line_coding.py       # Encoder dispatch dictionary and line schemes
├── scrambling.py        # B8ZS and HDB3 scrambling algorithms
├── decoding.py          # Voltage level and signal parameter decoders
├── modulation.py        # PCM and Delta Modulation encoders/decoders
├── palindrome.py        # Manacher's algorithm for O(N) palindrome detection
├── plotting.py          # Signal step-plots and staircase rendering
├── specification.md     # One-page specification report for submission
├── requirements.txt     # Environment dependencies
└── tests/
    └── test_project.py  # Unit test suite
```
---

## 9. Contributors
* **Sakshi** (2024BITE023)
* **Harmandeep kour** (2024BITE038)
* **Simran** (2024BITE041)    