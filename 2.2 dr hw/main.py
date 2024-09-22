n = int(input("Iltimos, bir son kiriting: "))
for i in range(n, 0, -1):
    if i > 0 :
        print(i)
    else:
        print("no")
mevalar = input("Iltimos, 5ta meva kiriting (vergul bilan ajrating): ").split(" ")
for meva in mevalar:
    if 'i' not in meva:
        print(meva)