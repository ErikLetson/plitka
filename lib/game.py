#!usr/bin/env-python

import pygame, os, random

#PLITKA GOALS

#meta
#feel smoother than my previous games
#feel very frantic at a high level

#specific
#release on itch.io as well as game jolt
#make a youtube video

SCREEN_WIDTH = 1088
SCREEN_HEIGHT = 704
FRAMERATE = 60

WINDOW_POSITION_X = 120
WINDOW_POSITION_Y = 30

TILE_WIDTH = 32
TILE_HEIGHT = 32
TILE_COLS = SCREEN_WIDTH / 32
TILE_ROWS = SCREEN_HEIGHT / 32

#environment calls
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_POSITION_X,
                                                WINDOW_POSITION_Y)

#Resources
SHEETS = {
    'default_bg.png':[(32, 32), 748],
    'Blue_Plitka.png':[(32, 32), 150],
    'Red_Plitka.png':[(32, 32), 150],
    'Green_Plitka.png':[(32, 32), 150],
    'Cyan_Plitka.png':[(32, 32), 150],
    'Yellow_Plitka.png':[(32, 32), 150],
    'TileGrid.png':[(32, 32), 1],
    'side_arrow.png':[(32, 32), 4],
    'top_arrow.png':[(32, 32), 4],
    'selection_overlay.png':[(32, 32), 1],
    'wasd_instruction.png':[(260, 180), 1],
    'arrow_controls.png':[(260, 180), 1],
    'plitka_diagram.png':[(200, 160), 1],
    'sound_marker.png':[(160, 84), 1],
    'x.png':[(18, 18), 1],
    'instructions.png':[(320, 64), 1],
    'shift.png':[(160, 84), 1],
    'retry.png':[(400, 64), 2],
    'enter.png':[(400, 64), 1]
    }
ANIMATIONS = {
    'Blue_Plitka.png':{
        'shimmer':([(1, 0), (2, 0), (3, 0), (4, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
                    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
                    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6),
                    (0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
                    (0, 8), (1, 8), (2, 8), (3, 8), (4, 8),
                    (0, 9), (1, 9), (2, 9), (3, 9), (4, 9),
                    (0, 10), (1, 10), (2, 10), (3, 10), (4, 10),
                    (0, 11), (1, 11), (2, 11), (3, 11), (4, 11),
                    (0, 12), (1, 12), (2, 12), (3, 12), (4, 12),
                    (0, 13), (1, 13), (2, 13), (3, 13), (4, 13),
                    (0, 14), (1, 14), (2, 14), (3, 14), (4, 14),
                    (0, 15), (1, 15), (2, 15), (3, 15), (4, 15),
                    (0, 16), (1, 16), (2, 16), (3, 16), (4, 16),
                    (0, 17), (1, 17), (2, 17), (3, 17), (4, 17),
                    (0, 18), (1, 18), (2, 18), (3, 18), (4, 18),
                    (0, 19), (1, 19), (2, 19), (3, 19), (4, 19),
                    (0, 20), (1, 20), (2, 20), (3, 20), (4, 20),
                    (0, 21), (1, 21), (2, 21), (3, 21), (4, 21),
                    (0, 22), (1, 22), (2, 22), (3, 22), (4, 22),
                    (0, 23), (1, 23), (2, 23), (3, 23), (4, 23),
                    (0, 24), (1, 24), (2, 24), (3, 24), (4, 24),
                    (0, 25), (1, 25), (2, 25), (3, 25), (4, 25),
                    (0, 26), (1, 26), (2, 26), (3, 26), (4, 26),
                    (0, 27), (1, 27), (2, 27), (3, 27), (4, 27),
                    (0, 28), (1, 28), (2, 28), (3, 28), (4, 28),
                    (0, 29), (1, 29), (2, 29), (3, 29), (4, 29)], 1)
        },
    'Red_Plitka.png':{
        'shimmer':([(1, 0), (2, 0), (3, 0), (4, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
                    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
                    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6),
                    (0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
                    (0, 8), (1, 8), (2, 8), (3, 8), (4, 8),
                    (0, 9), (1, 9), (2, 9), (3, 9), (4, 9),
                    (0, 10), (1, 10), (2, 10), (3, 10), (4, 10),
                    (0, 11), (1, 11), (2, 11), (3, 11), (4, 11),
                    (0, 12), (1, 12), (2, 12), (3, 12), (4, 12),
                    (0, 13), (1, 13), (2, 13), (3, 13), (4, 13),
                    (0, 14), (1, 14), (2, 14), (3, 14), (4, 14),
                    (0, 15), (1, 15), (2, 15), (3, 15), (4, 15),
                    (0, 16), (1, 16), (2, 16), (3, 16), (4, 16),
                    (0, 17), (1, 17), (2, 17), (3, 17), (4, 17),
                    (0, 18), (1, 18), (2, 18), (3, 18), (4, 18),
                    (0, 19), (1, 19), (2, 19), (3, 19), (4, 19),
                    (0, 20), (1, 20), (2, 20), (3, 20), (4, 20),
                    (0, 21), (1, 21), (2, 21), (3, 21), (4, 21),
                    (0, 22), (1, 22), (2, 22), (3, 22), (4, 22),
                    (0, 23), (1, 23), (2, 23), (3, 23), (4, 23),
                    (0, 24), (1, 24), (2, 24), (3, 24), (4, 24),
                    (0, 25), (1, 25), (2, 25), (3, 25), (4, 25),
                    (0, 26), (1, 26), (2, 26), (3, 26), (4, 26),
                    (0, 27), (1, 27), (2, 27), (3, 27), (4, 27),
                    (0, 28), (1, 28), (2, 28), (3, 28), (4, 28),
                    (0, 29), (1, 29), (2, 29), (3, 29), (4, 29)], 1)
        },
    'Green_Plitka.png':{
        'shimmer':([(1, 0), (2, 0), (3, 0), (4, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
                    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
                    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6),
                    (0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
                    (0, 8), (1, 8), (2, 8), (3, 8), (4, 8),
                    (0, 9), (1, 9), (2, 9), (3, 9), (4, 9),
                    (0, 10), (1, 10), (2, 10), (3, 10), (4, 10),
                    (0, 11), (1, 11), (2, 11), (3, 11), (4, 11),
                    (0, 12), (1, 12), (2, 12), (3, 12), (4, 12),
                    (0, 13), (1, 13), (2, 13), (3, 13), (4, 13),
                    (0, 14), (1, 14), (2, 14), (3, 14), (4, 14),
                    (0, 15), (1, 15), (2, 15), (3, 15), (4, 15),
                    (0, 16), (1, 16), (2, 16), (3, 16), (4, 16),
                    (0, 17), (1, 17), (2, 17), (3, 17), (4, 17),
                    (0, 18), (1, 18), (2, 18), (3, 18), (4, 18),
                    (0, 19), (1, 19), (2, 19), (3, 19), (4, 19),
                    (0, 20), (1, 20), (2, 20), (3, 20), (4, 20),
                    (0, 21), (1, 21), (2, 21), (3, 21), (4, 21),
                    (0, 22), (1, 22), (2, 22), (3, 22), (4, 22),
                    (0, 23), (1, 23), (2, 23), (3, 23), (4, 23),
                    (0, 24), (1, 24), (2, 24), (3, 24), (4, 24),
                    (0, 25), (1, 25), (2, 25), (3, 25), (4, 25),
                    (0, 26), (1, 26), (2, 26), (3, 26), (4, 26),
                    (0, 27), (1, 27), (2, 27), (3, 27), (4, 27),
                    (0, 28), (1, 28), (2, 28), (3, 28), (4, 28),
                    (0, 29), (1, 29), (2, 29), (3, 29), (4, 29)], 1)
        },
    'Cyan_Plitka.png':{
        'shimmer':([(1, 0), (2, 0), (3, 0), (4, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
                    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
                    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6),
                    (0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
                    (0, 8), (1, 8), (2, 8), (3, 8), (4, 8),
                    (0, 9), (1, 9), (2, 9), (3, 9), (4, 9),
                    (0, 10), (1, 10), (2, 10), (3, 10), (4, 10),
                    (0, 11), (1, 11), (2, 11), (3, 11), (4, 11),
                    (0, 12), (1, 12), (2, 12), (3, 12), (4, 12),
                    (0, 13), (1, 13), (2, 13), (3, 13), (4, 13),
                    (0, 14), (1, 14), (2, 14), (3, 14), (4, 14),
                    (0, 15), (1, 15), (2, 15), (3, 15), (4, 15),
                    (0, 16), (1, 16), (2, 16), (3, 16), (4, 16),
                    (0, 17), (1, 17), (2, 17), (3, 17), (4, 17),
                    (0, 18), (1, 18), (2, 18), (3, 18), (4, 18),
                    (0, 19), (1, 19), (2, 19), (3, 19), (4, 19),
                    (0, 20), (1, 20), (2, 20), (3, 20), (4, 20),
                    (0, 21), (1, 21), (2, 21), (3, 21), (4, 21),
                    (0, 22), (1, 22), (2, 22), (3, 22), (4, 22),
                    (0, 23), (1, 23), (2, 23), (3, 23), (4, 23),
                    (0, 24), (1, 24), (2, 24), (3, 24), (4, 24),
                    (0, 25), (1, 25), (2, 25), (3, 25), (4, 25),
                    (0, 26), (1, 26), (2, 26), (3, 26), (4, 26),
                    (0, 27), (1, 27), (2, 27), (3, 27), (4, 27),
                    (0, 28), (1, 28), (2, 28), (3, 28), (4, 28),
                    (0, 29), (1, 29), (2, 29), (3, 29), (4, 29)], 1)
        },
    'Yellow_Plitka.png':{
        'shimmer':([(1, 0), (2, 0), (3, 0), (4, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
                    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
                    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
                    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6),
                    (0, 7), (1, 7), (2, 7), (3, 7), (4, 7),
                    (0, 8), (1, 8), (2, 8), (3, 8), (4, 8),
                    (0, 9), (1, 9), (2, 9), (3, 9), (4, 9),
                    (0, 10), (1, 10), (2, 10), (3, 10), (4, 10),
                    (0, 11), (1, 11), (2, 11), (3, 11), (4, 11),
                    (0, 12), (1, 12), (2, 12), (3, 12), (4, 12),
                    (0, 13), (1, 13), (2, 13), (3, 13), (4, 13),
                    (0, 14), (1, 14), (2, 14), (3, 14), (4, 14),
                    (0, 15), (1, 15), (2, 15), (3, 15), (4, 15),
                    (0, 16), (1, 16), (2, 16), (3, 16), (4, 16),
                    (0, 17), (1, 17), (2, 17), (3, 17), (4, 17),
                    (0, 18), (1, 18), (2, 18), (3, 18), (4, 18),
                    (0, 19), (1, 19), (2, 19), (3, 19), (4, 19),
                    (0, 20), (1, 20), (2, 20), (3, 20), (4, 20),
                    (0, 21), (1, 21), (2, 21), (3, 21), (4, 21),
                    (0, 22), (1, 22), (2, 22), (3, 22), (4, 22),
                    (0, 23), (1, 23), (2, 23), (3, 23), (4, 23),
                    (0, 24), (1, 24), (2, 24), (3, 24), (4, 24),
                    (0, 25), (1, 25), (2, 25), (3, 25), (4, 25),
                    (0, 26), (1, 26), (2, 26), (3, 26), (4, 26),
                    (0, 27), (1, 27), (2, 27), (3, 27), (4, 27),
                    (0, 28), (1, 28), (2, 28), (3, 28), (4, 28),
                    (0, 29), (1, 29), (2, 29), (3, 29), (4, 29)], 1)
        },
    'side_arrow.png':{
        'bob':([(0, 0), (0, 1), (1, 0), (1, 1)], 10)
        },
    'top_arrow.png':{
        'bob':([(0, 0), (0, 1), (1, 0), (1, 1)], 10)
        },
    'retry.png':{
        'flash':([(0, 0), (1, 0)], 30)
        }
    }

################################################################################

class Game(object):
    """
    Object that controls the entire game structure.
    """

    def __init__(self):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.set_caption('Plitka')
        self.frame_clock = pygame.time.Clock()

        self.mode = 'START'

        self.on = True

        self.font = pygame.font.Font(os.path.join('data', 'font',
                                                  'kremlin.ttf'), 12)

        self.score_header = self.font.render('score', False, (255, 255, 255))
        self.best_header = self.font.render('best', False, (255, 255, 255))

        self.sheets = {}
        self.animations = {}

        #loading
        self.load_sheets(SHEETS)

        self.board = Board(self)

        self.plitka_timer = 100
        self.difficulty = 10
        self.clears = 0
        self.spawn = True
        self.score = 0
        self.highscore = 0
        self.timer = 0
        self.incrementor = 0
        self.max_plitkas = 2
        self.sound_on = True
        self.retry_delay = 60

        f = open(os.path.join('data', 'scr', 'highscore'), 'r')
        self.highscore = int(f.read())
        f.close()

        self.retry_prompt = Entity(self, self.sheets['retry.png'], (0, 0),
                                   ANIMATIONS['retry.png'], (-600, -600))
        self.enter_prompt = Entity(self, self.sheets['enter.png'], (0, 0),
                                   None, (-600, -600))
        self.highscore_meter = self.font.render(str(self.highscore), False,
                                                (255, 255, 255))
        self.score_meter = self.font.render(str(self.score), False,
                                           (255, 255, 255))

        #sounds
        self.clear_sound = pygame.mixer.Sound(os.path.join('data', 'snd',
                                                           'clear.wav'))
        self.music = pygame.mixer.Sound(os.path.join('data', 'snd',
                                                    'Interstelavator.wav'))
        self.scoot_sound = pygame.mixer.Sound(os.path.join('data', 'snd',
                                                           'scoot.wav'))
        self.die_sound = pygame.mixer.Sound(os.path.join('data', 'snd',
                                                         'end.wav'))

        #controllers
        for t in self.board.tiles:

            if self.board.tiles[t].coordinates == (22, 5):
                
                self.side_arrow = Arrow(self, self.sheets['side_arrow.png'],
                                        (0, 0), ANIMATIONS['side_arrow.png'],
                                        (704, 160), (22, 5),
                                        self.board.tiles[t])
                self.side_arrow.make_overlays(range(12, 22), [5])
                self.side_arrow.set_animation('bob')

            elif self.board.tiles[t].coordinates == (21, 4):

                self.top_arrow = Arrow(self, self.sheets['top_arrow.png'],
                                       (0, 0), ANIMATIONS['top_arrow.png'],
                                       (672, 128), (21, 4),
                                       self.board.tiles[t])
                self.top_arrow.make_overlays([21], range(5, 20))
                self.top_arrow.set_animation('bob')

        #self.top_arrow.visible = False#TEMP
        self.cursor_follow = False

        self.buttons = {#'button':[pressed, delay, flagged for active]
            pygame.K_w:[False, 0, False],
            pygame.K_a:[False, 0, False],
            pygame.K_s:[False, 0, False],
            pygame.K_d:[False, 0, False],
            pygame.K_UP:[False, 0, False],
            pygame.K_DOWN:[False, 0, False],
            pygame.K_LEFT:[False, 0, False],
            pygame.K_RIGHT:[False, 0, False],
            pygame.K_m:[False, 0, False],
            pygame.K_RETURN:[False, 0, False]
            }

        #instructions
        self.wasd = Entity(self, self.sheets['wasd_instruction.png'], (0, 0),
                           None, (28, 190))
        self.arrow_keys = Entity(self, self.sheets['arrow_controls.png'],
                                 (0, 0), None, (780, 190))
        #self.diagram = Entity(self, self.sheets['plitka_diagram.png'],
        #                     (0, 0), None, (68, 448))
        self.shift = Entity(self, self.sheets['shift.png'],
                            (0, 0), None, (88, 388))
        self.x_mark = Entity(self, self.sheets['x.png'], (0, 0), None,
                             (845, 453))
        self.ins = Entity(self, self.sheets['instructions.png'],
                          (0, 0), None, (400, 20))
        self.sound_marker = Entity(self, self.sheets['sound_marker.png'],
                                   (0, 0), None, (820, 400))

        self.instructions = [self.wasd, self.arrow_keys, self.shift,
                             self.sound_marker, self.x_mark, self.ins]
        self.redraw_instructions = True

        ############
        ##TITLE#####
        ############

        self.title_array = {}
        self.bg = Entity(self, self.sheets['default_bg.png'], (0, 0), None,
                         (0, 0))

        self.start_timer = 240
        
        for px in range(0, 60):

            self.title_array[px] = Entity(self, self.sheets['Red_Plitka.png'],
                                         (1, 0), ANIMATIONS['Red_Plitka.png'],
                                         (-600, -600))
            
        #P
        self.title_array[0].rect.topleft = (192, -6 * 32)
        self.title_array[1].rect.topleft = (192, -5 * 32)
        self.title_array[2].rect.topleft = (192, -4 * 32)
        self.title_array[3].rect.topleft = (192, -3 * 32)
        self.title_array[4].rect.topleft = (192, -2 * 32)
        self.title_array[5].rect.topleft = (192, -1 * 32)
        self.title_array[6].rect.topleft = (192 + 32, -6 * 32)
        self.title_array[7].rect.topleft = (192 + 32, -4 * 32)
        self.title_array[8].rect.topleft = (192 + 64, -6 * 32)
        self.title_array[9].rect.topleft = (192 + 64, -5 * 32)
        self.title_array[10].rect.topleft = (192 + 64, -4 * 32)

        #L
        self.title_array[11].rect.topleft = (320, -6 * 32)
        self.title_array[12].rect.topleft = (320, -5 * 32)
        self.title_array[13].rect.topleft = (320, -4 * 32)
        self.title_array[14].rect.topleft = (320, -3 * 32)
        self.title_array[15].rect.topleft = (320, -2 * 32)
        self.title_array[16].rect.topleft = (320, -1 * 32)
        self.title_array[17].rect.topleft = (320 + 32, -1 * 32)
        self.title_array[18].rect.topleft = (320 + 64, -1 * 32)

        #I
        self.title_array[19].rect.topleft = (448, -6 * 32)
        self.title_array[20].rect.topleft = (448, -5 * 32)
        self.title_array[21].rect.topleft = (448, -4 * 32)
        self.title_array[22].rect.topleft = (448, -3 * 32)
        self.title_array[23].rect.topleft = (448, -2 * 32)
        self.title_array[24].rect.topleft = (448, -1 * 32)

        #T
        self.title_array[25].rect.topleft = (512, -6 * 32)
        self.title_array[26].rect.topleft = (544, -6 * 32)
        self.title_array[27].rect.topleft = (576, -6 * 32)
        self.title_array[28].rect.topleft = (544, -5 * 32)
        self.title_array[29].rect.topleft = (544, -4 * 32)
        self.title_array[30].rect.topleft = (544, -3 * 32)
        self.title_array[31].rect.topleft = (544, -2 * 32)
        self.title_array[32].rect.topleft = (544, -1 * 32)

        #K
        self.title_array[33].rect.topleft = (640, -6 * 32)
        self.title_array[34].rect.topleft = (640, -5 * 32)
        self.title_array[35].rect.topleft = (640, -4 * 32)
        self.title_array[36].rect.topleft = (640, -3 * 32)
        self.title_array[37].rect.topleft = (640, -2 * 32)
        self.title_array[38].rect.topleft = (640, -1 * 32)
        self.title_array[39].rect.topleft = (672, -4 * 32)
        self.title_array[40].rect.topleft = (672, -3 * 32)
        self.title_array[41].rect.topleft = (704, -6 * 32)
        self.title_array[42].rect.topleft = (704, -5 * 32)
        self.title_array[43].rect.topleft = (704, -3 * 32)
        self.title_array[44].rect.topleft = (704, -2 * 32)
        self.title_array[45].rect.topleft = (704, -1 * 32)

        #A
        self.title_array[46].rect.topleft = (768, -6 * 32)
        self.title_array[47].rect.topleft = (768, -5 * 32)
        self.title_array[48].rect.topleft = (768, -4 * 32)
        self.title_array[49].rect.topleft = (768, -3 * 32)
        self.title_array[50].rect.topleft = (768, -2 * 32)
        self.title_array[51].rect.topleft = (768, -1 * 32)
        self.title_array[52].rect.topleft = (800, -6 * 32)
        self.title_array[53].rect.topleft = (800, -3 * 32)
        self.title_array[54].rect.topleft = (832, -6 * 32)
        self.title_array[55].rect.topleft = (832, -5 * 32)
        self.title_array[56].rect.topleft = (832, -4 * 32)
        self.title_array[57].rect.topleft = (832, -3 * 32)
        self.title_array[58].rect.topleft = (832, -2 * 32)
        self.title_array[59].rect.topleft = (832, -1 * 32)
                
    def load_sheets(self, sheets):
        """
        Load all sheets in the SHEET constant.
        """

        for sh in sheets:

            self.sheets[sh] = Sheet(self, sh, sheets[sh][0], sheets[sh][1])

    def shift_frames(self):
        """
        Change to the next frame. Must be called first in
        the game loop.
        """

        self.frame_clock.tick(FRAMERATE)

    def handle_events(self):
        """
        Handle all events sent to the game by the system or
        user.
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                f = open(os.path.join('data', 'scr', 'highscore'), 'w')

                f.write(str(self.highscore))

                f.close()

                self.on = False

            elif event.type == pygame.KEYDOWN:

                for k in self.buttons:

                    if k == event.key:

                        self.buttons[k][0] = True

                if event.key == pygame.K_LSHIFT:

                    self.cursor_follow = True

            elif event.type == pygame.KEYUP:

                for k in self.buttons:

                    if k == event.key:

                        self.buttons[k][0] = False
                        self.buttons[k][1] = 10
                        self.buttons[k][2] = False

                if event.key == pygame.K_LSHIFT:

                    self.cursor_follow = False

        #handle control events
        if self.mode == 'GAME':
            
            if self.buttons[pygame.K_UP][2] == True:

                self.buttons[pygame.K_UP][2] = False
                self.buttons[pygame.K_UP][1] = 10

                if self.side_arrow.coordinates[1] > 5:

                    self.side_arrow.shift(0, -1)

            elif self.buttons[pygame.K_DOWN][2] == True:

                self.buttons[pygame.K_DOWN][2] = False
                self.buttons[pygame.K_DOWN][1] = 10

                if self.side_arrow.coordinates[1] < 19:

                    self.side_arrow.shift(0, 1)

            elif self.buttons[pygame.K_a][2] == True:

                self.buttons[pygame.K_a][2] = False
                self.buttons[pygame.K_a][1] = 10

                shifts = []

                for t in self.board.rows[self.side_arrow.coordinates[1]]:

                    if t.contents != None and t.contents.settled == False:

                        shifts.append(t.contents)

                m = False

                for s in shifts:

                    s.shift(-1, 0)
                    m = True

                if m and self.sound_on:

                    self.scoot_sound.play()

            elif self.buttons[pygame.K_d][2] == True:

                self.buttons[pygame.K_d][2] = False
                self.buttons[pygame.K_d][1] = 10

                shifts = []

                for t in self.board.rows[self.side_arrow.coordinates[1]]:

                    if t.contents != None and t.contents.settled == False:

                        shifts.append(t.contents)

                shifts.reverse()#keeps plitka shifts from overlapping

                m = False

                for s in shifts:
                        
                    s.shift(1, 0)
                    m = True

                if m and self.sound_on:

                    self.scoot_sound.play()

            elif self.buttons[pygame.K_LEFT][2] == True:

                self.buttons[pygame.K_LEFT][2] = False
                self.buttons[pygame.K_LEFT][1] = 10

                if self.top_arrow.coordinates[0] > 12:

                    self.top_arrow.shift(-1, 0)

            elif self.buttons[pygame.K_RIGHT][2] == True:

                self.buttons[pygame.K_RIGHT][2] = False
                self.buttons[pygame.K_RIGHT][1] = 10

                if self.top_arrow.coordinates[0] < 21:

                    self.top_arrow.shift(1, 0)

            elif self.buttons[pygame.K_w][2] == True:

                self.buttons[pygame.K_w][2] = False
                self.buttons[pygame.K_w][1] = 10

                shifts = []

                for t in self.board.columns[self.top_arrow.coordinates[0]]:

                    if t.contents != None and t.contents.settled == False:

                        shifts.append(t.contents)

                m = False

                for s in shifts:

                    s.shift(0, -1)
                    m = True

                if m and self.sound_on:

                    self.scoot_sound.play()

            elif self.buttons[pygame.K_s][2] == True:

                self.buttons[pygame.K_s][2] = False
                self.buttons[pygame.K_s][1] = 10

                shifts = []

                for t in self.board.columns[self.top_arrow.coordinates[0]]:

                    if t.contents != None and t.contents.settled == False:

                        shifts.append(t.contents)

                shifts.reverse()#keeps plitka shifts from overlapping

                m = False

                for s in shifts:
                        
                    s.shift(0, 1)
                    m = True

                if m and self.sound_on:

                    self.scoot_sound.play()

            elif self.buttons[pygame.K_m][2] == True:

                self.buttons[pygame.K_m][2] = False
                self.buttons[pygame.K_m][1] = 10

                if self.sound_on == True:

                    self.sound_on = False
                    self.x_mark.visible = False

                    pygame.mixer.pause()

                    self.redraw_instructions = True

                elif self.sound_on == False:

                    self.sound_on = True
                    self.x_mark.visible = True

                    pygame.mixer.unpause()

                    self.redraw_instructions = True

        elif self.mode == 'RETRY':

            if self.buttons[pygame.K_RETURN][2] == True and (
                self.retry_delay == 0):

                self.buttons[pygame.K_RETURN][2] = False
                self.buttons[pygame.K_RETURN][1] = 10

                del self.board
                self.board = Board(self)

                self.plitka_timer = 100
                self.difficulty = 10
                self.clears = 0
                self.spawn = True
                self.timer = 0
                self.incrementor = 0
                self.max_plitkas = 2
                self.sound_on = True

                if self.score > self.highscore:
                    self.highscore = self.score

                self.score = 0

                self.cursor_follow = False
                self.redraw_instructions = True
                self.retry_timer = 60
                self.retry_prompt.rect.topleft = (-600, -600)

                self.mode = 'GAME'

            elif self.buttons[pygame.K_m][2] == True:

                self.buttons[pygame.K_m][2] = False
                self.buttons[pygame.K_m][1] = 10

                if self.sound_on == True:

                    self.sound_on = False
                    self.x_mark.visible = False

                    pygame.mixer.pause()

                    self.redraw_instructions = True

                elif self.sound_on == False:

                    self.sound_on = True
                    self.x_mark.visible = True

                    pygame.mixer.unpause()

                    self.redraw_instructions = True

        elif self.mode == 'START':

            if self.buttons[pygame.K_RETURN][2] == True and (
                self.start_timer == 0):

                self.buttons[pygame.K_RETURN][2] = False
                self.buttons[pygame.K_RETURN][1] = 10

                self.enter_prompt.rect.topleft = (-600, -600)

                self.mode = 'GAME'            

    def update(self):
        """
        Empty the screen, iterate game logic, then redraw
        the screen.
        """

        for k in self.buttons:

            if self.buttons[k][0] == True:
                if self.buttons[k][1] > 0:
                    self.buttons[k][1] -= 1
                else:
                    self.buttons[k][2] = True
            else:
                self.buttons[k][1] = 0

        if self.mode == 'GAME':

            if self.incrementor < 36:
                self.incrementor += 1
            elif self.timer < 1000:
                self.incrementor = 0
                self.timer += 1
                if self.timer == 200:
                    self.difficulty += 20
                    self.max_plitkas += 1
                elif self.timer == 400:
                    self.difficulty += 10
                    self.max_plitkas += 1
                elif self.timer == 600:
                    self.difficulty += 20
                elif self.timer == 800:
                    self.difficulty += 20
                    self.max_plitkas += 1

            self.board.tiles[(30, 2)].update(self.screen)
            self.board.tiles[(31, 2)].update(self.screen)
            self.board.tiles[(32, 2)].update(self.screen)

            self.screen.blit(self.score_header, (950, 46))
                    
            self.score_meter = self.font.render(str(self.score), False,
                                               (255, 255, 255))
            self.screen.blit(self.score_meter, (960, 66))

            if self.plitka_timer == 0:

                self.plitka_timer = 100 - self.difficulty
                s = random.random() + (self.difficulty / 100)
                if s > 0.5:
                    self.spawn = True
                self.board.shift_plitkas()
                self.spawn = False

            elif self.plitka_timer > 0:

                self.plitka_timer -= 1

            self.board.update(self.screen)#this should go first
            self.board.clear_dead_plitkas()

            self.side_arrow.update(self.screen)
            self.top_arrow.update(self.screen)

            if self.redraw_instructions:

                for i in self.instructions:

                    i.update(self.screen)
                    
                self.screen.blit(self.best_header, (86, 46))

                self.highscore_meter = self.font.render(str(self.highscore),
                                                    False, (255, 255, 255))

                self.screen.blit(self.highscore_meter, (96, 66))

                self.redraw_instructions = False

        elif self.mode == 'RETRY':

            if self.retry_delay > 0:
                self.retry_delay -= 1
            else:
                self.retry_prompt.rect.topleft = (344, 370)
                self.retry_prompt.set_animation('flash')

            s = pygame.Surface((self.retry_prompt.image.get_width(),
                               self.retry_prompt.image.get_height()))
            s.fill((0, 0, 0))

            self.screen.blit(s, self.retry_prompt.rect)

            self.retry_prompt.update(self.screen)

            if self.redraw_instructions:

                for i in self.instructions:

                    i.update(self.screen)
                    
                self.screen.blit(self.best_header, (86, 46))

                self.highscore_meter = self.font.render(str(self.highscore),
                                                    False, (255, 255, 255))

                self.screen.blit(self.highscore_meter, (96, 66))

                self.redraw_instructions = False

        elif self.mode == 'START':

            self.screen.fill((0, 0, 0))

            if self.start_timer > 0:

                self.start_timer -= 1

                if self.start_timer > 60:

                    for p in self.title_array:

                        self.title_array[p].move((0, 2))

                if self.start_timer == 239:

                    for p in self.title_array:

                        self.title_array[p].set_animation('shimmer')

                elif self.start_timer == 0:

                    self.music.play(loops=-1)
                    self.enter_prompt.rect.topleft = (344, 540)

            for pp in self.title_array:

                self.title_array[pp].update(self.screen)

            self.enter_prompt.update(self.screen)

        pygame.display.update()

    def mainloop(self):

        while self.on:

            self.shift_frames()
            self.handle_events()
            self.update()

        pygame.quit()

################################################################################

class Sheet(object):
    """
    Class for the spritesheets that entity images are loaded
    from. Supports regularized spritesheets only (all sprites
    feature the same dimensions).
    """

    def __init__(self, game, name, sprite_size, total_sprites):

        self.game = game

        #try and load all sprites on the sheet
        success = self.load_sheet(name, sprite_size, total_sprites)

        if success == 1:#failure, cleanup vals
            
            self.sprites = {}
            print "Failed to load sheet: " + name#error message

    def load_sheet(self, name, sprite_size, total_sprites):
        """
        Load a sheet and divide it into subsurfaces for
        use as images by sprite entities.
        """

        #remember important variables
        self.name = name
        self.sprite_size = sprite_size
        self.total_sprites = total_sprites

        #Step 1: attempt to load the appropriate image file
        try:

            self.sheet = pygame.image.load(os.path.join("data", "img", name))

        #catch a missing file error and stop, set up graceful failure
        except:

            self.sheet = None

        #Step 2: if sheet exists, divide it into sprites
        if self.sheet != None:

            self.sprites = {}#empty dict to hold our loaded images

            #vals to track our progress thru the sheet
            x = 0
            y = 0

            #while we still have more sprites to load, load them
            while len(self.sprites) < total_sprites:

                #get a rect that can be used to make a subsurface of the sheet
                new_rect = pygame.Rect((x * sprite_size[0], y * sprite_size[1]),
                                            sprite_size)

                #load image, store it in our dict, set its colorkey
                self.sprites[(x, y)] = self.sheet.subsurface(new_rect).convert()
                self.sprites[(x, y)].set_colorkey((255, 0, 255))

                x += 1#scoot over to the right

                #if we're hanging off the right side, scoot down and start over
                #again from the far left
                if x * sprite_size[0] >= self.sheet.get_width():

                    x = 0
                    y += 1

            return 0#SUCCESS!!

        #No sheet exists
        else:

            return 1# failure :C

################################################################################

class Entity(pygame.sprite.Sprite):
    """
    Visible game object parent class. Allows for drawing, moving,
    animating, and more. Basically expands on pygame.sprite.Sprite.
    """

    def __init__(self, game, sheet, sprite, animations, position,
                 visible = True):

        pygame.sprite.Sprite.__init__(self)

        self.game = game
        
        #loads image and makes rect
        self.sheet = sheet
        self.image = self.sheet.sprites[sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        #can be turned off if we don't want to be drawn
        self.visible = visible

        #determines if we get redrawn
        self.dirty = 1

        ########################
        #ANIMATIONS:           
        #Animations are a tuple of two values:
        #   (sprites, timer)
        #where 'sprites' is an ORDERED list of sheet positions values
        #and 'timer' is the amount of time that any one sprite will
        #be shown on the screen.
        #######################
        
        #Animation values. Remember:entity takes a whole dict of animations!
        self.animations = {}#dict which stores all animations
        self.current_animation = None
        self.current_sprite = sprite
        self.animation_timer = -1#-1 = off. this val is used for a countdown

        #setup all animations available to this entity's spritesheet
        if animations != None:
            
            for an in animations:

                self.setup_animation(an, animations[an][0], animations[an][1])

    def move(self, offset):
        """
        Move rect by the provided offset, from the topleft.
        """

        self.rect.topleft = (self.rect.topleft[0] + offset[0],
                             self.rect.topleft[1] + offset[1])

    def setup_animation(self, name, sprites, timer = 2):
        """
        Sets up an animation given a unique name, a list
        of sprite origin positions on the entity's sheet,
        and a timer. Sprites must be in an ordered list.
        """

        self.animations[name] = (sprites, timer)

    def set_animation(self, name):
        """
        Set the chosen animation as the current (active)
        animation, provided it is already in the animations
        list.
        """

        #check through the animations for the chosen animation
        if name in self.animations.keys():

            #setup all animation values for the new animation
            self.current_animation = self.animations[name]
            self.animation_timer = self.current_animation[1]
            self.current_sprite = self.current_animation[0][0]
            self.image = self.sheet.sprites[self.current_sprite]

        elif name == 'PLACEHOLDER':

            self.current_animation = None
            self.image = self.sheet.sprites[(0, 0)]
            self.current_sprite = (0, 0)
            self.animation_timer = -1

    def animate(self):
        """
        Countdown each frame from the maximum (the animation
        timer number) and shift frames when 0 is reached.
        """

        if self.animation_timer != -1:#animations are not off

            #if we are not at zero, countdown 1
            if self.animation_timer > 0:

                self.animation_timer -= 1

            #if we are, shift frames in the animation and reset the timer.
            else:

                self.shift_animation()
                self.animation_timer = self.current_animation[1]

    def shift_animation(self):
        """
        Shifts to the next sprite (frame) in the animation.
        """

        if self.current_animation != None:#make sure we actually have one

            sprites = self.current_animation[0]#'sprites' name for convenience

            #if the iterated sprite value is not out of range
            #NOTE: the same sprite loaction on the sheet cannot be repeated
            #in an animation because of the .index method. A sheet must
            #have a unique sprite for each location used in an animation
            if sprites.index(self.current_sprite) + 1 <= (len(sprites) - 1):

                newsp = sprites[sprites.index(self.current_sprite) + 1]

                self.current_sprite = newsp
                self.image = self.sheet.sprites[newsp]

            #else if the value is out of range, restart animation
            else:

                #shift to the first sprite in the list
                self.current_sprite = sprites[0]
                self.image = self.sheet.sprites[sprites[0]]

    def act(self, surface = None, *args):
        """
        Method to be overwritten with update data unique to subclasses. Can
        handle any arguments passed via update().
        """

        pass

    def update(self, surface = None, *args):

        self.act(surface, args)#method to be overwritten with unique update data

        #play an animation, if one is set
        if self.current_animation != None:

            self.animate()

        #finally, draw this entity if we can (surface exists and we're onscreen)
        r = surface.get_rect()
        
        if surface != None and self.rect.colliderect(r) and self.visible:

            surface.blit(self.image, self.rect)

################################################################################

class Tile(Entity):
    """
    Class for the background tiles that are involved in dirty
    blitting and coordination.
    """

    def __init__(self, game, sheet, sprite, animations, position, coordinates,
                 board):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.coordinates = coordinates
        self.board = board

        self.contents = None#none for empty, plitka reference for full

        self.playboard_tile = False#true if we're in range of the playboard

        #self.arrange()

        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def arrange(self):
        """
        Arranges this tile's position based on it's board
        coordinate.
        """

        self.rect.topleft = (self.coordinates[0] * TILE_WIDTH,
                             self.coordinates[1] * TILE_HEIGHT)

    def get_adjacents(self):

        for t in self.board.playboard:

            if t.coordinates == (self.coordinates[0] - 1, self.coordinates[1]):

                self.left = t

            elif t.coordinates== (self.coordinates[0] + 1, self.coordinates[1]):

                self.right = t

            elif t.coordinates== (self.coordinates[0], self.coordinates[1] - 1):

                self.top = t

            elif t.coordinates== (self.coordinates[0], self.coordinates[1] + 1):

                self.bottom = t

    def act(self, surface, *args):

        s = pygame.Surface((self.image.get_width(),
                            self.image.get_height()))
        s.fill((0, 0, 0))
        surface.blit(s, self.rect)

################################################################################

class Plitka(Entity):
    """
    Class for the multicolored tiles that drop. This is the
    parent class that the colored plitka's will source from.
    """

    def __init__(self, game, sheet, sprite, animations, position, color,
                 coordinates, tile):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.color = color
        self.settled = False
        self.tile = tile
        self.flagged = False
        self.coordinates = coordinates#based on which tile we're on
        self.kill_timer = 20

    def shift(self, direction_x, direction_y):

        old_coords = self.coordinates

        if (self.coordinates[0] + direction_x) in range(12, 22):
            
            self.coordinates = (self.coordinates[0] + direction_x,
                                self.coordinates[1])

        if (self.coordinates[1] + direction_y) in range(5, 20):
            
            self.coordinates = (self.coordinates[0],
                                self.coordinates[1] + direction_y)

        return self.reposition(old_coords)

    def reposition(self, previous_coords):
        """
        Makes position and rect match coordinates.
        """

        repo = True

        for t in self.game.board.playboard:

            if t.coordinates == self.coordinates and t.contents == None:
                
                self.tile.contents = None
                self.tile = t
                t.contents = self

        if self.coordinates != self.tile.coordinates:

            self.coordinates = previous_coords
            repo = False

        self.rect.topleft = self.tile.rect.topleft
        return repo

    def check_settled(self):
        """
        Checks if the tile below this plitka is filled, or is the
        floor, and if so, changes to settled.
        """

        if self.coordinates[1] == 19 and self.settled == False:#bottom of board

            self.settled = True
            self.set_animation('shimmer')

        if self.tile.bottom != None:

            if self.tile.bottom.contents != None and (
                self.tile.bottom.contents.settled):

                if self.settled == False:

                    self.settled = True
                    self.set_animation('shimmer')

            else:

                self.settled = False
                self.set_animation('PLACEHOLDER')

        if self.tile.top != None and self.tile.top.contents != None and (
            self.settled == False):

            self.tile.top.contents.check_settled()

    def be_cleared(self):

        self.visible = False
        self.settled = False
        self.coordinates = (-60, -60)
        self.rect.topleft = (-900, -900)

        self.game.score += 100

        self.game.board.plitkas.remove(self)
        self.tile.contents = None
        self.kill()

    def act(self, surface, *args):

        if self.flagged and self.kill_timer > 0:

            self.kill_timer -= 1

################################################################################

class Tile_Overlay(Entity):
    """
    Class for the object that overlays the game board to
    show selected rows and columns.
    """

    def __init__(self, game, sheet, sprite, animations, position, coordinates,
                 tile, arrow):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.coordinates = coordinates
        self.tile = tile
        self.arrow = arrow

    def act(self, surface, *args):

        self.rect.topleft = self.tile.rect.topleft

################################################################################

class Arrow(Entity):
    """
    Class for the arrows that the player controls to guide
    the plitkas.
    """

    def __init__(self, game, sheet, sprite, animations, position, coordinates,
                 tile):

        Entity.__init__(self, game, sheet, sprite, animations, position)

        self.coordinates = coordinates
        self.tile = tile
        self.overlays = []

    def make_overlays(self, xvals, yvals):

        for x in xvals:
            
            for y in yvals:

                self.overlays.append(Tile_Overlay(self.game,
                                     self.game.sheets['selection_overlay.png'],
                                     (0, 0), None, (x * TILE_WIDTH,
                                                    y * TILE_HEIGHT),
                                     (x, y), self.game.board.tiles[(x, y)],
                                      self))

    def shift(self, x_offset, y_offset):
        """
        Moves the arrow and all its overlays by the offset.
        """

        self.tile.update(self.game.screen)#maybe

        self.coordinates = (self.coordinates[0] + x_offset,
                            self.coordinates[1] + y_offset)
        self.tile = self.game.board.tiles[self.coordinates]

        for o in self.overlays:

            o.coordinates = (o.coordinates[0] + x_offset,
                             o.coordinates[1] + y_offset)
            o.tile = self.game.board.tiles[o.coordinates]

    def act(self, surface, *args):

        if self.tile.coordinates[1] > 4:

            self.tile.update(self.game.screen)#maybe

        self.rect.topleft = self.tile.rect.topleft

        for o in self.overlays:

            o.update(surface)

################################################################################

class Board(object):
    """
    Class that manages the background tiles, which have special
    coordinate properties.
    """

    def __init__(self, game):

        self.game = game

        self.tiles = {}#eventually support multiple bgs
        self.playboard = []

        self.plitkas = []

        self.rows = {}
        self.columns = {}

        self.make_tiles()

    def make_tiles(self):
        """
        Create all the tiles that make up the background.
        """

        for x in range(0, TILE_COLS):

            for y in range(0, TILE_ROWS):

                #undo hardcoded filename
                self.tiles[(x, y)] = Tile(self.game,
                                          self.game.sheets['default_bg.png'],
                                          (x, y), None, (x * TILE_WIDTH,
                                          y * TILE_HEIGHT), (x, y), self)

        #devise playboard
        for t in self.tiles:

            if self.tiles[t].coordinates[0] in range(12, 22) and (
               self.tiles[t].coordinates[1] in range(4, 20)):

                self.playboard.append(self.tiles[t])

                if self.tiles[t].coordinates[1] != 4:

                    self.tiles[t].playboard_tile = True
                    self.tiles[t].image = self.game.sheets['TileGrid.png'
                                                           ].sprites[(0,0)]

        for bx in range(12, 22):

            self.columns[bx] = []

        for by in range (4, 20):

            self.rows[by] = []

        self.playboard.sort()#python is best language, and list is best girl <3

        for bt in self.playboard:

            bt.get_adjacents()

            for cols in self.columns:

                if bt.coordinates[0] == cols:

                    self.columns[cols].append(bt)
                    
            for rows in self.rows:

                if bt.coordinates[1] == rows:

                    self.rows[rows].append(bt)

    def spawn_plitkas(self):
        """
        Spawn a series of 1 to 5 plitkas at the top of the board.
        """

        pks = random.randint(1, self.game.max_plitkas)
        count = 0

        while count < pks:
        
            for t in self.rows[4]:

                    if count < pks and t.contents == None:

                        r = random.randint(0, 16)

                        if r == 5:

                            p = Plitka(self.game,
                                self.game.sheets['Blue_Plitka.png'], (0, 0),
                                ANIMATIONS['Blue_Plitka.png'], t.rect.topleft,
                                'BLUE', t.coordinates, t)

                            self.plitkas.append(p)

                            t.contents = p

                            count += 1

                        elif r == 6:

                            p = Plitka(self.game,
                                self.game.sheets['Red_Plitka.png'], (0, 0),
                                ANIMATIONS['Red_Plitka.png'], t.rect.topleft,
                                'RED', t.coordinates, t)

                            self.plitkas.append(p)

                            t.contents = p

                            count += 1

                        elif r == 7:

                            p = Plitka(self.game,
                                self.game.sheets['Green_Plitka.png'], (0, 0),
                                ANIMATIONS['Green_Plitka.png'], t.rect.topleft,
                                'GREEN', t.coordinates, t)

                            self.plitkas.append(p)

                            t.contents = p

                            count += 1

                        elif r == 8:

                            p = Plitka(self.game,
                                self.game.sheets['Cyan_Plitka.png'], (0, 0),
                                ANIMATIONS['Cyan_Plitka.png'], t.rect.topleft,
                                'CYAN', t.coordinates, t)

                            self.plitkas.append(p)

                            t.contents = p

                            count += 1

                        elif r == 9:

                            p = Plitka(self.game,
                                self.game.sheets['Yellow_Plitka.png'], (0, 0),
                                ANIMATIONS['Yellow_Plitka.png'], t.rect.topleft,
                                'YELLOW', t.coordinates, t)

                            self.plitkas.append(p)

                            t.contents = p

                            count += 1

    def check_clears(self):
        """
        Flags all plitkas that are lined up in rows or columns.
        """

        for c in self.columns:

            red = []
            blue = []
            green = []
            cyan = []
            yellow = []

            for pc in self.columns[c]:

                if pc.contents != None and pc.contents.color == 'BLUE' and (
                    pc.contents.settled == True):

                    red = []
                    green = []
                    cyan = []
                    yellow = []

                    blue.append(pc.contents)

                    if len(blue) >= 4:

                        for b in blue:

                            b.flagged = True

                elif pc.contents != None and pc.contents.color == 'RED' and (
                    pc.contents.settled == True):

                    blue = []
                    green = []
                    cyan = []
                    yellow = []

                    red.append(pc.contents)

                    if len(red) >= 4:

                        for r in red:

                            r.flagged = True

                elif pc.contents != None and pc.contents.color == 'GREEN' and (
                    pc.contents.settled == True):

                    red = []
                    blue = []
                    cyan = []
                    yellow = []

                    green.append(pc.contents)

                    if len(green) >= 4:

                        for g in green:

                            g.flagged = True

                elif pc.contents != None and pc.contents.color == 'CYAN' and (
                    pc.contents.settled == True):

                    red = []
                    green = []
                    blue = []
                    yellow = []

                    cyan.append(pc.contents)

                    if len(cyan) >= 4:

                        for n in cyan:

                            n.flagged = True

                elif pc.contents != None and pc.contents.color == 'YELLOW' and (
                    pc.contents.settled == True):

                    red = []
                    green = []
                    cyan = []
                    blue = []

                    yellow.append(pc.contents)

                    if len(yellow) >= 4:

                        for w in yellow:

                            w.flagged = True

                elif pc.contents == None:

                    red = []
                    blue = []
                    green = []
                    cyan = []
                    yellow = []

        for r in self.rows:

            red = []
            blue = []
            green = []
            cyan = []
            yellow = []

            for rc in self.rows[r]:

                if rc.contents != None and rc.contents.color == 'BLUE' and (
                    rc.contents.settled == True):

                    red = []
                    green = []
                    cyan = []
                    yellow = []

                    blue.append(rc.contents)

                    if len(blue) >= 4:

                        for b in blue:

                            b.flagged = True

                elif rc.contents != None and rc.contents.color == 'RED' and (
                    rc.contents.settled == True):

                    blue = []
                    green = []
                    cyan = []
                    yellow = []

                    red.append(rc.contents)

                    if len(red) >= 4:

                        for r in red:

                            r.flagged = True

                elif rc.contents != None and rc.contents.color == 'GREEN' and (
                    rc.contents.settled == True):

                    red = []
                    blue = []
                    cyan = []
                    yellow = []

                    green.append(rc.contents)

                    if len(green) >= 4:

                        for g in green:

                            g.flagged = True

                elif rc.contents != None and rc.contents.color == 'CYAN' and (
                    rc.contents.settled == True):

                    red = []
                    green = []
                    blue = []
                    yellow = []

                    cyan.append(rc.contents)

                    if len(cyan) >= 4:

                        for n in cyan:

                            n.flagged = True

                elif rc.contents != None and rc.contents.color == 'YELLOW' and (
                    rc.contents.settled == True):

                    red = []
                    green = []
                    cyan = []
                    blue = []

                    yellow.append(rc.contents)

                    if len(yellow) >= 4:

                        for w in yellow:

                            w.flagged = True

                elif rc.contents == None:

                    red = []
                    blue = []
                    green = []
                    cyan = []
                    yellow = []

    def check_loss(self):

        for t in self.rows[4]:

            if t.contents != None and t.contents.settled == True:

                if self.game.sound_on:

                    self.game.die_sound.play()

                self.game.mode = 'RETRY'

    def shift_plitkas(self):
        """
        Shifts plitkas downward and spawns new ones.
        """

        to_shift = []

        for p in self.plitkas:

            if p.settled == False:

                to_shift.append(p)

        while len(to_shift) > 0:

            for tp in to_shift:

                shifted = tp.shift(0, 1)

                if shifted:
                    to_shift.remove(tp)

        if self.game.side_arrow.coordinates[1] < 19 and (
            self.game.cursor_follow == True):

            self.game.side_arrow.shift(0, 1)

        if self.game.spawn == True:

            self.spawn_plitkas()

        self.check_clears()
        self.check_loss()

    def clear_dead_plitkas(self):

        clear = False#for sound

        #check every clear, then destroy one time for all
        for p in self.plitkas:

            if p.flagged == True and p.kill_timer == 0:

                p.be_cleared()
                clear = True

        if clear == True and self.game.sound_on == True:

            self.game.clear_sound.play()

    def update(self, surface = None):#would like to eventually make tiles use
                                     #a group.

        for t in self.tiles:

            if self.game.redraw_instructions:

                self.tiles[t].update(surface)

            else:

                if self.tiles[t] in self.playboard:

                    self.tiles[t].update(surface)

        for p in self.plitkas:

            p.check_settled()

            if p.visible:

                p.update(surface)
        
        self.check_clears()
        self.check_loss()
        
