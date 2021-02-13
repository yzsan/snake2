# pygameを読み込む
import pygame
# sysライブラリを読み込む
import sys
# pygameのlocalファイルにあるすべての変数、関数、クラスを読み込む
from pygame.locals import *
# GUI表示ライブラリtkinterを読み込む
import tkinter as tk
# os関数の処理をするosライブラリを読み込む
import os
# snake.pyにあるすべての変数、関数、クラスを読み込む
from snake2 import *
# food.pyにあるすべての変数、関数、クラスを読み込む
from food import *
# background.pyにあるすべての変数、関数、クラスを読み込む
from background.py import *
# effects.pyにあるすべての変数、関数、クラスを読み込む
from effects import *

class Game:
    """　__複数行でのコメント
    Gameクラス

    Game全体を管理するクラス
    """
    # 画面の大きさ
    SIZE = WIDTH, HEIGHT = (800, 800)

    # 色情報をRBGで管理
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0

    # frame per second,1秒中のフレーム数、フレーム数が多いと滑らかになるが処理が遅くなる
    fps = 20
    # スコア
    score = 0

    def __init__(self):
        """
        初期化関数
        """

        # 謎の処理
        os.environ["SDL_VIDEO_WINDOW_POS] = f'{(tk.Tk().winfo_screenwidth() - self.WIDTH)
        f'{(tk.Tk().winfo_screenheight() - self.HEIGHT) // 2}'
        
        # pygame mixerの初期設定 ＊＊音声を読み込んで再生するためのpygameのモジュール
        pygame.mixer.pre_init(44100, -16, 2048)　# __mixerモジュールを初期化する引数を事前に設定
        pygame.mixer.init()　# __mixerモジュールを初期化
        # pygameの初期化
        pygame.init()
        # MIDファイルのロード
        pygame.mixer.music.load("System/sounds/music.mid")
        # 音楽を再生
        pygame.mixer.music.play(9)
        # ゲーム表示画面のキャプション名を設定
        pygame.display.set_caption("Snake")

        # 効果音「ゲームオーバー」を変数に設定 __Soundはクラスの模様
        self.sound_game_over = pygame.mixer.Sound("System/Sounds/game_over.wav") 
        # 効果音「Snakeが食べ物を食べた時の音」を変数に設定
        self.sound_eat_food = pygame.mixer.Sound("System/Sounds/eat_food.wav")
        # 画像を描写するために使用するSurfaceクラスからインスタンスを生成
        self.surf = pygame.display.set_mode(self.SIZE) #__インスタンス化：クラスを使えるような状態にすること。基本は『インスタンス名＝クラス名（実引数１，実引数２…）』
        # 時間の設定
        self.clock = pygame.time.Clock()

        # 背景のインスタンスを生成
        self.bg = BG(self.surf)
        # effectのインスタンスを生成
        self.effect = Effect(self.surf)
        # effectのトリガー変数
        self.effect_trigger = False
        # snakeのインスタンスを生成
        self.snake = Snake(self.surf)
        # foodのインスタンスを生成
        self.food = Food(self.surf)

        # スコア表示のフォント
        self.font_score = pygame.font.Font(None, 22)
        # 終了表示のフォント
        self.font_end = pygame.font.Font(None, 48)
        # ボタンのフォント
        self.font_button =pygame.font.Font(None, 30)

        # play関数を実行
        self.play() # __メソッドの実行 a = Student() →　a.avg()

    def play(self):
        """
        キー操作
        foodを食べた時の処理
        ゲームオーバー判定
        """

        # ゲーム終了しない限り実行
        while True:
            # 終了コマンドを設定
            for event in pygame.event.get() #sho解説にもあり
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # キーを押したことを判定 __フォントを13から12に変更
            keys = pygame.key.get_pressed()
            
            # 左またはaを押した __snakeの動き方をここで定義
            if keys[K_LEFT] or keys[K_a]:
                #進行方向が右でない __進行方向が右でなかったら右にする。
                if self.snake.direction != "r": # __!=(ノットイコール)比較演算子
                    # 進行方向を左に設定
                    self.snake.direction = "l"
            # 右またはdを押した
            elif keys[K_RIGHT] or keys[K_d]:
                #進行方向が左ではない
                if self.snake.direction != "l":
                    # 進行方向を右に設定
                    self.snake.direction = "r"
            # 上またはwを押した
            elif keys[K_UP] or keys[K_w]:
                #進行方向がしたではない
                if self.snake.direction != "d":
                    #進行方向が上に設定
                    self.snake.direction = "u"
            # 下またはsを押した
            elif keys[K_DOWN] or keys[K_s]:
                #進行方向が上ではない
                if self,snake.direction != "u":
                    #進行方向が下に設定
                    self.snake.direction = "d"

            # foodがsnakeに食べられた
            if self.food.is_eaten(self.snake.x, self.snake.y, self.snake.SIDE):
                # foodを食べる効果音を再生
                self.sound_eat_food.play()
                # snakeの長さが伸びる
                self.snake.add_length() #__実は元のGitHubは綴りが間違っている。
                #effectのトリガーがTrue
                self.effect_trigger = True
                #新しいfoodを配置
                self.food.new_foodxy(self.snake.SIDE)
                #スコアを加算
                self.score += 1
                #fpsが加算。速度が速くなり難易度が上がる
                self.fps += 1

            # snakeが画面外に出たらゲームオーバー __↓ちょっとこれはコピーで対応
            if(self.snake.x < 0 or self.snake.y < 0 or self.snake.x + self.snake.SIDE > self.WIDTH or self.snake.y + self.snake.SIDE > self.HEIGHT) or len(self.snake.XY) != len(set(self.snake.XY)):
                self.game_over()

            # draw関数を実行
            self.draw()

    def draw(self):
        """
        描画関数
        """
        # 画面を黒にして描画して初期化
        self.surf.fill(self.BLACK) #shoではwindow.fill((0, 0, 0))
        # スコア表示
        self.surf.blit(self.font_score.render(f'SCORE:{self.score}', 1, (255, 165, 0), (self.WIDTH - -90, 5))

        # 背景を描画
        self.bg.draw(self.snake.direction)
        # foodを描画
        self.food.add_food()

        #snakeの移動を描画
        self.snake.move_snake(self.snake.direction) 
        
        # effectを実行
        self.effect.run(self.effect_trigger, snake.x, self.snake.y)
        # effectトリガーをFalse
        self.effect_trigger = False

        # pygameのディスプレイをupdate
        pygame.display.update() # __shoでもdef reDrawWindowにて同様。
        # fpsを更新
        self.clock.tick(self.fps)

    def game_over(self):
        """
        ゲームオーバー処理
        """
        # 音楽を停止
        pygame.mixer.music.stop()
        # 効果音「ゲームオーバー」を再生
        self.sound_game_over.play()

        #次の処理をするまで実行し続ける
        while True:
            # スコアの結果を表示
            self.surf.blit(self.font_end.render{f'YOUR SCORE:{self.score}', 1, (255, 165, 0)}, (self.WIDTH // 2 -130, self.HEIGHT // 3))

            # mouseのポインタ位置
            mouse_coord = pygame.mouse.get_pos()
            # mouseのクリックイベント
            mouse_events = pygame.mouse.get_pressed()


            #retryボタンにマウスホバーすると色が変わる __途中からはGitHubからコピー
            if self.WIDTH // 2 - 50 <mouse_coord[0] <self.WIDTH // 2 +50 and \
            self.HEIGHT // 2 - 50 < mouse_coord[1] < self.HEIGHT // 2 -10:
                # 緑の長方形を描画
                pygame.draw.rect(self.surf, self.GREEN, (self.WIDTH // 2 - 50, self.HEIGHT // 2 -50, 100 ,40))
                if mouse_events[0]:
                    #RETRYボタン領域をクリック
                    break
            else:
                # 赤の長方形を描画
                pygame.draw.rect(self.surf, self.RED, (self.WIDTH // 2 - 50, self.HEIGHT // 2 -50, 100 ,40))

            # RETRYの文字表示 __ここはコピーした
            self.surf.blit(self.font_button.render("RETRY", 1, self.BLACK), (self.WIDTH // 2 - 33, self.HEIGHT // 2 - 40))

            # fpsを更新
            self.clock.tick(self.fps)
            # ディスプレイを更新
            pygame.display.update()

            # 終了コマンド
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
        # Gameクラスを初期化してリトライ
        game()

if __name__ == "__main__":
    # Gameクラスを初期化してスタート
    Game()
        

