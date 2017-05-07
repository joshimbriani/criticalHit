BOARD_WIDTH = 18
BOARD_HEIGHT = 24

class Board:

    def __init__(self):
        self.board = []
        for i in range(BOARD_HEIGHT):
            boardRow = []
            for j in range(BOARD_WIDTH):
                boardRow.append('C')
            self.board.append(boardRow)


