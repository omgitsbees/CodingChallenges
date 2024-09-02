import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    return Counter(text)

def build_huffman_tree(freq_table):
    priority_queue = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0]  # Ensure the root node is returned

def generate_huffman_codes(root, current_code='', codes=defaultdict()):
    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        generate_huffman_codes(root.left, current_code + '0', codes)
        generate_huffman_codes(root.right, current_code + '1', codes)
    return codes

def encode(text, codes):
    return ''.join(codes[char] for char in text)

def decode(encoded_text, root):
    decoded_chars = []
    current_node = root
    
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_chars.append(current_node.char)
            current_node = root
    
    return ''.join(decoded_chars)

# Example usage
if __name__ == "__main__":
    text = "this is an example for huffman encoding"
    
    # Build frequency table
    freq_table = build_frequency_table(text)
    print("Frequency Table:", freq_table)
    
    # Build Huffman Tree
    root = build_huffman_tree(freq_table)  # Ensure the root is correctly assigned
    
    # Generate Huffman Codes
    codes = generate_huffman_codes(root)
    print("Huffman Codes:", codes)
    
    # Encode the text
    encoded_text = encode(text, codes)
    print("Encoded Text:", encoded_text)
    
    # Decode the text
    decoded_text = decode(encoded_text, root)
    print("Decoded Text:", decoded_text)
