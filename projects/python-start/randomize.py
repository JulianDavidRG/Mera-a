import os
import os.path
import random
import base64

def main():
    imagenes = []
    for entry in os.scandir('imagenes'):
        if entry.is_file():
            imagenes.append(entry.name)

    for i in range(5000):
        name =  str(base64.urlsafe_b64encode(random.randbytes(64)))
        selected = random.choice(imagenes)
        with open(f"imagenes/{selected}", "rb") as ifile:
            with open(f"imagenes/results/{name}.png", "wb") as ofile:
                ofile.write(ifile.read())
    pass

if __name__ == "__main__":
    main()
    pass