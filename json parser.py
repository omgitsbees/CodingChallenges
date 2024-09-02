import re

def tokenize(json_string):
    # Regular expression to match strings, numbers, and JSON special characters
    token_pattern = r'\"(.*?)\"|\-?\d+\.\d+|\-?\d+|true|false|null|[{}\[\]:,]'
    tokens = re.findall(token_pattern, json_string)
    tokens = [t for t in tokens if t]  # Remove any empty tokens
    print("Tokens:", tokens)  # Debug: Print tokens
    return tokens

def parse_value(tokens):
    if not tokens:
        raise ValueError("No tokens left to parse.")
        
    token = tokens.pop(0)
    print("Parsing token:", token)  # Debug: Print the current token

    if token == '{':
        obj = {}
        while tokens[0] != '}':
            key = parse_value(tokens)
            assert tokens.pop(0) == ':'
            value = parse_value(tokens)
            obj[key] = value
            if tokens[0] == '}':
                break
            assert tokens.pop(0) == ','
        tokens.pop(0)  # remove '}'
        return obj
    
    elif token == '[':
        array = []
        while tokens[0] != ']':
            array.append(parse_value(tokens))
            if tokens[0] == ']':
                break
            assert tokens.pop(0) == ','
        tokens.pop(0)  # remove ']'
        return array
    
    elif token == 'true':
        return True
    
    elif token == 'false':
        return False
    
    elif token == 'null':
        return None
    
    elif token.startswith('"') and token.endswith('"'):
        return token[1:-1]  # remove the surrounding quotes
    
    else:
        try:
            if '.' in token:
                return float(token)
            else:
                return int(token)
        except ValueError:
            raise ValueError(f"Unexpected token: {token}")

def parse_json(json_string):
    tokens = tokenize(json_string)
    return parse_value(tokens)

# Example usage
if __name__ == "__main__":
    # Test cases
    json_data_1 = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
    json_data_2 = '[1, 2, 3, {"a": 1, "b": [true, false, null]}, "end"]'

    parsed_data_1 = parse_json(json_data_1)
    parsed_data_2 = parse_json(json_data_2)

    print("Parsed Data 1:")
    print(parsed_data_1)
    print("\nParsed Data 2:")
    print(parsed_data_2)
