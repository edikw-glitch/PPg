import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лабиринт")
font = pygame.font.Font(None, 32)
background = pygame.Surface(screen.get_size())
background.fill((30, 30, 30))

image_o_p = "data/lab.png"
image_o_r = pygame.image.load(image_o_p)

image_left_p = "data/lab_left.png"
image_left = pygame.image.load(image_left_p)

image_port_p = "data/lab_port.png"
image_port = pygame.image.load(image_port_p)

image_rush_p = "data/lab_rush.png"
image_rush = pygame.image.load(image_rush_p)


def draw_text(text, position):
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, position)


class Button:
    def __init__(self, text, pos, action):
        self.text = text
        self.pos = pos
        self.action = action
        self.rect = pygame.Rect(pos[0], pos[1], 200, 50)

    def draw(self):
        pygame.draw.rect(screen, (100, 100, 255), self.rect)
        draw_text(self.text, (self.pos[0] + 20, self.pos[1] + 10))

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.action()


def game_over():
    buttons = [
        Button("Начать заново", (50, 200), start_game),
        Button("Закрыть игру", (50, 260), pygame.quit)
    ]
    while True:
        screen.blit(background, (0, 0))
        draw_text("Игра окончена", (50, 50))
        draw_text("Хотите сыграть снова?", (50, 100))
        for button in buttons:
            button.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in buttons:
                    button.check_click(mouse_pos)


def start_game():
    buttons = [
        Button("Налевво", (50, 200), lambda: first_choice("Налевво")),
        Button("Прямо", (50, 260), lambda: first_choice("Прямо")),
        Button("Направо", (50, 320), lambda: first_choice("Направо")),
    ]
    while True:
        screen.blit(background, (0, 0))
        screen.blit(image_o_r, (400, 400))
        draw_text("Здравствуйте, дорогой первопроходец", (50, 50))
        draw_text("Ты находишься в лабиринте, найди истинный путь,", (50, 100))
        draw_text("чтобы 'сбежать' отсюда. Выберите одну из дверей:", (50, 150))
        for button in buttons:
            button.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in buttons:
                    button.check_click(mouse_pos)


def first_choice(choice):
    screen.blit(background, (0, 0))
    if choice == "Налевво":
        draw_text("Вы решили пойти в левую дверь, вы увидели еще одну развилку.", (50, 50))
        draw_text("Куда пойдете? (Направо, Налевво)", (50, 100))
        screen.blit(image_left, (400, 400))
        buttons = [
            Button("Направо", (50, 200), lambda: left_choice("Направо")),
            Button("Налевво", (50, 260), lambda: left_choice("Налевво")),
        ]
    elif choice == "Прямо":
        draw_text("Вы решились зайти в дверь по середине.", (50, 50))
        draw_text("Была только дверь налево.", (50, 100))
        screen.blit(image_rush, (400, 400))
        buttons = [
            Button("Налевво", (50, 260), lambda: straight_choice("Налевво")),
        ]
    elif choice == "Направо":
        draw_text("Зайдя в правую дверь, вы видите 3 портала.", (50, 50))
        draw_text("Так в какой пойти? (1, 2, 3)", (50, 100))
        screen.blit(image_port,(400, 400))
        buttons = [
            Button("Портал 1", (50, 200), lambda: right_choice("1")),
            Button("Портал 2", (50, 260), lambda: right_choice("2")),
            Button("Портал 3", (50, 320), lambda: right_choice("3")),
        ]

    while True:
        pygame.display.flip()
        for button in buttons:
            button.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in buttons:
                    button.check_click(mouse_pos)


def left_choice(choice):
    screen.blit(background, (0, 0))
    screen.blit(image_left, (400, 400))
    if choice == "Направо":
        draw_text("Войдя в правую дверь, вы оказываетесь в комнате,", (50, 50))
        draw_text("где вас никто не видел.", (50, 100))
        buttons = [Button("Начать заново", (50, 200), start_game)]
    elif choice == "Налевво":
        draw_text("Вы решаете пойти в левую дверь и клачок бумаги.", (50, 50))
        draw_text("На нём говориться про какое-то 3 и сон", (50, 100))
        draw_text("Чтобы это значило?А потом осознаёте что двери нет в этой комнате....", (50, 150))
        buttons = [Button("Начать заново", (50, 200), start_game)]

    while True:
        for button in buttons:
            button.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in buttons:
                    button.check_click(mouse_pos)


def straight_choice(choice):
    screen.blit(background, (0, 0))
    screen.blit(image_rush, (400, 400))
    if choice == "Налевво":
        draw_text("Вы решили пойти налево и нашли огромный тунель.", (50, 50))
        draw_text("Вы решаете пойти в него и счастье вы вышли!", (50, 100))
        buttons = [Button("Начать заново", (50, 200), start_game)]

    while True:
        for button in buttons:
            button.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in buttons:
                    button.check_click(mouse_pos)


def right_choice(portal):
    screen.blit(background, (0, 0))
    if portal == "1":
        draw_text("Вы выходите к деревне.", (50, 50))
        draw_text("И решаете остаться в ней и забыть обо всём", (50, 100))
        buttons = [Button("Начать заново", (50, 200), start_game)]
    elif portal == "2":
        draw_text("Вы попали на поле битвы и вас убивают...", (50, 50))
        buttons = [Button("Начать заново", (50, 200), start_game)]
    elif portal == "3":
        draw_text("Это был всего лишь сон. Вы просыпаетесь!", (50, 50))
        draw_text("Что очень вас удивляет ,что это просто сон", (50, 100))
        draw_text("Вы решили сделать кофе ведь ещё нужно ", (50, 150))
        draw_text("закончить проект который вы не доделали", (50, 200))
        draw_text("И да прибудут с вами боги .--- .- ...- .-!", (50, 250))
        buttons = [
            Button("Начать заново", (50, 300), start_game),
            Button("Закрыть игру", (50, 370), pygame.quit)
        ]

    while True:
        for button in buttons:
            button.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in buttons:
                    button.check_click(mouse_pos)


if __name__ == "__main__":
    start_game()