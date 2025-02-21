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
