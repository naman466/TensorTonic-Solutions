def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    step = chunk_size - overlap
    n = len(tokens)
    chunks = []
    
    i = 0
    while i < n:
        chunk = tokens[i:i + chunk_size]
        chunks.append(chunk)
        
        # last chunk if end of tokens
        if i + chunk_size >= n:
            break
        
        i += step
    
    return chunks
    
    return chunks
