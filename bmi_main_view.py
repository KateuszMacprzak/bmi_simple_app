def cm_to_metres(given_height):
    return given_height/100

import easygui
w=easygui.buttonbox('Chcesz sprawdzić swoje BMI', 'Your BMI status',['Tak','Nie','Zamknij program'])
if w=='Tak':
    weight = int(easygui.enterbox('Podaj wagę: '))
    height = float(easygui.enterbox('Podaj wzrost w centymentrach: '))
    if height<3:
        height = cm_to_metres(height)
    else:
        height = height
    result =  weight/(height**2)
    