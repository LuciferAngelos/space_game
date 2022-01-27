class Stats():
    '''отслеживание статистики'''

    def __init__(self):
        '''инициализирует статистику'''
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        ''''статистика, меняющаяся во время игры'''
        self.lives = 3
        self.score = 0
