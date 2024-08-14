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
        popularity_points = {num: win_nums.count(num) for num in set(win_nums)}
        popularity_percentage = {key: value / sum(popularity_points.values()) * 100 for key, value in
                                 popularity_points.items()}
        return popularity_percentage

    @staticmethod
    def count_nums_stagnation(win_nums_box):
        stagnation_points = {}
        for run in win_nums_box:
            for num in run:
                if num not in stagnation_points.keys():
                    stagnation_points[num] = win_nums_box.index(run)
        stagnation_percentage = {key: value / sum(stagnation_points.values()) * 100 for key, value in
                                 stagnation_points.items()}
        return stagnation_percentage

    @staticmethod
    def count_nums_pairs(win_nums_box):
        pairs_points = {}
        for i in range(1, 21):
            for j in range(1, 21):
                if i != j and (j, i) not in pairs_points.keys():
                    pairs_points[(i, j)] = 0.0
        for key, value in pairs_points.items():
            for run in win_nums_box:
                if key[0] in run and key[1] in run:
                    pairs_points[key] += 1.0
        pairs_percentage = {key: value / (len(win_nums_box) * 6) * 100 for key, value in pairs_points.items()}
        return pairs_percentage

    @staticmethod
    def summary_nums_count(popularity, stagnation, pairs):
        summary = pairs.copy()
        for key, value in summary.items():
            summary[key] = (value + (popularity[key[0]] + popularity[key[1]]) / 2 + (
                    stagnation[key[0]] + stagnation[key[1]]) / 2) / 20
        return summary

    @staticmethod
    def organizer_for_pairs(summary):
        organizer_draft = {num: {} for num in range(1, 21)}
        for key, value in summary.items():
            organizer_draft[key[0]].update({key: value})
        organizer = {}
        keys_for_del = []
        for key, value in organizer_draft.items():
            for nums, val in value.items():
                if val == max(value.values()) and nums[0] not in keys_for_del and nums[1] not in keys_for_del:
                    organizer[nums] = val
                    keys_for_del.append(nums[0])
                    keys_for_del.append(nums[1])

        return organizer

    @staticmethod
    def clean_nums(organizer):
        clean_nums = []
        for row in organizer:
            if row[0][0] not in clean_nums and row[0][1] not in clean_nums:
                clean_nums.append(row[0][0])
                clean_nums.append(row[0][1])
        return clean_nums[:4]
