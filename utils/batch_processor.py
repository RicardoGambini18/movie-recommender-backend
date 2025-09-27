class BatchProcessor:
    _batch_size = 300

    @staticmethod
    def process(items: list[dict], callback: callable):
        for i in range(0, len(items), BatchProcessor._batch_size):
            batch = items[i:i + BatchProcessor._batch_size]
            batch_number = i // BatchProcessor._batch_size + 1
            batch_size = len(batch)
            callback(batch, batch_number, batch_size)
