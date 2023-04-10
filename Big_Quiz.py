# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:23:29 2023

@author: Andrew
"""

import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import sys
import pgzero
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_h


WIDTH = 1280
HEIGHT = 720
main_box = pygame.Rect(50, 40, 820, 240)
timer_box = pygame.Rect(990, 40, 240, 240)

answer_box1 = pygame.Rect(50, 358, 495, 165)
answer_box2 = pygame.Rect(735, 358, 495, 165)
answer_box3 = pygame.Rect(50, 538, 495, 165)
answer_box4 = pygame.Rect(735, 538, 495, 165)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["What is the capital of France?",
      "London", "Paris", "Berlin", "Tokyo", 2]
q2 = ["what is 5+7",
      "12", "10", "14", "8", 1]
q3 = ["What is the seventh month of the year?",
      "April", "May", "June", "July", 4]
q4 = ["Which planet is closest to the Sun?",
      "Saturn", "Neptune", "Mercury", "Venus", 3]
q5 = ["Where are the pyramids?",
      "India", "Mexico", "China", "Egypt", 4]
q6 = ["What is the capital of California?", 
      "Oakland", "San Francisco", "San Jose", "Sacramento", 4]
q7 = ["Who is the President of the United States?", 
      "John Cena", "Andrew Lin", "Joe Biden", "Donald Trump", 3]
q8 = ["Who has the most Olympic Medals?", 
      "Michael Phelps", "Yao Ming", "Lebron James", "Michael Jordan", 1]
q9 = ["Who is going to win the 2023 NBA Finals?", 
      "Golden State Warriors", "Denver Nuggets", "Philadelphia 76ers", "Boston Celtics", 1]
q10 = ["Where is the Great Wall located?", 
      "Spain", "Italy", "Russia", "China", 4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
question = questions.pop(0)


def draw(screen):
    screen.fill(" midnight blue")
    pygame.draw.rect(screen, "dark cyan", main_box)
    pygame.draw.rect(screen, "dark magenta", timer_box)

    for box in answer_boxes:
        pygame.draw.rect(screen, "saddle brown", box)

    font = pygame.font.Font(None, 46)
    question_text = font.render(question[0], True, (0, 0, 0))
    screen.blit(question_text, (main_box.x + 10, main_box.y + 10))

    text = font.render(str(time_left), True, (0, 0, 0))
    screen.blit(text, (timer_box.x + 10, timer_box.y + 10))

    index = 1
    for box in answer_boxes:
        text = font.render(question[index], True, (0, 0, 0))
        screen.blit(text, (box.x + 10, box.y + 10))
        index += 1


def game_over():
    global question, time_left
    message = ("Game over. You got %s questions correct" % str(score))
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()


def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer" + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index += 1


def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

def on_key_up(key): 
    if key == keys.H:
        print("The correct answer is box number %s" % question[5])


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # 1000 milliseconds = 1 second

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            on_mouse_down(event.pos)
        elif event.type == pygame.USEREVENT + 1:
            update_time_left()
        elif event.type == KEYDOWN:
            if event.key == K_h:
                print("Hint: The correct answer is at position", question[5])


    draw(screen)
    pygame.display.update()
    clock.tick(60)
