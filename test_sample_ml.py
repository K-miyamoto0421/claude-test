"""sample_ml.py に対するユニットテスト。"""

import math

import pytest

from sample_ml import (
    covariance,
    linear_regression,
    mean,
    predict,
    r_squared,
    rmse,
    variance,
)


class TestMean:
    """mean 関数のテスト。"""

    def test_mean_basic(self) -> None:
        """既知のデータで正しい平均値が返ること。"""
        assert mean([1, 2, 3, 4, 5]) == 3.0

    def test_mean_single_value(self) -> None:
        """要素が1件の場合にその値自身が返ること。"""
        assert mean([10]) == 10.0

    def test_mean_empty_raises_value_error(self) -> None:
        """空リストの場合に ValueError が発生すること。"""
        with pytest.raises(ValueError):
            mean([])


class TestVariance:
    """variance 関数のテスト。"""

    def test_variance_basic(self) -> None:
        """既知のデータで正しい分散値が返ること。"""
        # [2, 4, 4, 4, 5, 5, 7, 9] の母分散は 4.0
        values = [2, 4, 4, 4, 5, 5, 7, 9]
        assert variance(values) == pytest.approx(4.0)

    def test_variance_constant_values_is_zero(self) -> None:
        """全て同じ値の場合に分散が0になること。"""
        assert variance([5, 5, 5, 5]) == 0.0

    def test_variance_empty_raises_value_error(self) -> None:
        """空リストの場合に ValueError が発生すること（mean 経由）。"""
        with pytest.raises(ValueError):
            variance([])


class TestCovariance:
    """covariance 関数のテスト。"""

    def test_covariance_basic(self) -> None:
        """既知のデータで正しい共分散値が返ること。"""
        x = [1, 2, 3]
        y = [2, 4, 6]
        assert covariance(x, y) == pytest.approx(4 / 3)

    def test_covariance_mismatched_length_raises_value_error(self) -> None:
        """x と y の長さが異なる場合に ValueError が発生すること。"""
        with pytest.raises(ValueError):
            covariance([1, 2, 3], [1, 2])


class TestLinearRegression:
    """linear_regression 関数のテスト。"""

    def test_linear_regression_perfect_line(self) -> None:
        """y = 2x の完全な直線データで正しい傾き・切片が得られること。"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        slope, intercept = linear_regression(x, y)
        assert slope == pytest.approx(2.0)
        assert intercept == pytest.approx(0.0)

    def test_linear_regression_with_intercept(self) -> None:
        """y = 3x + 1 のデータで正しい傾き・切片が得られること。"""
        x = [0, 1, 2, 3]
        y = [1, 4, 7, 10]
        slope, intercept = linear_regression(x, y)
        assert slope == pytest.approx(3.0)
        assert intercept == pytest.approx(1.0)

    def test_linear_regression_empty_raises_value_error(self) -> None:
        """空リストの場合に ValueError が発生すること。"""
        with pytest.raises(ValueError):
            linear_regression([], [])

    def test_linear_regression_single_point_raises_value_error(self) -> None:
        """データ点が1件の場合に ValueError が発生すること（分散が0になるため）。"""
        with pytest.raises(ValueError):
            linear_regression([1], [5])

    def test_linear_regression_mismatched_length_raises_value_error(self) -> None:
        """x と y の長さが異なる場合に ValueError が発生すること。"""
        with pytest.raises(ValueError):
            linear_regression([1, 2, 3], [1, 2])

    def test_linear_regression_identical_x_raises_value_error(self) -> None:
        """x が全て同一値の場合に ValueError が発生すること。"""
        with pytest.raises(ValueError):
            linear_regression([2, 2, 2], [1, 2, 3])


class TestPredict:
    """predict 関数のテスト。"""

    def test_predict_basic(self) -> None:
        """傾きと切片から正しい予測値が計算されること。"""
        assert predict(4, slope=2.0, intercept=1.0) == pytest.approx(9.0)

    def test_predict_zero_slope(self) -> None:
        """傾きが0の場合は切片がそのまま返ること。"""
        assert predict(100, slope=0.0, intercept=5.0) == pytest.approx(5.0)


class TestRSquared:
    """r_squared 関数のテスト。"""

    def test_r_squared_perfect_fit(self) -> None:
        """完全な直線データではR²が1.0になること。"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        slope, intercept = linear_regression(x, y)
        assert r_squared(x, y, slope, intercept) == pytest.approx(1.0)

    def test_r_squared_constant_y_returns_one(self) -> None:
        """y が全て同一値の場合にR²が1.0になること。"""
        x = [1, 2, 3]
        y = [5, 5, 5]
        assert r_squared(x, y, slope=0.0, intercept=5.0) == 1.0


class TestRmse:
    """rmse 関数のテスト。"""

    def test_rmse_perfect_fit_is_zero(self) -> None:
        """完全な直線データではRMSEが0になること。"""
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        slope, intercept = linear_regression(x, y)
        assert rmse(x, y, slope, intercept) == pytest.approx(0.0, abs=1e-9)

    def test_rmse_known_value(self) -> None:
        """既知の誤差データで正しいRMSEが計算されること。"""
        x = [1, 2]
        y = [1, 2]
        # slope=0, intercept=0 -> predictions are [0, 0], errors are [1, 4]
        result = rmse(x, y, slope=0.0, intercept=0.0)
        assert result == pytest.approx(math.sqrt(2.5))
