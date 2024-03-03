clavier_dict = { "2" : 'a',"22" : 'b',"222" : 'c',"3" : 'd',"33" : 'e',"333" : 'f',"4" : 'g',"44" : 'h',"444" : 'i',"5" : 'j',"55" : 'k',"555" : 'l',"6" : 'm',"66" : 'n',"666" : 'o',"7" : 'p',"77" : 'q',"777" : 'r',"7777" : 's',"8" : 't',"88" : 'u',"888" : 'v',"9" : 'w',"99" : 'x',"999" : 'y',"9999" : 'z',"a" : '0',"b" : '1',"c" : '2',"d" : '3',"e" : '4',"f" : '5',"g" : '6',"h" : '7',"i" : '8',"j" : '9',
}

def saisi():
    saisi = input("veuillez saisir une phrase : ")
    phrase_trans = ""
    for i in range(len(saisi) - 1):
        car_to_check = ""
        if saisi[i - 1] == saisi[i] and saisi[i + 1] ==saisi[i] :
            car_to_check= saisi[i]*3
            i = i + 2
        elif saisi[i]==saisi[i + 1] : 
                car_to_check = saisi[i]*2
        else :
            car_to_check = saisi[i]
            
    # car_to_check = saisi[i]
        print(car_to_check)
    #     for key in clavier_dict.keys():
    #         if car_to_check == key :
    #             phrase_trans += clavier_dict[key]
    #             print(phrase_trans)
    # print(phrase_trans)


saisi()