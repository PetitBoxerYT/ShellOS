import mpv

player = mpv.MPV(
    input_default_bindings=True,
    osc=False,
    ytdl=False
)

def play(path):
    player.play(path)

def pause():
    player.pause = not player.pause
