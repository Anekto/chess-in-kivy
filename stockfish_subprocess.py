
import subprocess, time


class StockFish():

    def __init__(self) -> None:
        
        self.engine = subprocess.Popen(
        "stockfish\stockfish-windows-x86-64-avx2.exe",
        universal_newlines=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        bufsize=1,
    )

    def put(self, command):
        print('\nyou:\n\t'+ command)
        self.engine.stdin.write(command +'\n')
        
    def get(self):
        # using the 'isready' command (engine has to answer 'readyok')
        # to indicate current last line of stdout
        self.engine.stdin.write('isready\n')
        print('\nengine:')
        while True:
            text = self.engine.stdout.readline().strip()
            if text == 'readyok':
                break
            if text !='' or text.startswith("bestmove"):

                if text.startswith("bestmove"):
                    

                    print('\t' + text)
                    return text

                print('\t'+text)
        return ""

#new_fish = StockFish()

"""
new_fish.get()
new_fish.put('uci')
new_fish.get()
new_fish.put("position fen RNBKQBNR/PPPP1PPP/8/4P3/8/8/pppppppp/rnbkqbnr/")
new_fish.get()
new_fish.put('go depth 1')
new_fish.get()
new_fish.get()

"""
