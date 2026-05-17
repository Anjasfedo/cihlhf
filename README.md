# Coverless Steganography CIHLHF

This repository provides a Python implementation of the **CIHLHF** (*Coverless Information Hiding based on the Lowest and Highest Image Fragments*) method. 

CIHLHF is an evolution of the CIHMSB algorithm. While CIHMSB uses the average intensity of an image fragment, CIHLHF extracts features from the **Minimum (L)** and **Maximum (H)** pixel values within each fragment. This approach allows for a significantly higher hiding capacity—up to **3 times greater** than CIHMSB—while maintaining perfect visual quality and robust security.

### Academic Attribution

The code in this repository is an independent implementation based on the following research paper:

"A High-Capacity Coverless Information Hiding Based on the Lowest and Highest Image Fragments" by Kurnia Anggriani, Shu-Fen Chiou, Nan-I Wu, and Min-Shiang Hwang (Electronics 2023, 12, 395).
DOI: [10.3390/electronics12020395](https://doi.org/10.3390/electronics12020395)

### Key Features

- **Triple Capacity**: PACKS 3x more data than traditional CIHMSB by utilizing dual-value mapping.
- **Perfect Fidelity**: Achieves an **infinite PSNR** and **SSIM of 1.0** because the cover image is never modified.
- **Enhanced Security**: Uses a secret mapping key ($Z$) to randomize fragment selection, making brute-force attacks mathematically infeasible.

### Repository Structure

- `assets/`: Directory for cover images (e.g., `cover.png`).
- `src/`: Contains the core `cihlhf.py` module.
- `tests/`: Modular test suite for capacity, security, quality, and functional demos.
- `main.py`: A quickstart example of the embedding and extraction process.
- `run_tests.py`: Master script to run the full paper replication benchmark.

### Requirements

- Python 3.x
- NumPy
- Pillow (PIL)

### How to Run

1. Clone this repository.
2. Place a grayscale or RGB image named `cover.png` in the `assets/` folder.
3. Run the demonstration script:
   ```bash
   python main.py
   ```

*Developed for academic research purposes. Last updated May 2026.*
