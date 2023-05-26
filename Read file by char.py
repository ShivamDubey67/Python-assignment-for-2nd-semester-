file = open('file.txt', 'r')

 

while True:

    char = file.read(1)         

    if not char:

        break

         

    print(char)
