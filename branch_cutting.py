#!utf-8
def branch_cutting(threshold=0.3):
    with open("data/input_data0716.csv",'r',encoding='utf-8') as f:
        with open('data/edges.csv','a', encoding= 'utf-8') as f2:
            cont = f.readline()
            temp = cont.split(",")
            while cont:
                if temp[2] < threshold:
                    f2.write(cont)
                cont = f.readline()

th = input("threshold:   ") 
branch_cutting(th)




