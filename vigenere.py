
alphabets = "abcdefghijklmnopqrstuvwxyz"

def encrypt(p, k):
    c = ""
    kpos = []
    for x in k:

        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) + kpos[i]
      if pos > 25:
          pos = pos-26
      c += alphabets[pos].capitalize()
      i +=1
    return c

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 26
      p += alphabets[pos].lower()
      i +=1
    return p

def menu():
        choice = 0
        while choice != 'q':
            print("")
            print("Do you want to [enc]rypt [dec]rypt or [q]uit?")
            choice = input("Your choice: ").lower()

            if choice == "enc":
                p = input("Enter plain text: ").lower()
                k = input("Enter key: ").lower()
                p = p.replace(" ", "")
                k = k.replace(" ", "")
                if p.isalpha() and k.isalpha():
                    c = encrypt(p,k)
                    print("Chiper text is: ", c)
                else:
                    print("Text and key has to be characters")

            elif choice == "dec":
                c = input("Enter chiper text: ").lower()
                k = input("Enter key: ").lower()
                c = c.replace(" ", "")
                k = k.replace(" ", "")
                if c.isalpha() and k.isalpha():
                    p = decrypt(c, k)
                    print("Plain text is: ", p)
                else:
                    print("Chiper and key has to be characters")

            elif choice == 'q':
                print("Bye")
                exit()



if __name__ == "__main__":
    menu()