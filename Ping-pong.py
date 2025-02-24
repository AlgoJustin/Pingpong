from pygame import * # Import all modules from the pygame library

'''Required classes''' # Section marker for necessary classes

# Parent class for all sprites in the game
class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, width, height):
    super().__init__() # Call the constructor of the parent class (Sprite)

    # Load the sprite image and resize it according to the given parameters
    self.image = transform.scale(image.load(player_image), (width, height)) # Width and height determine sprite size

    self.speed = player_speed # Movement speed of the sprite

    # Get the rect object to determine the sprite's position and boundaries
    self.rect = self.image.get_rect()
    self.rect.x = player_x # Initial horizontal position of the sprite
    self.rect.y = player_y # Initial vertical position of the sprite

    def reset(self):
      # Display the sprite on the screen at its current position
      window.blit(self.image, (self.rect.x, self.rect.y))

# Subclass for a controllable player
class Player(GameSprite):
  def update_r(self): # Method to move the right player
    keys = key.get_pressed() # Get the status of all pressed keys

    # Move the player up if the UP key is pressed and does not exceed the upper boundary
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed

    # Move the player down if the DOWN key is pressed and does not exceed the lower boundary
    if keys[K_DOWN] and self.rect.y < win_height - 80:
      self.rect.y += self.speed

  def update_l(self): #Method to move the left player
    keys = key.get_pressed() # Get the status of all pressed keys

    # Move the player up if the W key is pressed and does not exceed the upper boundary
    if keys[K_w] and self.rect.y > 5:
      self.rect.y -= self.speed

    # Move the player down if the S key is pressed and does not exceed the lower boundary
    if keys[K_s] and self.rect.y < win_height - 80:
      self.rect.y += self.speed

# Set the background color and window dimensions
back = (200, 255, 255) # Light blue background color
win_width = 600 # Width of the game window
win_height = 500 # Height of the game window
window = display.set_mode((win_width, win_height)) # Create the game window with specified dimensions
window.fill(back) # Fill the background with the chosen color

# Flags to control game state
game = True # Main game loop control
finish = False # Indicates whether the game has ended or not
clock = time.Clock() # Create a clock object to control frame rate
FPS = 60 # Frames per second setting

# Creating ball and paddles with specified positions and sizes
racket1 = Player('racket.png', 30, 200, 4, 50, 150) # Left paddle (player 1)
racket2 = Player('racket.png', 520, 200, 4, 50, 150) # Right paddle (player 2)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50) # Ball object

# Initializing font for displaying game over messages
font.init()
font = font.Font(None, 35) # Set font size to 35
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0)) # Message when Player 1 loses
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0)) # Message when Player 2 loses

# Ball movement speed variables
speed_x = 3 # Horizontal speed of the ball
speed_y = 3 # Vertical speed of the ball

# Main game loop
while game:
  for e in event.get(): # Loop to handle user inputs
    if e.type == QUIT: # If the quit event is triggered, end the game
      game = False
      
  if finish != True: # If the game is not finished, update game objects
    window.fill(back) # Redraw the background to clear previous frames
    racket1.update_1() # Update left paddle movement
    racket2.update_2() # Update right paddle movement

    # Move the ball according to its speed
    ball.rect.x += speed_x # Update ball's horizontal position
    ball.rect.y += speed_y # Update ball's vertical position

    # Check collision between the ball and paddles
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
      speed_x *= -1 # Reverse horizontal direction upon collision
      speed_y *= 1 # Maintain the same vertical direction

    # If the ball hits the top or bottom edges of the screen, reverse vertical direction
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
      speed_y *= -1

    # If the ball moves past the left edge, Player 1 loses
    if ball.rect.x < 0:
      finish = True # End the game
      window.blit(lose1, (200, 200)) # Display Player 1 loss message
      game_over = True # Set game over flag

    #If the ball moves past teh right edge, Player 2 loses
    if ball.rect.x > win_width:
      finish = True # End the game
      window.blit(lose2, (200, 200)) # Display Player 2 loss message
      game_over = True # Set game over flag

    # Redraw paddles and ball at their updated positions
    racket1.reset()
    racket2.reset()
    ball.reset()

display.update() # Refresh the display to show updated positions
clock.tick(FPS) # Control the frame rate of the game
