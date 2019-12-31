class anagram:
    # def __init__(self, first_string, second_string):
    #     first_string = first_string
    #     second_string = second_string

    def anagram_func(self, anagram_firststring,anagram_secondstring):
        first_string = anagram_firststring.replace(' ', '').lower()
        second_string = anagram_secondstring.replace(' ', '').lower()
        skip_list = []        

        for i in range(len(first_string)):
            l=0
            for j in range(len(second_string)):
                if first_string[i] == second_string[j]:                    
                    for k in range(len(skip_list)):
                        if skip_list[k] == j:
                            l=1
                    if l == 0:
                        skip_list.append(j)

        if len(skip_list) == len(second_string):
            print(anagram_firststring,",",anagram_secondstring, "are anagram")
        else:
            print(anagram_firststring,",",anagram_secondstring, "are not anagram")

obj1 = anagram()
obj1.anagram_func("Las Vegas", "Salvages")
obj1.anagram_func("Fourth of July", "Joyful Fourth")
obj1.anagram_func("Stressed", "Desserts")
obj1.anagram_func("aa", "bb")
