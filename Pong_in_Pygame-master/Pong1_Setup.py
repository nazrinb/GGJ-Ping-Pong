import pygame, sys
from variables import *
from Pong2_Drawing import *
from Pong3_BallAnimation import *
# from Pong4_Input import *
# from Pong5_Opponent import *
# from Pong6_Restart import *
# from Pong7_Score import *
# from Pong8_Timer import *
# from Pong9_collision import *

while True:
	#Handling input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	
	# Updating the window 
	pygame.display.flip()
	clock.tick(60)
