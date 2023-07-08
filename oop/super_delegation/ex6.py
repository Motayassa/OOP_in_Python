class SoftList(list):
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj

    def __len__(self):
        return len(self.iter_obj)

    def __getitem__(self, item):
        if type(item) != int:
            return False
        if not - len(self) <= item <= len(self) - 1:
            return False

        return self.iter_obj[item]


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
