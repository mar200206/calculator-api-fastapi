history = []

def save_record(a, b, operation, result):
    history.append({
        'a': a,
        'b': b,
        'operation': operation,
        'result': result
    })

def get_history():
    return history
