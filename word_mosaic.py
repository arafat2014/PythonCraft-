def create_mosaic(word, size):
    for i in range(1, size + 1):
        print((word + " ") * i)
    for i in range(size - 1, 0, -1):
        print((word + " ") * i)

if __name__ == "__main__":
    word = input("Enter a word: ")
    size = int(input("Enter the size of the mosaic: "))
    create_mosaic(word, size)
