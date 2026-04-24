def add(a, b):
    return a + b

def save_result():
    with open("output.txt", "w") as f:
        f.write("CI/CD is working!")

if __name__ == "__main__":
    save_result()