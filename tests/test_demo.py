import numpy as np
from src.cihlhf import CIHLHF

def run_test():
    print("\n[1] CIHLHF EXPERIMENT DEMO")
    img_dummy = np.random.randint(0, 256, (512, 512), dtype=np.uint8)
    cihlhf = CIHLHF(fragment_size=8, first_msb_bits=6, second_msb_bits=6, seed=2026)
    
    secret_message = "CIHLHF_REPLICATION_2026"
    mapping_flag = cihlhf.embed(img_dummy, secret_message)
    extracted = cihlhf.extract(img_dummy, mapping_flag)
    
    print(f"Original Message: {secret_message}")
    print(f"Extraction Match: {secret_message == extracted}")

if __name__ == "__main__":
    run_test()