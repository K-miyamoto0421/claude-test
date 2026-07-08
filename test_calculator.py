"""calculator.py に対するユニットテスト。"""

from typing import Any

import pytest

from calculator import add, calculate, divide, multiply, subtract


class TestAdd:
    """add 関数のテスト。"""

    def test_add_positive_numbers(self) -> None:
        """正の数の加算が正しく行われること。"""
        assert add(10, 5) == 15

    def test_add_negative_numbers(self) -> None:
        """負の数を含む加算が正しく行われること。"""
        assert add(-3, -7) == -10

    def test_add_float(self) -> None:
        """浮動小数点数の加算が正しく行われること。"""
        assert add(1.5, 2.5) == 4.0

    def test_add_invalid_type_raises_type_error(self) -> None:
        """数値以外を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            add("1", 2)  # type: ignore[arg-type]

    def test_add_invalid_type_both_args_raises_type_error(self) -> None:
        """両方の引数が数値以外の場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            add(None, [1, 2])  # type: ignore[arg-type]

    @pytest.mark.parametrize("invalid_value", ["1", None, [1], {1: 2}, True])
    def test_add_non_numeric_input_raises_type_error(self, invalid_value: Any) -> None:
        """文字列・None・リスト・辞書・bool を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            add(invalid_value, 1)  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            add(1, invalid_value)  # type: ignore[arg-type]


class TestSubtract:
    """subtract 関数のテスト。"""

    def test_subtract_basic(self) -> None:
        """基本的な減算が正しく行われること。"""
        assert subtract(10, 3) == 7

    def test_subtract_negative_result(self) -> None:
        """結果が負になる減算が正しく行われること。"""
        assert subtract(3, 10) == -7

    def test_subtract_invalid_type_raises_type_error(self) -> None:
        """数値以外を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            subtract(10, "3")  # type: ignore[arg-type]

    @pytest.mark.parametrize("invalid_value", ["1", None, [1], {1: 2}, True])
    def test_subtract_non_numeric_input_raises_type_error(self, invalid_value: Any) -> None:
        """文字列・None・リスト・辞書・bool を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            subtract(invalid_value, 1)  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            subtract(1, invalid_value)  # type: ignore[arg-type]


class TestMultiply:
    """multiply 関数のテスト。"""

    def test_multiply_basic(self) -> None:
        """基本的な乗算が正しく行われること。"""
        assert multiply(4, 7) == 28

    def test_multiply_by_zero(self) -> None:
        """ゼロとの乗算が0になること。"""
        assert multiply(5, 0) == 0

    def test_multiply_invalid_type_raises_type_error(self) -> None:
        """数値以外を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            multiply([1], 2)  # type: ignore[arg-type]

    @pytest.mark.parametrize("invalid_value", ["1", None, [1], {1: 2}, True])
    def test_multiply_non_numeric_input_raises_type_error(self, invalid_value: Any) -> None:
        """文字列・None・リスト・辞書・bool を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            multiply(invalid_value, 1)  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            multiply(1, invalid_value)  # type: ignore[arg-type]


class TestDivide:
    """divide 関数のテスト。"""

    def test_divide_basic(self) -> None:
        """基本的な除算が正しく行われること。"""
        assert divide(20, 4) == 5

    def test_divide_result_is_float(self) -> None:
        """割り切れない除算が正しく行われること。"""
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_value_error(self) -> None:
        """ゼロ除算で ValueError が発生すること。"""
        with pytest.raises(ValueError):
            divide(10, 0)

    def test_divide_invalid_type_raises_type_error(self) -> None:
        """数値以外を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            divide("10", 2)  # type: ignore[arg-type]

    @pytest.mark.parametrize("invalid_value", ["1", None, [1], {1: 2}, True])
    def test_divide_non_numeric_input_raises_type_error(self, invalid_value: Any) -> None:
        """文字列・None・リスト・辞書・bool を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            divide(invalid_value, 1)  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            divide(1, invalid_value)  # type: ignore[arg-type]


class TestCalculate:
    """calculate 関数のテスト。"""

    @pytest.mark.parametrize(
        "a,operator,b,expected",
        [
            (10, "+", 5, 15),
            (10, "-", 3, 7),
            (4, "*", 7, 28),
            (20, "/", 4, 5),
        ],
    )
    def test_calculate_basic_operations(
        self, a: Any, operator: str, b: Any, expected: Any
    ) -> None:
        """各演算子で正しい結果が返ること。"""
        assert calculate(a, operator, b) == expected

    def test_calculate_unknown_operator_raises_value_error(self) -> None:
        """未知の演算子を指定した場合に ValueError が発生すること。"""
        with pytest.raises(ValueError):
            calculate(1, "%", 2)

    def test_calculate_division_by_zero_raises_value_error(self) -> None:
        """演算子経由でもゼロ除算時に ValueError が発生すること。"""
        with pytest.raises(ValueError):
            calculate(1, "/", 0)

    def test_calculate_invalid_type_raises_type_error(self) -> None:
        """数値以外を渡した場合に TypeError が発生すること。"""
        with pytest.raises(TypeError):
            calculate("1", "+", 2)  # type: ignore[arg-type]
