MAX_SEQUENCE = 5


class Stack:
    """
    Stack class
    """
    def __init__(self, player, rect_size):
        """
        Intialize stack
        String, Size --> Stack
        """
        self.content = []
        self.position = sorted([])
        self.sequence = [0 for i in range(4)]
        self.sequence_position = []
        self.player = player
        self.rect_size = rect_size
        self.three_sequence = False
        self.four_sequence = False

    def push(self, item):
        """
        Add item to the content
        tuple --> None
        """
        self.content.append(item)
        self.position.append((item.x, item.y))

    def decision_win(self):
        """
        Check whether there is 5 in a row sequence
        horizontally, vertically, and diagonally
        If there is True in any direction of sequence, return True
        None --> Boolean
        """
        result = []
        result.append(self.check_horizontally())
        result.append(self.check_vertically())
        result.append(self.check_diagonally_up())
        result.append(self.check_diagonally_down())
        if True in result:
            return True
        return False

    def check_horizontally(self):
        """
        Check sequence horizontally
        None --> Boolean
        """
        way = "hor"
        sequence = 0
        for i in self.position:
            for j in range(MAX_SEQUENCE):
                if (i[0] + self.rect_size * j, i[1]) in self.position:
                    sequence += 1
                    self.check_num_sequence(sequence, way, i, j)
                    if sequence == MAX_SEQUENCE:
                        return True
                else:
                    sequence = 0
            sequence = 0
        return False

    def check_vertically(self):
        """
        Check sequence vertically
        None --> Boolean
        """
        way = "ver"
        sequence = 0
        for i in self.position:
            for j in range(MAX_SEQUENCE):
                if (i[0], i[1] + self.rect_size * j) in self.position:
                    sequence += 1
                    self.check_num_sequence(sequence, way, i, j)
                    if sequence == MAX_SEQUENCE:
                        return True
                else:
                    sequence = 0
            sequence = 0
        return False

    def check_diagonally_up(self):
        """
        Check sequence diagonally(positive slope)
        None --> Boolean
        """
        way = "dia_po"
        sequence = 0
        for i in self.position:
            for j in range(MAX_SEQUENCE):
                if ((i[0] + self.rect_size * j,
                   i[1] - self.rect_size * j) in self.position):
                    sequence += 1
                    self.check_num_sequence(sequence, way, i, j)
                    if sequence == MAX_SEQUENCE:
                        return True
                else:
                    sequence = 0
            sequence = 0
        return False

    def check_diagonally_down(self):
        """
        Check sequence diagonally(negative slope)
        None --> Boolean
        """
        way = "dia_ne"
        sequence = 0
        for i in self.position:
            for j in range(MAX_SEQUENCE):
                if ((i[0] + self.rect_size * j,
                   i[1] + self.rect_size * j) in self.position):
                    sequence += 1
                    self.check_num_sequence(sequence, way, i, j)
                    if sequence == MAX_SEQUENCE:
                        return True
                else:
                    sequence = 0
            sequence = 0
        return False

    def check_num_sequence(self, sequence, way, i, j):
        """
        Check if there is three in a row sequence in any direction
        """
        if sequence > 1:
            self.sequence_position.append(self.position)
            if way == "hor":
                self.sequence[0] = "hor"
            elif way == "ver":
                self.sequence[1] = "ver"
            elif way == "dia_po":
                self.sequence[2] = "dia_po"
            elif way == "dia_ne":
                self.sequence[3] = "dia_ne"
            if sequence == 4:
                self.four_sequence = True
            if sequence == 3:
                self.three_sequence = True
