text_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
first_text_list = text_list.pop(0)
first_text_list = first_text_list.split(' ')
first_name = first_text_list.pop()
first_name = first_name.title()
second_text_list = text_list.pop(0)
second_text_list = second_text_list.split(' ')
second_name = second_text_list.pop()
second_name = second_name.title()
third_text_list = text_list.pop(0)
third_text_list = third_text_list.split(' ')
third_name = third_text_list.pop()
third_name = third_name.title()
fourth_text_list = text_list.pop(0)
fourth_text_list = fourth_text_list.split(' ')
fourth_name = fourth_text_list.pop()
fourth_name = fourth_name.title()
first_message = f'Привет, {first_name}!'
print(first_message)
second_message = f'Привет, {second_name}!'
print(second_message)
third_message = f'Привет, {third_name}!'
print(third_message)
fourth_message = f'Привет, {fourth_name}!'
print(fourth_message)

# понимаю что можно как-то проще все это сделать, но, по крайней мере, все работает