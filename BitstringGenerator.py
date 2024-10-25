
"""
Generate all possible bitstrings of a specified length.

Args: (int) length of bitstring
Returns: (list) list of bitstrings
"""
def generate_bitstrings(length):
    return [[int(bit) for bit in f"{i:0{length}b}"] for i in range(2 ** length)]


"""
Filter bitstrings starting with a specified prefix.

Args: (list) list of bitstrings, (str) prefix
Returns: (list) list of bitstrings
"""
def filter_start_bitstrings(bitstrings, prefix):
    prefix_list = [int(bit) for bit in prefix]
    filtered_bitstrings = [bits for bits in bitstrings if bits[:len(prefix_list)] != prefix_list]
    return filtered_bitstrings

"""
Filter bitstrings ending with a specified suffix.

Args: (list) list of bitstrings, (str) suffix
Returns: (list) list of bitstrings
"""
def filter_end_bitstrings(bitstrings, suffix):
    suffix_list = [int(bit) for bit in suffix]
    filtered_bitstrings = [bits for bits in bitstrings if bits[-len(suffix_list):] != suffix_list]
    return filtered_bitstrings

"""
Filter bitstrings containing any specified binary pattern as a subset.

Args: (list) list of bitstrings, (str) subset
Returns: (list) list of bitstrings
"""
def filter_subsets(bitstrings, subset):
    # Convert subset to a list of integers for easy comparison
    subset_list = [int(bit) for bit in subset]
    subset_len = len(subset_list)
    
    # Filter out bitstrings that contain the subset anywhere within them
    filtered_bitstrings = [
        bits for bits in bitstrings
        if not any(bits[i:i + subset_len] == subset_list for i in range(len(bits) - subset_len + 1))
    ]
    
    return filtered_bitstrings


"""
Display the bitstrings and their count.

Args: (list) list of bitstrings, (int) length of bitstring
Returns: None
"""
def display_bitstrings(bitstrings, length):
    bitstring_str = ', '.join([f"{{{', '.join(map(str, bits))}}}" for bits in bitstrings])
    print(f"B_{length} = {bitstring_str}")
    print(f"|B_{length}| = {len(bitstrings)}")
