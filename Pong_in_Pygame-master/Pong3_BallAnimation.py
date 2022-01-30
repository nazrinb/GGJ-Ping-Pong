import pygame, sys
from variables import *

def ball_animation():
	global ball_speed_x, ball_speed_y
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= screen_width:
		ball_speed_x *= -1

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		# Game logic
		ball_animation()

		screen.fill(bg_color)
		pygame.draw.rect(screen, light_grey, player)
		pygame.draw.rect(screen, light_grey, opponent)
		pygame.draw.ellipse(screen, light_grey, ball)
		pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

		pygame.display.flip()
		clock.tick(60)

if __name__ == "__main__":
	main()