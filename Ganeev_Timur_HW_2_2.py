text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#text_list[1] = '"05"'     # так код будет короче
#text_list[-2] = '"+05"'
#text_list[3] = '"17"'
text_list[1] = '05'     # так по заданию правильней
text_list[-2] = '+05'
text_list.insert(1, '"')
text_list.insert(3, '"')
text_list.insert(5, '"')
text_list.insert(7, '"')
text_list.insert(-1, '"')
text_list.insert(-3, '"')
cut_text_list = ' '.join(text_list)
print(cut_text_list)