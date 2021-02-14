# pygameを読み込む
import pygame

class snake:
    """
    Snakeクラス
    """

    # snakeの色
    COLOR = [0, 170, 0]
    # snakeの長辺の長さ __snakeが長方形で描かれているが長い辺のこと
    SIDE = 15
    # snakeの長さ __綴りを修正して入力している __長辺の長さを定義しsnakeの長さを定義
    length = 2
    # snakeの移動速度(velocity) __velocity:速度
    vel = 10

    def __init__(self, surface):
        """
        初期化関数
        """
        # Surfaceクラスのインスタンス__を生成し、
        self.surface = surface # 括弧付けなくても大丈夫か？
        # 画面の横幅の整数値 __を取得します（//は割った商の整数 __を取得することができる） __mac行コピー:⌘+Cだけ
        self.x = surface.get_width() // 2
        # 画面の縦幅の整数値（//は割った商の整数） __mac次の行：⌘＋Enter
        self.y = surface.get_height() // 4
        # 画面の縦横のタプルをリストに入れる __mac行末：fn + →
        self.XY = [(self.x, self.y)]
        # 移動方向　l=左 r=右 d=下 u=上 __なのだが最初にダイレクションとしてdを入力していく
        self.direction = "d"

    def add_length(self):
        """
        snakeを長くする
        """
        # 1長くする
        self.length += 1 #綴りは元を修正して入力
        # 長辺の長さを1長くする
        self.SIDE += 1
        # RGBのGを濃くする
        self.COLOR[1] += 1
        # RGBのGの最大値は255、min関数は2つのうち小さい方を選ぶ
        self.COLOR[1] = min(self.COLOR[1], 255)

    def get_snake(self):
        """
        snakeを描画
        """
        self.XY += [(self.x, self.y)]
        self.XY = self.XY[-self.length:] #綴りは修正して入力
        # snakeの体をブロックごとに描写 __する処理をここではやっている
        for kx, ky in self.XY:
            pygame.draw.rect(self.surface, self.COLOR, (kx, ky, self.SIDE, self.SIDE))

    def move_snake(self, key):
        """
        snakeをキー操作
        """

        # 左へ操作
        if key == "l":
            # 左方向へ速度を加算 __左方向はx軸の負の方向なのでマイナス
            self.x -= self.vel
            self.get_snake()
        # 右へ操作
        if key == "r":
            # 右方向へ速度を加算
            self.x += self.vel
            self.get_snake()
        # "上"へ操作 __同様に下へ操作する時は減算する必要があって画面の上方向は負の方向になるので引いている
        if key == "u":
            # "上"方向へ速度を加算
            self.y -= self.vel
            self.get_snake()
        # "下"へ操作
        if key == "d":
            # "下"方向へ速度を加算
            self.y += self.vel
            self.get_snake()
        # X軸正方向が右，Y軸正方向が下となります．数学の座標軸とY軸だけ逆方向なので注意して下さい．
        # Picthon(ピクトグラミングPython版）使い方よりーPictogramming より