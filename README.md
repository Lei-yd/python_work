##项目介绍
该项目是在学习《Python编程：从入门到实践》时编写的《外星人入侵》游戏，代码基本与书中一致，且修复了书中关于外星人移动后一整行外星人重叠到一处的问题。
##修复外星人位置重叠问题：
原代码将外星人移动时的x坐标值放在init中，修复后将self.x = float(self.rect.x)放在update中，故在计算外星人移动时的x值时使用的是外星人生成时的x坐标值，而非init中定义的初始值。
def update(self):
        """向右移动外星人"""
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x 
