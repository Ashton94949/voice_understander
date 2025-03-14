from claude_module import query_claude

def process_query(text):
    response = query_claude(text)
    return response
