class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be non-negative")
        self._value = new_value

obj = MyClass(10)
obj.value = 20  # 正常赋值
print(obj.value)  # 输出: 20
# obj.value = -5  # 会报错: ValueError: Value must be non-negative
