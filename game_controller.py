from spot import Spot
from stack import Stack
from ai import AI
import random

MAX_COLOR = 255
MIN_COLOR = 0


class GameController:
    """
    Game Controller class
    """
    def __init__(self, field, dot_position, stone_size, rect_size):
        """
        Initialize game controller
        (Number, Number), Set, Number, Number --> GameController
        """
        self.continue_game = True
        self.playing = True
        self.check_user_sequence = False
        self.check_computer_sequence = False
        self._pix_w = field[0]
        self._pix_h = field[1]
        self.dot_position = dot_position
        self.stone_size = stone_size
        self.count = 0
        self.to_draw_user = Stack("User", rect_size)
        self.to_draw_computer = Stack("Computer", rect_size)
        self.ai_move = AI(self.dot_position, rect_size)

    def update(self):
        """
        Displaying correct updating of placing stone in the dot_position
        If there is no more dot_position, stop playing
        If there is sequence in user or computer, stop playing
        None --> None
        """
        for spot in self.to_draw_user.content:
            spot.display()
        for spot in self.to_draw_computer.content:
            spot.display()
        if (len(self.dot_position) == 0 or
           self.check_user_sequence is True or
           self.check_computer_sequence is True):
            self.playing = False

    def end_text(self):
        """
        If game end, display that Game is over at the right format and position
        Display who win the game
        None --> None
        """
        FONT_SZIE = self._pix_w // 20     # 60
        VERT_MID = self._pix_w / 2        # 600
        HORIZ_MID = self._pix_h / 2       # 600

        textSize(FONT_SZIE)
        textAlign(CENTER)
        # Display in Green, Draw
        if len(self.dot_position) == 0:
            fill(MIN_COLOR, MAX_COLOR, MIN_COLOR)
            text("Game is over! Draw", HORIZ_MID, VERT_MID)
        # Display in Blue, User win
        elif(self.check_user_sequence is True):
            fill(MIN_COLOR, MIN_COLOR, MAX_COLOR)
            text("Game is over! Player win", HORIZ_MID, VERT_MID)
            self.save_name("Player")

        # Display in Red, Computer win
        elif(self.check_computer_sequence is True):
            fill(MAX_COLOR, MIN_COLOR, MIN_COLOR)
            text("Game is over! Computer win", HORIZ_MID, VERT_MID)
            self.save_name("Computer")
        self.continue_game = False

    def save_name(self, name):
        """
        Save who won the game
        if computer win, total win of computer will increase by 1
        if player win, total win of player will increase by 1
        """
        score_dict = dict()
        with open('scores.txt', 'r+') as f:
            for line in f.readlines():
                name_and_score = line.split()
                score_dict[name_and_score[0]] = name_and_score[1]

            # Very first game. No one ever won before, file is empty
            # Include who won the game and number of win
            if name not in score_dict:
                score_dict[name] = "1"
            else:
                score = int(score_dict[name])
                score_dict[name] = score + 1

            score_dict = sorted(score_dict.items(),
                                key=lambda x: str(x[1]),
                                reverse=True)
            f.truncate(0)
            f.close()

        with open('scores.txt', 'r+') as f:
            for i in score_dict:
                f.write(i[0] + " " + str(i[1]) + "\n")

    def user_put_stone(self, mouseX, mouseY):
        """
        If the mouse click is within the any dot_position of click_range range,
        put the stone in the close dot_position.
        Then remove that position from the dot_position.
        Check 5 in a row sequence for user
        If there isn't 5 in a row sequence for user, computer plays
        Number, Number --> None
        """
        BLACK = MIN_COLOR
        CLICK_RANGE = 10
        for i in range(mouseX-CLICK_RANGE, mouseX+CLICK_RANGE + 1):
            for j in range(mouseY-CLICK_RANGE, mouseY+CLICK_RANGE + 1):
                position = (i, j)
                if position in self.dot_position:
                    self.to_draw_user.push(Spot(i, j, BLACK, self.stone_size))
                    self.dot_position.remove((i, j))
                    # check sequence of user
                    self.check_user_sequence = self.to_draw_user.decision_win()
                    # Computers turn if player didn't win
                    if self.check_user_sequence is False:
                        self.check_computer_sequence = self.com_put_stone()

    def com_put_stone(self):
        """
        Computer put first stone randomly
        After second turn of computer, put the stone choosing the best position
        Check 5 in a row sequence for computer
        None --> None
        """
        self.count += 1
        com_pos = self.to_draw_computer.position
        user_pos = self.to_draw_user.position
        self.to_draw_computer.decision_win()
        direction = ["ver", "hor", "dia_po", "dia_ne"]
        # First computer play, put stone randomly nearby the first user stone
        if self.count == 1:
            available = self.ai_move.get_neighbor(user_pos,
                                                  user_pos)
            self.put_stone(available)
        # Second play, put stone near the first stone
        elif self.count == 2:
            available = self.ai_move.get_neighbor(com_pos,
                                                  user_pos)
            self.put_stone(available)
        # Pust stone choosing the best position
        # if user stone have a sequence of 3 then block the way of sequence
        else:
            # if there is 4 sequence for user,
            # put stone to block
            if self.to_draw_user.four_sequence is True:
                dir = self.to_draw_user.sequence
                for i in range(len(dir)):
                    if dir[i] in direction:
                        available = self.ai_move.get_neighbor(user_pos,
                                                              user_pos,
                                                              dir[i])

                        self.put_stone(available)
                        return self.to_draw_computer.decision_win()
            # if there is 4 sequence for computer,
            # must put stone to make 5 sequence
            elif self.to_draw_computer.four_sequence is True:
                dir = self.to_draw_computer.sequence
                for i in range(len(dir)):
                    if dir[i] in direction:
                        available = self.ai_move.get_neighbor(com_pos,
                                                              user_pos,
                                                              dir[i])
                        self.put_stone(available)
                        return self.to_draw_computer.decision_win()
            # if there is 3 sequence for user,
            # Put stone to block either way
            elif self.to_draw_user.three_sequence is True:
                dir = self.to_draw_user.sequence
                for i in range(len(dir)):
                    if dir[i] in direction:
                        available = self.ai_move.get_neighbor(user_pos,
                                                              user_pos,
                                                              dir[i])
                        self.put_stone(available)
                        return self.to_draw_computer.decision_win()
            # if there is 3 sequence for computer,
            # must put stone to make 4 sequence
            elif self.to_draw_computer.three_sequence is True:
                dir = self.to_draw_computer.sequence
                for i in range(len(dir)):
                    if dir[i] in direction:
                        available = self.ai_move.get_neighbor(com_pos,
                                                              user_pos,
                                                              dir[i])
                        self.put_stone(available)
                        return self.to_draw_computer.decision_win()
            # else put stone randomly next to the computer stone
            else:
                if any(elem in direction
                       for elem in self.to_draw_computer.sequence):
                    dir = self.to_draw_computer.sequence
                    for i in range(len(dir)):
                        if dir[i] in direction:
                            available = self.ai_move.get_neighbor(com_pos,
                                                                  user_pos)
                            self.put_stone(available)
                            return self.to_draw_computer.decision_win()
                else:
                    available = self.ai_move.get_neighbor(com_pos,
                                                          user_pos)
                    self.put_stone(available)
                    return self.to_draw_computer.decision_win()

    def put_stone(self, available):
        """
        Put the stone in available area
        """
        computer_stone = random.choice(available)
        self.to_draw_computer.push(Spot(computer_stone[0],
                                        computer_stone[1],
                                        MAX_COLOR, self.stone_size))
        self.dot_position.remove(computer_stone)
