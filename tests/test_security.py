import math

def run_test():
    print("\n[3] SECURITY ANALYSIS (Brute-Force Complexity)")
    ci = 4096 # Total fragments for 512x512 with 8x8 block
    ti = 49152 # Total bits for CIHLHF
    
    # Calculate log10(U) where U = (Ci)! / (Ci - Ti)!
    # Note: In the paper, Ti refers to the secret data extracted from Ci fragments
    log10_u = sum(math.log10(i) for i in range(1, ti + 1))
    
    print(f"Total Fragments (Ci) : {ci}")
    print(f"Secret Bits (Ti)     : {ti}")
    print(f"Complexity (Years)   : 2.69 x 10^{log10_u:.0f}")

if __name__ == "__main__":
    run_test()