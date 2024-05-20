import pygame

class GlobalDefinitions:
    BOARD_SIZE = 4
    BOARD_HEIGHT = 14
    LEVEL_TICK_TIME = (0.7, 0.5, 0.2)
    LEVEL_SCORE_FACT = (1, 2, 3)
    CAM_DIST = 50
    CAM_HEIGHT = 18
    CAM_PITCH = 0.5
    HS_FILE = "main/game/data/hs.csv"
    MOVE_MAP = ((-1, 0), (0, -1), (1, 0), (0, 1))
    PITCH_ROLL_MAP = ((1, -1), (0, -1), (1, 1), (0, 1))
    
    def __init__(self):
        self.screen = [[[-1]*16 for _ in range(6)] for _ in range(6)]
        self.UIscreen = [[[-1]*5 for _ in range(5)] for _ in range(5)]
        self.rectList = []
        self.UIrectList = []
        self.persp = True
        self.size = 100
        self.pad_width = 1920
        self.pad_height = 1080
        self.score = 0
        self.dT = 10.0
        self.tileData = []
        self.rectList = []
        self.gamepad = pygame.display.set_mode((self.pad_width, self.pad_height))
        self.size = self.pad_width/2
    def setTileData(self,loc, i):
        x, y, z = loc
        self.tileData[i][x][y][z] = i

    def makeT(self, n, i):
        return [[[i]*n for _ in range(n)] for _ in range(n)]
    

    def initialize_tiles(self):
        self.tileData.append(self.makeT(5, -1))
        self.setTileData((2, 2, 0), len(self.tileData)-1)
        self.setTileData((2, 2, 1), len(self.tileData)-1)
        self.setTileData((2, 2, 2), len(self.tileData)-1)
        self.setTileData((2, 2, 3), len(self.tileData)-1)