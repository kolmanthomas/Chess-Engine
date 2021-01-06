import chess

class State(object):

    def __init__(self):
        self.board = chess.Board()

    def serialize(self):
        # 257 bits according to README
        pass

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # TODO: Add neural net here
        return 1

if __name__ == "__main__":
    s = State()
    print(s.edges())




