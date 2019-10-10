def compute_result(data):
    return data["a"] * data["b"]

def main():
    data = {"a": 2, "b": "3"}
    result = compute_result(data)
    print(result)

main()
