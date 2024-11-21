from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'{self.__class__.__name__}({self.color}) at position {self.position}'

class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        # Pěšák se pohybuje pouze vpřed (jinak podle barvy)
        if self.color == "white":
            if self.is_position_on_board((row + 1, col)):  # pohyb o jedno pole vpřed
                moves.append((row + 1, col))
            if row == 2 and self.is_position_on_board((row + 2, col)):  # první tah, o dvě pole
                moves.append((row + 2, col))
        elif self.color == "black":
            if self.is_position_on_board((row - 1, col)):  # pohyb o jedno pole vpřed
                moves.append((row - 1, col))
            if row == 7 and self.is_position_on_board((row - 2, col)):  # první tah, o dvě pole
                moves.append((row - 2, col))
        return moves

class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        # Pohyb střelce na všechny čtyři diagonály
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # směry diagonál
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if self.is_position_on_board((r, c)):
                    moves.append((r, c))
                else:
                    break
        return moves

class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        # Pohyb věže na všechny čtyři směry (horizontálně a vertikálně)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # směry vertikálně a horizontálně
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if self.is_position_on_board((r, c)):
                    moves.append((r, c))
                else:
                    break
        return moves

class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        # Pohyb dámy jako kombinace věže a střelce
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row, col
            while True:
                r += dr
                c += dc
                if self.is_position_on_board((r, c)):
                    moves.append((r, c))
                else:
                    break
        return moves

class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        # Král se pohybuje o jedno pole ve všech směrech
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if self.is_position_on_board((r, c)):
                moves.append((r, c))
        return moves
