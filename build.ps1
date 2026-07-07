# Build BhootEscape.exe — a standalone Windows game (no Python needed to run).
# Prereqs (once):  py -3.12 -m venv .venv ; .\.venv\Scripts\Activate.ps1 ; pip install -r requirements.txt pyinstaller
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

python -m PyInstaller --noconfirm --clean --onefile --windowed `
  --name "BhootEscape" `
  --icon "assets/icon.ico" `
  --add-data "scene.jpg;." `
  --add-data "character.png;." `
  --add-data "bhoot.png;." `
  --add-data "assets/icon.png;assets" `
  game.py

Write-Host "`nBuilt: $(Join-Path $PSScriptRoot 'dist\BhootEscape.exe')" -ForegroundColor Green
