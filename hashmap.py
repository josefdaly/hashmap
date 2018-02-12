class HashMap(object):

    def __init__(self):
        self._buckets = [[], [], [], []]
        self._number_of_elements = 0

    # def __unicode__(self):
    #     [] = set_list
    #     return

    def __len__(self):
        return self._number_of_elements

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.retrieve_value(key)

    def need_more_buckets(self):
        if self._number_of_elements >= len(self._buckets) / 2:
            return True
        return False

    def double_buckets_and_reorder_items(self):
        flat_item_list = [item for sublist in self._buckets for item in sublist]
        self._buckets = [[]] * (len(self._buckets) * 2)
        for key, val in flat_item_list:
            self.assign_value(key, val)

    def get_bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def assign_value(self, key, val):
        target_bucket = self.get_bucket_index(key)
        for items in self._buckets[target_bucket]:
            stored_key, stored_val = items
            if hash(stored_key) == hash(key):
                stored_val = val
                return 0 # NOTE: if just resetting val, don't increment
        self._buckets[target_bucket].append((key, val))
        return 1

    def retrieve_value(self, key):
        for stored_key, val in self._buckets[self.get_bucket_index(key)]:
            if hash(stored_key) == hash(key):
                return val
        raise ValueError('That key does not exist')

    def set(self, key, val):
        self._number_of_elements += self.assign_value(key, val)
        if self.need_more_buckets():
            self.double_buckets_and_reorder_items()

    def get(self, key, default=None):
        try:
            return self.retrieve_value(key)
        except ValueError:
            return default


if __name__ == '__main__':
    import ipdb; ipdb.set_trace() # for sandbox use
