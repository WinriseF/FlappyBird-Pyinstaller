The original code is https://github.com/sourabhv/FlapPyBird

>Since the original code cannot be packaged directly through pyinstaller, there will be image missing problems, so we have changed the original code and can directly generate a complete exe file through pyinstaller after installing the necessary packages.

>You can generate an executable file directly through <pyinstaller --onefile --add-data "assets/sprites;assets/sprites" --add-data "assets/audio;assets/audio" main.py>

[FlapPyBird](https://sourabhv.github.io/FlapPyBird)
===============

A Flappy Bird Clone made using [python-pygame][pygame]

> If you are in interested in the old one-file code for the game, you can [find it here][one-file-game]

[pygame]: http://www.pygame.org
[one-file-game]: https://github.com/sourabhv/FlapPyBird/blob/038359dc6122f8d851e816ddb3e7d28229d585e5/flappy.py


Setup (as tested on MacOS)
---------------------------

1. Install Python 3 from [here](https://www.python.org/download/releases/) (or use brew/apt/pyenv)

2. Run `make init` (this will install pip packages, use virtualenv or something similar if you don't want to install globally)

3. Run `make` to run the game. Run `DEBUG=True make` to see rects and coords

4. Use <kbd>&uarr;</kbd> or <kbd>Space</kbd> key to play and <kbd>Esc</kbd> to close the game.

5. Optionally run `make web` to run the game in the browser (`pygbag`).

Notable forks
-------------
- [FlapPyBlink Blink to control the bird](https://github.com/sero583/FlappyBlink)
- [FlappyBird Fury Mode](https://github.com/Cc618/FlapPyBird)
- [FlappyBird Model Predictive Control](https://github.com/philzook58/FlapPyBird-MPC)
- [FlappyBird OpenFrameworks Port](https://github.com/TheLogicMaster/ofFlappyBird)
- [FlappyBird On Quantum Computing](https://github.com/WingCode/QuFlapPyBird)

Made something awesome from FlapPyBird? Add it to the list :)


Demo
----------

https://user-images.githubusercontent.com/2307626/130682424-9254b32d-efe0-406e-a6ea-3fb625a2df5e.mp4
