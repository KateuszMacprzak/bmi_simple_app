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
    if result > 15.1 and result <= 17.4:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wychudzenie')
    if result > 17.5 and result <=18.5:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - niedowaga')
    if result > 18.5 and result <= 24.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wartość prawidłowa')
    if result > 25 and result <= 29.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - nadwaga')
    if result > 30.0 and result <= 34.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - I stopień otyłości')
    if result > 35.0 and result <= 39.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - II stopień otyłości')
    if result > 40.0:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - III stopień otyłości')

w=easygui.buttonbox('Chcesz sprawdzić swoje BMI', 'Your BMI status',['Tak','Zamknij program '])
if w=='Tak':
    weight = int(easygui.enterbox('Podaj wagę: '))
    height = cm_to_m(float(easygui.enterbox('Podaj wzrost w centymentrach: ')))
    result = weight/(height*height)
    if result < 15 :
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wygłodzenie')
        print(show_image())
    if result > 15.1 and result <= 17.4:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wychudzenie')
        print(show_image())
    if result > 17.5 and result <=18.5:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - niedowaga')
        print(show_image())
    if result > 18.5 and result <= 24.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - wartość prawidłowa')
        print(show_image())
    if result > 25 and result <= 29.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - nadwaga')
        print(show_image())
    if result > 30.0 and result <= 34.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - I stopień otyłości')
        print(show_image())
    if result > 35.0 and result <= 39.9:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - II stopień otyłości')
        print(show_image())
    if result > 40.0:
        easygui.msgbox(f'Twoje BMI wynosi {round(result,2)} - III stopień otyłości')
        print(show_image())


