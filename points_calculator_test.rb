require 'points_calculator'
require 'test/unit'

class PointsCalculatorTest < Test::Unit::TestCase
  def test_calculate
    data = 'Jed Prentice,,1430,100,80,80,,,,100,75,80,75,100,100,,,,80,100,100,100,65,50,80,65,,,,,,,'
    points = [100, 80, 80, 0, 0, 100, 75, 80, 75, 100, 100, 0, 0, 80, 100, 100, 100, 65, 50, 80, 65]
    calculator = PointsCalculator.new(data)
    assert_equal('Jed Prentice', calculator.driver, "Wrong driver")
    assert_equal(points, calculator.points)
    assert_equal(1430, calculator.total, 'Incorrect total')
    assert_equal(1175, calculator.total_with_drops, 'Incorrect total with drops')
  end

  def test_calculate_another
    data = 'Christopher Graham,,1315,80,100,100,,,,,,,80,100,100,,,,100,100,80,100,100,100,100,75,,,,,,,'
    points = [80, 100, 100, 0, 0, 0, 0, 0, 80, 100, 100, 0, 0, 100, 100, 80, 100, 100, 100, 100, 75]
    calculator = PointsCalculator.new(data)
    assert_equal('Christopher Graham', calculator.driver, "Wrong driver")
    assert_equal(points, calculator.points)
    assert_equal(1315, calculator.total, 'Incorrect total')
    assert_equal(1240, calculator.total_with_drops, 'Incorrect total with drops')
  end

end
