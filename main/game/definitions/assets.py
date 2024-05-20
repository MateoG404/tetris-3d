import numpy as np
from game.classes.engine import Color

class Assets:
    def __init__(self):
        
        self.SHAPE1 = np.array((((0, 0),
                            (1, 1)),

                        ((0, 0),
                            (1, 1))))

        self.SHAPE2 = np.array((((0, 0),
                            (0, 0)),

                        ((1, 1),
                            (1, 1))))

        self.SHAPE3 = np.array((((0, 0, 0),
                            (0, 0, 0),
                            (0, 1, 0)),

                        ((0, 1, 0),
                            (0, 1, 0),
                            (0, 1, 0)),

                        ((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0))))

        self.SHAPE4 = np.array((((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0)),

                        ((0, 1, 1),
                            (0, 1, 0),
                            (0, 1, 0)),

                        ((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0))))

        self.SHAPE5 = np.array((((0, 1),
                            (0, 0)),

                        ((1, 1),
                            (0, 1))))

        self.SHAPE6 = np.array((((1, 0),
                            (1, 1)),

                        ((0, 0),
                            (1, 0))))

        self.SHAPE7 = np.array((((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0)),

                        ((0, 0, 0),
                            (1, 1, 0),
                            (0, 1, 1)),

                        ((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0))))

        self.SHAPE8 = np.array((((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0)),

                        ((0, 1, 0),
                            (0, 1, 0),
                            (0, 0, 0)),

                        ((0, 1, 0),
                            (0, 1, 0),
                            (0, 0, 0))))

        self.SHAPE9 = np.array((((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0)),

                        ((0, 0, 0),
                            (1, 1, 0),
                            (0, 1, 1)),

                        ((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0))))

        self.SHAPE10 = np.array((((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0)),

                            ((0, 1, 0),
                            (0, 1, 0),
                            (0, 1, 0)),

                            ((0, 0, 0),
                            (0, 1, 0),
                            (0, 0, 0))))


        self.SHAPES = (self.SHAPE1, self.SHAPE2, self.SHAPE3,
                        self.SHAPE4, self.SHAPE5, self.SHAPE6, self.SHAPE7,
                        self.SHAPE8, self.SHAPE9, self.SHAPE10)
        self.COLORS = (Color(255, 102, 102), Color(255, 178, 102), Color(255, 255, 102),
                Color(178, 255, 102), Color(102, 255, 102), Color(102, 255, 178),
                Color(102, 255, 255), Color(102, 178, 255), Color(102, 102, 255),
                Color(178, 102, 255), Color(255, 102, 255), Color(255, 102, 178),
                Color(192, 192, 192))
