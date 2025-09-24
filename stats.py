def get_number_of_words(text):
    split_text = text.split()
    count_text = len(split_text)
    return count_text

def get_number_of_characters(text):
    characters = {}
    split_text = text.split()
    for c in split_text:
        new_text = list(c)
        for l in new_text:
            lower_ch = l.lower()
            if lower_ch not in characters:
                characters[lower_ch] = 0
            characters[lower_ch] += 1
    return characters

def get_dictionary(dict):
    dic_list = []
    for i,value in dict.items():
        new_dic = {"char":i,"num":value}
        dic_list.append(new_dic)
    return dic_list

def sort_dic(item):
    return item["num"]
