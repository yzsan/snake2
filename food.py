# pygameを読み込む
import pygame
# randomライブラリのrandint__(ランダムイント）関数を読み込む
from random import randint
# ランダムイント関数はint型（integer:整数）のランダム値を取得することができます。
class Food:
    """
    Foodクラス このターミナルの抜け方：__Use quit() or Ctrl-D (i.e. EOF) to exit
    """

    # RGBで色を設定
    COLOR = (255, 0, 0)
    # 大きさ
    SIDE = 25

    def __init__(self, surface):
        """
        初期化関数
        """
        # Surfaceクラスのインスタンス __を取得
        self.surface = surface
        # foodのx座標 __を取得
        self.x = self.SIDE
        # foodのy座標 __を取得
        self.y = self.SIDE
        # x座標の場合 __set関数を使って変数に入れておきます。
        self.set_x = set()
        # y座標の場合
        self.set_y = set()

    def add_food(self):
        """
        foodを追加
        """
        # foodを描画 __pygame.draw.rect:四角形を描写:(Surface, color, Rect(:＊＊left, top, width, height＊＊), width=0)
        pygame.draw.rect(self.surface, self.COLOR, (self.x, self.y, self.SIDE, self.SIDE))
        # foodのx軸方向の領域。setで管理
        self.set_x = set(range(self.x, self.x + self.SIDE + 1))
        # foodのy軸方向の領域。setで管理/__setというのは「集合」のこと
        self.set_y = set(range(self.y, self.y + self.SIDE))

    def new_foodxy(self, snake_side):
        """
        新しいfoodの位置を設定
        """
        # snakeの大きさを考慮してランダムに配置
        self.x = randint(snake_side, self.surface.get_width() - snake_side)
        self.y = randint(snake_side, self.surface.get_height() - snake_side)

    def is_eaten(self,snake_x, snake_y, snake_side):
        """
        foodとsnakeの当たり判定
        """

        # snakeの座標をset(集合)で管理。foodとのset(集合)とで共通集合があれば当たったと判定
        if set(range(snake_x, snake_x + snake_side +1)) & self.set_x and set(range(snake_y, snake_y + snake_side +1)) & self.set_y:
            return True
        return False
        # 座標の集合とって同じ座標があると当たっているよね、というようなことをやっている。


