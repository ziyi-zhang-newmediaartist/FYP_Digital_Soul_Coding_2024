def break_string_into_chunks(text, chunk_size=10):
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Example usage:
text = "This is a sample string that we want to break into chunks of ten words each."
chunks = break_string_into_chunks(text)
for chunk in chunks:
    print(chunk)
