class AnalyzeNums:
    def __init__(self):
        self.win_nums_boxes_a = []
        self.win_nums_boxes_b = []
        self.win_nums_a = []
        self.win_nums_b = []
        self.nums_variety_a = 0
        self.nums_variety_b = 0

    def filling_vars(self, clean_data):
        for run in clean_data:
            self.win_nums_boxes_a.append(run[3])
            for num in run[3]:
                self.win_nums_a.append(num)
            self.win_nums_boxes_b.append(run[4])
            for num in run[4]:
                self.win_nums_b.append(num)
        self.nums_variety_a = len(set(self.win_nums_a))
        self.nums_variety_b = len(set(self.win_nums_b))

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
    def count_nums_pairs(win_nums_box, nums_variety):
        pairs_points = {}
        for i in range(1, nums_variety + 1):
            for j in range(1, nums_variety + 1):
                if i != j and (j, i) not in pairs_points.keys():
                    pairs_points[(i, j)] = 0.0
        for key, value in pairs_points.items():
            for run in win_nums_box:
                if key[0] in run and key[1] in run:
                    pairs_points[key] += 1.0
        pairs_percentage = {key: value / (len(win_nums_box) * 6) * 100 for key, value in pairs_points.items()}
        return pairs_percentage

    @staticmethod
    def summary_nums_count(popularity, stagnation, pairs, nums_variety):
        summary = pairs.copy()
        for key, value in summary.items():
            summary[key] = (value + (popularity[key[0]] + popularity[key[1]]) / 2 + (
                    stagnation[key[0]] + stagnation[key[1]]) / 2) / nums_variety
        return summary

    @staticmethod
    def organizer_for_pairs(summary, nums_variety):
        organizer_draft = {num: {} for num in range(1, nums_variety + 1)}
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
    def sort_organizer(organizer):
        organizer_sorted = sorted(organizer.items(), key=lambda x: x[1], reverse=True)
        return organizer_sorted

    @staticmethod
    def clean_nums(organizer):
        clean_nums = []
        for row in organizer:
            if row[0][0] not in clean_nums and row[0][1] not in clean_nums:
                clean_nums.append(row[0][0])
                clean_nums.append(row[0][1])
        return clean_nums[:4]

    @classmethod
    def analyze_nums(cls, clean_data):
        analysis = AnalyzeNums()
        cls.filling_vars(analysis, clean_data)

        nums_variety_a = analysis.nums_variety_a
        nums_variety_b = analysis.nums_variety_b

        popularity_a = cls.count_nums_popularity(analysis.win_nums_a)
        popularity_b = cls.count_nums_popularity(analysis.win_nums_b)

        stagnation_a = cls.count_nums_stagnation(analysis.win_nums_boxes_a)
        stagnation_b = cls.count_nums_stagnation(analysis.win_nums_boxes_b)

        pairs_a = cls.count_nums_pairs(analysis.win_nums_boxes_a, nums_variety_a)
        pairs_b = cls.count_nums_pairs(analysis.win_nums_boxes_b, nums_variety_b)

        summary_a = cls.summary_nums_count(popularity_a, stagnation_a, pairs_a, nums_variety_a)
        summary_b = cls.summary_nums_count(popularity_b, stagnation_b, pairs_b, nums_variety_b)

        organizer_a = cls.organizer_for_pairs(summary_a, nums_variety_a)
        organizer_b = cls.organizer_for_pairs(summary_b, nums_variety_b)

        sorted_organizer_a = cls.sort_organizer(organizer_a)
        sorted_organizer_b = cls.sort_organizer(organizer_b)

        clean_nums_a = cls.clean_nums(sorted_organizer_a)
        clean_nums_b = cls.clean_nums(sorted_organizer_b)

        return clean_nums_a, clean_nums_b
