import pygame
import threading
import win32gui
import sys
import screen
import workspace


class Bar:
    def __init__(self, widgets_list, height, workspaces=[], top_bar=True, fps=1):
        self.widgets_list = widgets_list
        self.height = height
        self.top_bar = top_bar
        self.fps = fps
        self.screen = None
        self.workspaces = None

    def set_screen(self, screen):
        self.screen = screen

    def set_workspaces(self, workspaces):
        self.workspaces = workspaces

    def start_process(self):
        self.process = threading.Thread(target=self.process_function)
        self.process.start()

    def process_function(self):
        pygame.init()
        self.size = (self.screen.resolution[0], self.height)
        self.display = pygame.display.set_mode(self.size, pygame.NOFRAME)
        pygame.display.set_caption("Bar")

        hwnd = pygame.display.get_wm_info()['window']
        # win32gui.SetWindowPos(hwnd, -1, 0, 0, self.size[0], self.size[1])
        win32gui.MoveWindow(hwnd, 0, 0, self.size[0], self.size[1], 1)

        # w = workspace.get_current(self.workspaces).stack[0]
        # w.focus()

        self.clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.display.fill((255, 0, 0))
            pygame.display.flip()
            self.clock.tick(self.fps)
