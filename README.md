# 👻 Bhoot Escape

A tiny **2D arcade game** built with **Python + pygame** — dodge the falling *bhoots* (ghosts) for as long as you can. Lightweight by design, so it runs smoothly on low-end hardware.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![pygame](https://img.shields.io/badge/pygame-000000?logo=python&logoColor=white)
[![Download](https://img.shields.io/badge/%E2%AC%87_Download-Windows_.exe-7C3AED)](https://github.com/sourabhxmishra/Bhoot_Escape_Game/releases/latest)

## ⬇️ Download & play (Windows)
Grab **`BhootEscape.exe`** from the **[latest release](https://github.com/sourabhxmishra/Bhoot_Escape_Game/releases/latest)** and double-click it — no Python required. It's a single ~14 MB file with its own ghost app icon.

## 🎮 How to play
- **← / →** (or **A / D**) — slide between the three lanes
- **SPACE** — start / restart
- **Esc / Q** — quit

Every ghost you dodge scores a point; a hit costs a life (you start with 3). The ghosts fall faster the longer you survive — how high can you score?

## 🚀 Run from source
```bash
pip install -r requirements.txt      # pygame
python game.py
```

## 📦 Build the .exe yourself
```powershell
py -3.12 -m venv .venv ; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt pyinstaller
.\build.ps1          # → dist\BhootEscape.exe (icon + assets bundled)
```

## 🧩 Under the hood
A fixed-timestep pygame loop with three `Ghost` sprites, real rectangle collision (`Rect.colliderect`), a difficulty ramp tied to score, and start / playing / game-over states. Art (`character.png`, `bhoot.png`, `scene.jpg`) resolves through a `resource()` helper, so it works both from source and inside the packaged app.
