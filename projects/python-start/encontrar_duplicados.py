import os
import hashlib

def main():
    dictionary = {}
    for entry in os.scandir('imagenes/results'):
        file = open(f"imagenes/results/{entry.name}", "rb")
        summary = hashlib.new('sha512')
        summary.update(file.read())
        digest = summary.hexdigest()
        print(digest)
        if digest not in dictionary:
            dictionary[digest]=0
        else: 
            dictionary[digest]= dictionary[digest]+1
        file.close()
    print(dictionary)

   
if __name__ == "__main__":
    main()
    pass

