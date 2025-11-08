class GameStarts:
    """跟踪统计游戏的信息"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_starts()
        # 在任何情况下都不应该重置最高分
        self.high_score = 0

    def reset_starts(self):
        """初始化游戏期间可能变化的统计信息"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
