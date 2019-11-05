import time


class Funnel:
    def __init__(self, capacity, leaking_rate):
        """
        :param capacity: 漏斗容量
        :param leaking_rate: 漏嘴流水速率
        """
        self.capacity = capacity  # 漏斗容量
        self.leaking_rate = leaking_rate  # 漏嘴流水速率
        self.left_quota = capacity  # 漏斗剩余空间
        self.leaking_time = time.time()  # 上一次漏水时间

    def make_space(self):
        now_time = time.time()
        delta_ts = now_time - self.leaking_time  # 距上次漏水时间
        delta_quota = delta_ts * self.leaking_rate  # 可以腾出多少空间
        if delta_quota < 1:
            return
        self.left_quota += delta_quota
        self.leaking_time = now_time
        if self.left_quota > self.capacity:
            self.left_quota = self.capacity

    def watering(self, quota):
        self.make_space()
        if quota <= self.left_quota:
            self.left_quota -= quota
            return True
        return False


funnels = {}

def is_action_allowed(user_id, action_key, capacity, leaking_rate):
    key = "%s:%s" % (str(user_id), str(action_key))
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] = funnel
    return funnel.watering(1)


if __name__ == '__main__':
    for _ in range(20):
        print(is_action_allowed("mumu", "read", 15, 0.5))

