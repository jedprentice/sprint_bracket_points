class PointsCalculator
  DROPS = 8
  RACES = 24
  RANDOM_EMPTY_COLUMNS = [8, 17]

  attr_reader :driver, :points, :sorted, :best

  def initialize(data)
    array = data.split(',')
    array.delete_at(RANDOM_EMPTY_COLUMNS[0])
    array.delete_at(RANDOM_EMPTY_COLUMNS[1] - 1)

    @driver = array[0]
    @points = array[3, RACES].map { |s| s.to_i }
  end

  def total
    points.sum
  end

  def total_with_drops
    @sorted = points.sort.reverse
    @best = sorted[0, sorted.length - DROPS]
    best.sum
  end

  def display
    "\n#{driver}\t Total: #{total}\tWith Drops: #{total_with_drops}\nPoints #{points}\nSorted #{sorted}\nBest #{best}"
  end
end
