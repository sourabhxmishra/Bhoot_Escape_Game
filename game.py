"""Bhoot Escape — a 2D dodge-the-ghosts arcade game built with pygame.

Falling *bhoots* (ghosts) drop down three lanes; slide left/right to dodge them.
Every ghost you dodge scores a point, a hit costs a life, and the ghosts speed
up the longer you survive. It's tiny, so it runs happily on low-end hardware.

Controls:  ← →  (or A / D) move  ·  SPACE  start / restart  ·  Esc / Q  quit
Run:       python game.py         (needs pygame — see requirements.txt)
"""
import asyncio
import os
import sys
import random

import pygame


def resource(name):
    """Find a bundled asset whether running from source or a PyInstaller .exe."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


WIDTH, HEIGHT = 360, 640
LANES = (30, 150, 270)          # x of the three lanes
FPS = 60
START_LIVES = 3
PLAYER = (60, 70)
WHITE, GREEN, RED = (240, 240, 240), (0, 220, 120), (235, 70, 70)


def load(name, size):
    image = pygame.image.load(resource(name)).convert_alpha()
    return pygame.transform.smoothscale(image, size)


class Ghost:
    def __init__(self, image):
        self.image = image
        self.w, self.h = image.get_size()
        self.spawn(first=True)

    def spawn(self, first=False):
        self.lane = random.randrange(len(LANES))
        self.x = LANES[self.lane]
        self.y = -random.randint(60, 720 if first else 320)

    def rect(self):
        return pygame.Rect(self.x, int(self.y), self.w, self.h)

    def fall(self, speed):
        self.y += speed
        if self.y > HEIGHT:          # dodged
            self.spawn()
            return True
        return False


def draw_heart(surf, cx, cy, s, color):
    """Draw a small heart (two circles + a triangle) so it needs no font glyph."""
    r = max(3, s // 4)
    pygame.draw.circle(surf, color, (cx - r, cy - r // 2), r)
    pygame.draw.circle(surf, color, (cx + r, cy - r // 2), r)
    pygame.draw.polygon(surf, color, [(cx - 2 * r, cy - r // 2), (cx + 2 * r, cy - r // 2), (cx, cy + 2 * r)])


async def main(max_frames=None):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bhoot Escape")
    try:
        pygame.display.set_icon(pygame.image.load(resource(os.path.join("assets", "icon.png"))))
    except Exception:
        pass
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Comic Sans MS,Arial", 26)
    big = pygame.font.SysFont("Comic Sans MS,Arial", 44)

    background = load("scene.jpg", (WIDTH, HEIGHT))
    player_img = load("character.png", PLAYER)
    ghost_img = load("bhoot.png", PLAYER)

    def centre(text, fnt, colour, cy):
        img = fnt.render(text, True, colour)
        screen.blit(img, img.get_rect(center=(WIDTH // 2, cy)))

    def fresh():
        return {"ghosts": [Ghost(ghost_img) for _ in range(3)], "lane": 1,
                "score": 0, "lives": START_LIVES}

    state, game = ("playing", fresh()) if max_frames else ("start", fresh())
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE and state in ("start", "over"):
                    game, state = fresh(), "playing"
                elif state == "playing" and event.key in (pygame.K_LEFT, pygame.K_a):
                    game["lane"] = max(0, game["lane"] - 1)
                elif state == "playing" and event.key in (pygame.K_RIGHT, pygame.K_d):
                    game["lane"] = min(len(LANES) - 1, game["lane"] + 1)

        screen.blit(background, (0, 0))

        if state == "playing":
            speed = 4 + game["score"] // 10          # ramps up with score
            player = pygame.Rect(LANES[game["lane"]], HEIGHT - 90, *PLAYER)
            for ghost in game["ghosts"]:
                if ghost.fall(speed):
                    game["score"] += 1
                screen.blit(ghost.image, (ghost.x, int(ghost.y)))
                if ghost.rect().colliderect(player):
                    game["lives"] -= 1
                    ghost.spawn()
                    if game["lives"] <= 0:
                        state = "over"
            screen.blit(player_img, player)
            screen.blit(font.render(f"Score {game['score']}", True, GREEN), (16, 12))
            screen.blit(font.render("HP", True, RED), (WIDTH - 132, 12))
            for i in range(game["lives"]):
                draw_heart(screen, WIDTH - 86 + i * 28, 30, 22, RED)
        elif state == "start":
            centre("BHOOT ESCAPE", big, WHITE, HEIGHT // 2 - 60)
            centre("Dodge the falling ghosts", font, WHITE, HEIGHT // 2 - 6)
            centre("Move: A / D or arrows", font, GREEN, HEIGHT // 2 + 40)
            centre("Press SPACE to start", font, GREEN, HEIGHT // 2 + 74)
        else:  # over
            centre("GAME OVER", big, RED, HEIGHT // 2 - 50)
            centre(f"Score  {game['score']}", font, WHITE, HEIGHT // 2 + 6)
            centre("SPACE  play again", font, GREEN, HEIGHT // 2 + 54)

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)

        frame += 1
        if max_frames and frame >= max_frames:
            pygame.quit()
            return


if __name__ == "__main__":
    asyncio.run(main())
    