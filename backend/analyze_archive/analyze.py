class AnalyzeNums:
    def __init__(self, clean_data):
        self.win_nums_boxes_a = []
        self.win_nums_boxes_b = []
        self.win_nums_a = []
        self.win_nums_b = []

        for run in clean_data:
            self.win_nums_boxes_a.append(run[3])
            for num in run[3]:
                self.win_nums_a.append(num)
            self.win_nums_boxes_b.append(run[4])
            for num in run[4]:
                self.win_nums_b.append(num)

    @staticmethod
    def count_nums_popularity(win_nums):
        popularity = {num: win_nums.count(num) for num in set(win_nums)}
        return popularity

    @staticmethod
    def count_nums_stagnation(win_nums_box):
        stagnation = {}
        for run in win_nums_box:
            for num in run:
                if num not in stagnation.keys():
                    stagnation[num] = win_nums_box.index(run)
        return stagnation
