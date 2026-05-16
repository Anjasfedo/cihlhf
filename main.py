import numpy as np
from PIL import Image
from src.cihlhf import CIHLHF

def run_example():
    # Load the cover image and convert to grayscale as per paper methodology
    img_pil = Image.open('assets/cover.png').convert('L')
    img_array = np.array(img_pil)

    # Initialize CIHLHF system
    # Using 12 bits per fragment (6 from Min, 6 from Max) and seed 2026
    cihlhf = CIHLHF(fragment_size=8, first_msb_bits=6, second_msb_bits=6, seed=2026)

    secret_message = "CIHLHF HIGH CAPACITY TEST 2026"
    print(f"Original Message: {secret_message}")

    # Process Embedding to generate the Mapping Flag (Ui)
    mapping_flag = cihlhf.embed(img_array, secret_message)
    print(f"Total Mapping Flag generated: {len(mapping_flag)} bits")

    # Process Extraction using the stego image and Mapping Flag
    extracted_message = cihlhf.extract(img_array, mapping_flag)
    print(f"Extracted Message: {extracted_message}")
    print(f"Match: {secret_message == extracted_message}")

if __name__ == "__main__":
    run_example()