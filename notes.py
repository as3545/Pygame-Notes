#
Pygame is designed for writing Video Games. It is a free and open-source library.
And one of the most popular Python libraries for creating games and applications.
It adds functionality on top of excellent.
Does not require a GUI to use all functions. 
Write the following code in your terminal:

python3 -m pip install -U pygame --user
#We are using “- -user” flag to tell pip to install pygame in the home directory rather than installing it globally.

#To see if it works, run the following command:

python3 -m pygame.examples.aliens

#Changing the title of the window using pygame:
pygame.display.set_caption("Copy Assignment")
#Add it before the loop

#Customize the Pygame Window: Background Color
fill(color, rect=None, special_flags=0) -> Rect

# Inside the while loop after the for-loop, write the following
screen.fill((167,145,55))

pygame.display.update()

#Customize the Pygame Window: Icon of window
Customize the Pygame Window: Icon of window


pygame.display.set_icon(icon)

#whole code

  import pygame

pygame.init()



screen = pygame.display.set_mode((800,600))

# Title

pygame.display.set_caption("Copy Assignment")

icon = pygame.image.load("task.png")

pygame.display.set_icon(icon)

isRunning = True



while(isRunning ==True):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            isRunning = False

    screen.fill((167,145,55))

    pygame.display.update()
