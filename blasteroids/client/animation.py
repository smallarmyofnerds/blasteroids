import pygame


class Animation:
    def __init__(self, frames, milliseconds_per_frame):
        self.frames = frames
        self.milliseconds_per_frame = milliseconds_per_frame
        self.active_frame = 0
        self.last_frame_advance = pygame.time.get_ticks()
    
    def _next_frame(self):
        self.active_frame = (self.active_frame + 1) % len(self.frames)
        self.last_frame_advance = pygame.time.get_ticks()

    def draw(self, screen, position, orientation):
        if pygame.time.get_ticks() - self.last_frame_advance > self.milliseconds_per_frame:
            self._next_frame()
        screen.draw_sprite(self.frames[self.active_frame], position, orientation)
