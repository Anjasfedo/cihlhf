import numpy as np

class CIHLHF:
    def __init__(self, fragment_size=8, first_msb_bits=1, second_msb_bits=1, seed=None):
        self.fragment_size = fragment_size
        self.first_msb_bits = first_msb_bits
        self.second_msb_bits = second_msb_bits
        self.seed = seed

    def _text_to_bin(self, text):
        binary_list = []
        for char in text:
            bin_char = format(ord(char), '07b')
            for bit in bin_char:
                binary_list.append(int(bit))
        return binary_list

    def _bin_to_text(self, binary_list):
        text = ""
        for i in range(0, len(binary_list), 7):
            chunk = binary_list[i:i+7]
            if len(chunk) < 7: break
            chunk_str = "".join(map(str, chunk))
            text += chr(int(chunk_str, 2))
        return text

    def _extract_min_max_msbs(self, image_array):
        h, w = image_array.shape
        h_trunc = h - (h % self.fragment_size)
        w_trunc = w - (w % self.fragment_size)
        
        msb_pool = []
        for i in range(0, h_trunc, self.fragment_size):
            for j in range(0, w_trunc, self.fragment_size):
                fragment = image_array[i:i+self.fragment_size, j:j+self.fragment_size]
                min_val = int(np.min(fragment)) 
                max_val = int(np.max(fragment)) 
                
                bin_min = format(min_val, '08b')
                for b in range(self.first_msb_bits):
                    msb_pool.append(int(bin_min[b]))
                
                bin_max = format(max_val, '08b')
                for b in range(self.second_msb_bits):
                    msb_pool.append(int(bin_max[b]))
        return msb_pool

    def _generate_z_key(self, capacity):
        if self.seed is None: return list(range(1, capacity + 1))
        state = np.random.get_state()
        np.random.seed(self.seed)
        z_key = np.random.permutation(np.arange(1, capacity + 1))
        np.random.set_state(state)
        return z_key.tolist()

    def embed(self, image_array, secret_text):
        secret_bits = self._text_to_bin(secret_text)
        msb_pool = self._extract_min_max_msbs(image_array)
        if len(secret_bits) > len(msb_pool):
            raise ValueError(f"Capacity {len(msb_pool)} bits is not enough.")
            
        z_key = self._generate_z_key(len(msb_pool))
        mapping_flag = [0] * len(secret_bits)
        for i in range(len(secret_bits)):
            target_index = z_key[i] - 1
            mapping_flag[i] = 1 if secret_bits[i] == msb_pool[target_index] else 0
        return mapping_flag

    def extract(self, image_array, mapping_flag):
        msb_pool = self._extract_min_max_msbs(image_array)
        z_key = self._generate_z_key(len(msb_pool))
        secret_bits = []
        for i in range(len(mapping_flag)):
            target_index = z_key[i] - 1
            t_i = 1 if mapping_flag[i] == msb_pool[target_index] else 0
            secret_bits.append(t_i)
        return self._bin_to_text(secret_bits)