import numpy as np

class Calculator:
    def process(self, data_frame):
        result = self._sum_numbers(data_frame)
        result = self._apply_transformations(result)
        return result

    def _sum_numbers(self, df):
        total = df.select_dtypes(include=[np.number]).sum().sum()
        return total

    def _apply_transformations(self, value):
        import math
        if value <= 0:
            return 0
        return math.log(value)
