def run_test():
    print("\n[2] HIDING CAPACITY ANALYSIS")
    img_size = 512
    frag_size = 8
    
    total_fragments = (img_size // frag_size) ** 2
    cihmsb_cap = total_fragments * 4
    cihlhf_cap = total_fragments * 12
    
    print(f"Total Fragments   : {total_fragments}")
    print(f"CIHMSB Capacity   : {cihmsb_cap} bits")
    print(f"CIHLHF Capacity   : {cihlhf_cap} bits")
    print(f"Improvement Factor: {cihlhf_cap / cihmsb_cap}x")

if __name__ == "__main__":
    run_test()