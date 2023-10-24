import pygame
from constant import *





class PygameApp:
    def __init__(self):
        pygame.init()

        # 游戏窗口大小
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600

        # 创建游戏窗口
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Pygame 示例")

        # 图像加载器
        self.image_loader = self.ImageLoader(self.window)

    # 图像加载器类
    class ImageLoader:
        def __init__(self, window):
            self.images = []
            self.window = window  # 传递窗口对象

            # 请替换以下路径为你的图像文件路径
            for path in IMAGE_NAME_LIST:
                image = pygame.image.load(path)
                self.images.append(image)

        def get_item_image_by_ID(self, index, row, col):
            rect = pygame.Rect(IMAGE_LOCATION_LIST[index][0], IMAGE_LOCATION_LIST[index][1], 32, 32)
            self.window.blit(self.images[1].subsurface(rect), (6 * 32, 2 * 32))
            return self.images[1].subsurface(rect)

    def draw_image(self):
        # 绘制图像
        self.image_loader.get_item_image_by_ID(1, 6 * 32, 2 * 32)
        self.image_loader.get_item_image_by_ID(5, 6 * 32, 2 * 32)

    def clear_image(self):
        # 清空屏幕
        self.window.fill((0, 0, 0))

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # 清空屏幕
            self.window.fill((0, 0, 0))
            self.draw_image()



            # 刷新屏幕
            pygame.display.flip()

            # 控制游戏帧率
            clock.tick(60)

        # 游戏结束后，关闭 Pygame
        pygame.quit()



