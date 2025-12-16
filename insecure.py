API_KEY = "sk_live_1234567890abcdef"  # hardcoded secret

def calculate(expr):
    return eval(expr)  # dangerous eval

with open(reading_path, "rb") as file:
    data = pickle.load(file)
