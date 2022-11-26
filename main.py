import random
def main():
    list = [0]*20
    list_every_2 = []
    list_every_3 = []
    list_back = []
    for i in range (0,20):
        list[i]= random.randint(0,500)
    for i in range (1,20,2):
        list_every_2.append(list[i])
    for i in range (2,20,3):
        list_every_3.append(list[i])
    for i in range (19,-1,-1):
        list_back.append(list[i])
    print('Начальный список:', list)
    print('C каждым 2м элементом:', list_every_2)
    print('C каждым 3м элементом:', list_every_3)
    print('В обратном порядке:', list_back)
main()

