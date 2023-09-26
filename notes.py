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
      
#text = "copyassignment"
textX = 10
textY = 10

Font(filename, size) -> Font
Font(object, size) -> Font

pygame.font.Font.bold	Gets or sets whether the font should be rendered in (faked) bold.
bold -> bool
pygame.font.Font.italic	Gets or sets whether the font should be rendered in (faked) italics.
italic -> bool
pygame.font.Font.underline	Gets or sets whether the font should be rendered with an underline.
underline -> bool
pygame.font.Font.render	draw text on a new Surface
render(text, antialias, color, background=None) -> Surface
pygame.font.Font.size	determine the amount of space needed to render text
size(text) -> (width, height)
pygame.font.Font.set_underline	control if text is rendered with an underline
set_underline(bool) -> None
pygame.font.Font.get_underline	check if text will be rendered with an underline
get_underline() -> bool
pygame.font.Font.set_bold	enable fake rendering of bold text
set_bold(bool) -> None
pygame.font.Font.get_bold	check if text will be rendered bold
get_bold() -> bool
pygame.font.Font.set_italic	enable fake rendering of italic text
set_italic(bool) -> None
pygame.font.Font.metrics	gets the metrics for each character in the passed string
metrics(text) -> list
pygame.font.Font.get_italic	check if the text will be rendered italic
get_italic() -> bool
pygame.font.Font.get_linesize	get the line space of the font text
get_linesize() -> int
pygame.font.Font.get_height	get the height of the font
get_height() -> int
pygame.font.Font.get_ascent	get the ascent of the font
get_ascent() -> int
pygame.font.Font.get_descent	get the descent of the font
get_descent() -> int



  import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
# Title
pygame.display.set_caption("copyassignment")
isRunning = True

#Loading image
player = pygame.image.load('athlete.png')


# Creating Text
# We are using an inbuilt font (freesansbold.ttf) provided to us by Pygame
text = "copyassignment"
font = pygame.font.Font('freesansbold.ttf',24)
textX = 10
textY = 10
textImage = font.render(text, True, (255,255,255))

#Specifying the X and Y Coordinate

playerX = 375
playerY = 500
Xchange = 0
Ychange = 0
while(isRunning ==True):
    screen.fill((167,145,55))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Ychange-=0.5
            if(event.key == pygame.K_DOWN):
                Ychange+=0.5
            if event.key == pygame.K_LEFT:
                Xchange-=0.5
            if event.key == pygame.K_RIGHT:
                Xchange+=0.5
        if event.type == pygame.KEYUP:
            Ychange=0
            Xchange=0
    if playerX+Xchange>775 or playerY+Ychange>565 or playerX+Xchange<0 or playerY+Ychange<0:
        playerY+=0
        playerX+=0
    else:
        playerY+=Ychange
        playerX+=Xchange
    screen.blit(textImage,(textX, textY))
    screen.blit(player,(playerX, playerY))
    pygame.display.update()

#Adding sound effect:
# Loading our sound
hitSound = mixer.Sound('sound.wav')

# Playing our sound
hitSound.play()
# Notice that we have not written -1 inside the parenthesis

        
