# -*- coding: utf-8 -*-
def add_ingredient():
    #ingredients = {1: 'Булочка', 2: 'Котлета (Говядина)', 3: 'Огурчик', 4: 'Помидорчик', 5: 'Майонез', 6:'Сыр', }
    ingredients = {1: 'Булочка', 2: 'Котлета (Говядина)', 3: 'Котлета (Свинина)', 4: 'Котлета (Курица)', 5: 'Котлета (Рыба)', 6: 'Огурец', 7: 'Помидор',
            8: 'Сыр' , 9: 'Лук' , 10: 'Салат' , 11: 'Кетчуп' , 12: 'Горчица' , 13: 'Майонез'}
    ingred_input = ''
    burger = ['Булочка']
    print('Собираем бургер!\n'
          'Чтобы добавить ингредиент, введите соответствующую цифру из списка.\n')
    print('Список доступных ингредиентов:\n'
          '   1: Булочка                 6: Огурец      11: Кетчуп \n'
          '   2: Котлета (Говядина)      7: Помидор     12: Горчица\n'
          '   3: Котлета (Свинина)       8: Сыр         13: Майонез\n'
          '   4: Котлета (Курица)        9: Лук   \n'
          '   5: Котлета (Рыба)         10: Салат \n')
   
    while ingred_input != 'Закончить бургер' or (ingred_input < 0 or ingred_input > 13):
        ingred_input = input('А теперь добавим...')
        if ingred_input == '':
            print('Неверный ввод!\n'
                'Попробуйте ещё раз!\n')
            continue
        else:
            
            if ingred_input == 'Закончить бургер':
                burger.append('Булочка')
                return '\n '.join(burger)
            else:
                ingred_input = int(ingred_input)
                if ingred_input < 0 or ingred_input > 13:
                    print('Неверный ввод!\n'
                          'Попробуйте ещё раз!\n')
                    continue
                else:
                    for k, v in ingredients.items():
                        if k == ingred_input:
                            burger.append(v)

def cheesebur():
    return'\n '.join(['Булочка','Котлета (Говядина)','Сыр','Кетчуп','Горчица','Лук','Огурец','Булочка'])
    #return add_ingredient()

def double_cheesebur():
    return'\n '.join(['Булочка','Котлета (Говядина)','Сыр','Котлета (Говядина)','Сыр','Кетчуп','Горчица','Лук','Огурец','Булочка'])
    #return add_ingredient()

def my_burg():
    return add_ingredient()


def burger():
    burger_input = input('Какой бургер вы хотите заказать? \n'
                         '   1: Чизбургер\n'
                         '   2: Двойной чизбургер\n'
                         '   3: Создать рецепт своего бургера\n'
                         'Ваш выбор:')
    if int(burger_input) == 1:
         return cheesebur()
    elif int(burger_input) == 2:
         return double_cheesebur()
    else:
         return my_burg()
