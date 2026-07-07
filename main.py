"""Web entry point for Bhoot Escape (pygbag / WebAssembly build).

pygbag runs this file's ``asyncio.run(main())`` inside the browser event loop.
The actual game lives in ``game.py`` and is shared with the desktop build.

The explicit ``import pygame`` below is required: pygbag scans this entry file
to decide which packages to preload, so pygame must be imported here (not only
inside ``game.py``) or the browser build gets an empty pygame stub.
"""
import asyncio

import pygame  # noqa: F401  (ensures pygbag preloads the real pygame module)

from game import main

asyncio.run(main())
