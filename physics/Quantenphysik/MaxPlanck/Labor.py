import pygame
import math
import sys

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Physics Constants
GRAVITY_ACCELERATION = 0.2  # Acceleration in pixels/frame^2 (adjust for desired speed)
ANGLE_DEGREES = 45
ANGLE_RADIANS = math.radians(ANGLE_DEGREES)

# Ball Properties
BALL_RADIUS = 15

# Plane Properties (Adjust start/end points as needed)
PLANE_START_MARGIN = 100 # Margin from screen edges
PLANE_START_X = PLANE_START_MARGIN
PLANE_START_Y = PLANE_START_MARGIN
# Calculate end point based on angle and screen size to keep it roughly 45 deg
plane_length_x = SCREEN_WIDTH - 2 * PLANE_START_MARGIN
PLANE_END_X = PLANE_START_X + plane_length_x
PLANE_END_Y = PLANE_START_Y + plane_length_x * math.tan(ANGLE_RADIANS) # y = x * tan(angle) for 45 deg

# Ensure plane doesn't go off screen vertically
if PLANE_END_Y > SCREEN_HEIGHT - PLANE_START_MARGIN:
    PLANE_END_Y = SCREEN_HEIGHT - PLANE_START_MARGIN
    # Recalculate end X based on clamped Y (maintains the visual segment)
    PLANE_END_X = PLANE_START_X + (PLANE_END_Y - PLANE_START_Y) / math.tan(ANGLE_RADIANS)


# --- Pygame Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball on Inclined Plane")
clock = pygame.time.Clock()

# --- Simulation Variables ---
# Calculate acceleration component parallel to the plane
acceleration_along_plane = GRAVITY_ACCELERATION * math.sin(ANGLE_RADIANS)

# Ball's state: distance traveled along the plane and velocity along the plane
distance_traveled = 0.0
velocity_along_plane = 0.0

# --- Game Loop ---
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_r: # Press 'R' to reset
                distance_traveled = 0.0
                velocity_along_plane = 0.0


    # --- Physics Update ---
    # Update velocity based on acceleration
    velocity_along_plane += acceleration_along_plane

    # Update distance traveled along the plane based on velocity
    distance_traveled += velocity_along_plane

    # Calculate the ball's current (x, y) coordinates based on distance traveled
    # Start at PLANE_START_X, PLANE_START_Y and move along the plane's vector
    current_ball_x = PLANE_START_X + distance_traveled * math.cos(ANGLE_RADIANS)
    current_ball_y = PLANE_START_Y + distance_traveled * math.sin(ANGLE_RADIANS)

    # --- Collision Detection (Stop at the end of the drawn plane segment) ---
    # Check if the ball's center has passed the end point of the plane segment
    if current_ball_x >= PLANE_END_X or current_ball_y >= PLANE_END_Y:
         # Option 1: Stop the ball
         velocity_along_plane = 0
         # Clamp position to the end point to prevent overshoot
         current_ball_x = PLANE_END_X
         current_ball_y = PLANE_END_Y
         # Adjust distance_traveled to match the clamped position (optional, but cleaner)
         distance_traveled = (PLANE_END_X - PLANE_START_X) / math.cos(ANGLE_RADIANS)

         # Option 2: Reset (uncomment below and comment out Option 1)
         # distance_traveled = 0.0
         # velocity_along_plane = 0.0


    # --- Drawing ---
    # Fill the background
    screen.fill(WHITE)

    # Draw the inclined plane (as a line)
    pygame.draw.line(screen, BLACK, (PLANE_START_X, PLANE_START_Y), (PLANE_END_X, PLANE_END_Y), 5)

    # Draw the ball
    # Use integer coordinates for drawing
    draw_x = int(current_ball_x)
    draw_y = int(current_ball_y)
    pygame.draw.circle(screen, RED, (draw_x, draw_y), BALL_RADIUS)

    # --- Update Display ---
    pygame.display.flip()

    # --- Frame Rate Control ---
    clock.tick(FPS)

# --- Cleanup ---
pygame.quit()
sys.exit()