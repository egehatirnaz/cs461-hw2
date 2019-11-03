"""
	CS461 Fall 2019 Homework 2 
	Authors: Faruk Ege Hatırnaz
			 Shabnam Sadigova
			 Sıla İnci
			 Dilara Halavurt
			 Doğukan Aydın

	Date: 	 07.11.2019
"""


class States:
    def __init__(self, x, y, b, path):
        self.situation = str(x) + "M" + str(y) + "C" + str(b)
        self.x = x
        self.y = y
        self.b = b
        self.path = [[self.x, self.y, self.b]]
        for p in path:
            self.path.append(p)

    """
	def __init__(self, situation):
		self.x = situation[0:1]
		self.y = situation[2:3]
		self.b = situation[5:]
	"""

    def update_situation(self, x, y, b):
        self.path.append([self.x, self.y, self.b])
        self.x = x
        self.y = y
        self.b = b
        self.situation = x + "M" + y + "C" + b

    @staticmethod
    def is_safe(x, y):
        if x >= 0 and y >= 0 and (6 - x) >= 0 and (6 - y) >= 0:
            if x == 6:
                if x >= y:
                    return True
                else:
                    return False
            if x == 0:
                if (6 - x) >= (6 - y):
                    return True
                else:
                    print("x: ", x, " ; y: ", y)
                    return False
            if (6 - x) >= (6 - y) and x >= y:
                return True
            else:
                return False
        else:
            return False

    def get_current_state(self):
        return [self.x, self.y, self.b]

    def get_situation(self):
        return str(self.x) + "M" + str(self.y) + "C" + str(self.b)

    def get_path(self):
        return self.path

    def get_next_action(self):
        current_x = self.x
        current_y = self.y
        current_boat = self.b

        action_list = []
        for swimmer in range(1, 6):  # 1-5 people can use the boat.
            for m in range(0, self.x + 1):
                for c in range(0, self.y + 1):
                    if m + c == swimmer:
                        if current_boat == 1:  # crossing
                            if self.is_safe(current_x - m, current_y - c) and [current_x - m, current_y - c, 0] not in self.path:
                                # print("Swimmer: ", swimmer, "; mis: ", m, "; can: ", c)
                                action_list.append(
                                    [current_x - m, current_y - c, 0])
                        elif current_boat == 0:  # returning
                            if self.is_safe(current_x + m, current_y + c) and [current_x + m, current_y + c, 1] not in self.path:
                                # print("Swimmer: ", swimmer, "; mis: ", m, "; can: ", c)
                                action_list.append(
                                    [current_x + m, current_y + c, 1])
        return action_list


if __name__ == '__main__':
    s = States(6, 6, 1, [])
    print(s.get_next_action())

    s = States(4, 4, 0, [[6, 6, 1]])
    print(s.get_next_action())
    print(s.get_path())
