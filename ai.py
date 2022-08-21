

class AI:
    """
    AI Class
    """
    def __init__(self, dot_position, rect_size):
        """
        Initialize AI
        List, Number --> AI
        """
        self.dot_position = dot_position
        self.rect_size = rect_size

    def get_neighbor(self, computer_position, user_position,
                     direction_way=None):
        """
        Get the availalble position from the neighbor for certain position
        List, List, String --> List
        """
        available_position = []
        for i in computer_position:
            if direction_way is None:
                dir = self.direction(i)
            else:
                if direction_way == "ver":
                    dir = [self.ver_up(i), self.ver_down(i)]
                elif direction_way == "hor":
                    dir = [self.hor_left(i), self.hor_right(i)]
                elif direction_way == "dia_po":
                    dir = [self.diag_down_left(i), self.diag_up_right(i)]
                elif direction_way == "dia_ne":
                    dir = [self.diag_up_left(i), self.diag_down_right(i)]
            for j in range(len(dir)):
                if dir[j] in self.dot_position:
                    if dir[j] not in available_position:
                        available_position.append(dir[j])
        # Remove the repeated position
        for j in user_position:
            if j in available_position:
                available_position.remove(j)
        for k in computer_position:
            if k in available_position:
                available_position.remove(k)

        return sorted(available_position)

    def direction(self, current_pos):
        """ All the position for each direction to the current position"""
        return [self.hor_right(current_pos),
                self.hor_left(current_pos),
                self.ver_up(current_pos),
                self.ver_down(current_pos),
                self.diag_up_right(current_pos),
                self.diag_up_left(current_pos),
                self.diag_down_right(current_pos),
                self.diag_down_left(current_pos)]

    def hor_right(self, current_pos):
        """horizontal right position"""
        return (current_pos[0] + self.rect_size, current_pos[1])

    def hor_left(self, current_pos):
        """horizontal right position"""
        return (current_pos[0] - self.rect_size, current_pos[1])

    def ver_up(self, current_pos):
        """vertical up position"""
        return (current_pos[0], current_pos[1] - self.rect_size)

    def ver_down(self, current_pos):
        """vertical down position"""
        return (current_pos[0], current_pos[1] + self.rect_size)

    def diag_up_right(self, current_pos):
        """diagonal up right position"""
        return (current_pos[0] + self.rect_size,
                current_pos[1] - self.rect_size)

    def diag_up_left(self, current_pos):
        """diagonal up left position"""
        return (current_pos[0] - self.rect_size,
                current_pos[1] - self.rect_size)

    def diag_down_right(self, current_pos):
        """diagonal down right position"""
        return (current_pos[0] + self.rect_size,
                current_pos[1] + self.rect_size)

    def diag_down_left(self, current_pos):
        """diagonal down left position"""
        return (current_pos[0] - self.rect_size,
                current_pos[1] + self.rect_size)
