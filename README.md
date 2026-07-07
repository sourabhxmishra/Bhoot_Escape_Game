# 👻 Bhoot Escape

A tiny **2D arcade game** built with **Python + pygame** — dodge the falling *bhoots* (ghosts) for as long as you can. Lightweight by design, so it runs smoothly on low-end hardware.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![pygame](https://img.shields.io/badge/pygame-000000?logo=python&logoColor=white)

## 🎮 How to play
- **← / →** (or **A / D**) — slide between the three lanes
- **SPACE** — start / restart
- **Esc / Q** — quit

Every ghost you dodge scores a point; a hit costs a life (you start with 3). The ghosts fall faster the longer you survive — how high can you score?

## 🚀 Run it
```bash
pip install -r requirements.txt      # pygame
python game.py
```

## 🧩 Under the hood
A fixed-timestep pygame loop with three `Ghost` sprites, real rectangle collision (`Rect.colliderect`), a difficulty ramp tied to score, and start / playing / game-over states. Art (`character.png`, `bhoot.png`, `scene.jpg`) is loaded relative to the script, so it runs from any directory.
