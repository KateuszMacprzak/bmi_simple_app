import easygui
import pygame
import time
def cm_to_m(given_value:int):
    if given_value<3:
        return given_value
    else:
        return given_value/100

def show_image():
    plot = pygame.display.set_mode([640, 480])
    pygame.display.set_caption('BMI w Polsce')
    obrazek = pygame.image.load('poland_bmi.png')
    plot.blit(obrazek, [0, 0])
    pygame.display.flip()
    time.sleep(3)
def check_bmi(given_weight, given_height):
    result = given_weight / (given_height * given_height)
    if result < 15 :
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wygłodzenie')
        second_try()
    if result > 15.1 and result <= 17.4:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wychudzenie')
        second_try()
    if result > 17.5 and result <=18.5:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - niedowaga')
        second_try()
    if result > 18.5 and result <= 24.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wartość prawidłowa')
        second_try()
    if result > 25 and result <= 29.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - nadwaga')
        second_try()
    if result > 30.0 and result <= 34.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - I stopień otyłości')
        second_try()
    if result > 35.0 and result <= 39.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - II stopień otyłości')
        second_try()
    if result > 40.0:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - III stopień otyłości')
        second_try()
def second_try():
    choice = easygui.buttonbox('Co chcesz zrobić ?', 'Your BMI status', ['Sprawdz BMI','BMI w Polsce','Zamknij program'])
    if choice == 'Sprawdz BMI':
        weight = int(easygui.enterbox('Podaj wagę: '))
        height = cm_to_m(float(easygui.enterbox('Podaj wzrost w centymentrach: ')))
        check_bmi(weight, height)
    if choice == 'BMI w Polsce':
        print(show_image())
        second_try()
    if choice == 'Zamknij program':
        easygui.msgbox('3maj forme, life if life ','Exit window')
        time.sleep(3)
w=easygui.buttonbox('Chcesz sprawdzić swoje BMI', 'Your BMI status',['Tak','Zamknij program '])
if w=='Tak':
    weight = int(easygui.enterbox('Podaj wagę: '))
    height = cm_to_m(float(easygui.enterbox('Podaj wzrost w centymentrach: ')))
    check_bmi(weight, height)
