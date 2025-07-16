def analyze_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    lines = text.splitlines()
    words = text.split()
    print(f"Lines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {len(text)}")

# Example
analyze_text('sample.txt')
