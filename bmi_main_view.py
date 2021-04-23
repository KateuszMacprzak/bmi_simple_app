import easygui
w=easygui.buttonbox('Chcesz sprawdzić swoje BMI', 'Your BMI status',['Tak','Nie','Zamknij program'])
if w=='Tak':
    weight = int(easygui.enterbox('Podaj wagę: '))
    height = float(easygui.enterbox('Podaj wzrost w centymentrach: '))
    result = weight/(height*height)
    if result < 15 :
        easygui.msgbox(f'Twoje BMI wynosi {result} - wygłodzenie')
    if result > 15.1 and result <= 17.4:
        easygui.msgbox(f'Twoje BMI wynosi {result} - wychudzenie')
    if result > 17.5 and result <=18.5:
        easygui.msgbox(f'Twoje BMI wynosi {result} - niedowaga')
    if result > 18.5 and result <= 24.9:
        easygui.msgbox(f'Twoje BMI wynosi {result} - wartość prawidłowa')
    if result > 25 and result <= 29.9:
        easygui.msgbox(f'Twoje BMI wynosi {result} - nadwaga')
    if result > 30.0 and result <= 34.9:
        easygui.msgbox(f'Twoje BMI wynosi {result} - I stopień otyłości')
    if result > 35.0 and result <= 39.9:
        easygui.msgbox(f'Twoje BMI wynosi {result} - II stopień otyłości')
    if result > 40.0:
        easygui.msgbox(f'Twoje BMI wynosi {result} - III stopień otyłości')


