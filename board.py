from piece import Piece, Rook, Pawn

class Board:
    def __init__(self):
        self.position = []
        for _ in range(8):
            col = []
            for _ in range (8):
                col.append(None)
            self.__position__.append(col)
        self.__position__[0][0] = Rook ("Black")
        self.__position__[0][7] = Rook ("Black")
        self.__position__[7][7] = Rook ("White")
        self.__position__[7][0] = Rook ("White")
    def get_piece(self, row, col):
        return self.__positions__[row][col]

