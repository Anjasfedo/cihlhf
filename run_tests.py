from tests import test_demo, test_capacity, test_security, test_quality

def main():
    try:
        test_demo.run_test()
        test_capacity.run_test()
        test_security.run_test()
        test_quality.run_test()
        
    except Exception as e:
        print(e)
        return
    
if __name__ == "__main__":
    main()