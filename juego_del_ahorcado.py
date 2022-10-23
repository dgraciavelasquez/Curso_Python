def read():
    palabras = []
    with open(".\archivos\numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabras.append((line))
    print(palabras)

def run():
    read()

if __name__ == "__main__":
    run()