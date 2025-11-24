import gc
import time
import tracemalloc
from dataclasses import dataclass
from core.constants import WARMUP_ITERATIONS


@dataclass
class AlgorithmMetrics:
    time: int
    memory: int
    operations: int
    iterations: int


class AlgorithmMetricsManager:
    _operations: int = 0
    _iterations: int = 0
    _start_time: int = 0
    _start_memory: int = 0
    _end_time: int = 0
    _end_memory: int = 0
    _original_gc_enabled: bool = False

    def warmup(self):
        for i in range(WARMUP_ITERATIONS):
            sum(range(i))

    def increment_operations(self, count: int = 1):
        self._operations += count

    def increment_iterations(self, count: int = 1):
        self._iterations += count

    def reset(self):
        self._operations = 0
        self._iterations = 0
        self._start_time = 0
        self._start_memory = 0
        self._end_time = 0
        self._end_memory = 0
        self._original_gc_enabled = False

    def start(self):
        self.reset()
        self.warmup()

        self._original_gc_enabled = gc.isenabled()
        gc.collect()

        if self._original_gc_enabled:
            gc.disable()

        tracemalloc.start()
        current, _ = tracemalloc.get_traced_memory()

        self._start_memory = current
        self._start_time = time.perf_counter_ns()

    def end(self):
        self._end_time = time.perf_counter_ns()

        _, peak = tracemalloc.get_traced_memory()
        self._end_memory = peak

        tracemalloc.stop()

        if self._original_gc_enabled:
            gc.enable()

    def get_metrics(self):
        return AlgorithmMetrics(
            operations=self._operations,
            iterations=self._iterations,
            time=self._end_time - self._start_time,
            memory=self._end_memory - self._start_memory
        )
