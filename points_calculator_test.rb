require 'points_calculator'
require 'test/unit'

class PointsCalculatorTest < Test::Unit::TestCase
  def test_calculate
    data = 'Jed Prentice,,1005,100,80,80,,,,,,,50,80,65,,,,50,40,40,80,80,100,80,80,,,,'
    points = [100, 80, 80, 0, 0, 0, 0, 0, 50, 80, 65, 0, 0, 0, 50, 40, 40, 80, 80, 100, 80, 80]
    calculator = PointsCalculator.new(data)
    assert_equal('Jed Prentice', calculator.driver, "Wrong driver")
    assert_equal(points, calculator.points)
    assert_equal(1005, calculator.total, 'Incorrect total')
    assert_equal(965, calculator.total_with_drops, 'Incorrect total with drops')
  end
end
