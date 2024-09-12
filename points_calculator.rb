class PointsCalculator
  DROPS = 8
  RANDOM_EMPTY_COLUMNS = [8, 17]

  attr_reader :driver, :points

  def initialize(data)
    array = data.split(',')
    array.delete_at(RANDOM_EMPTY_COLUMNS[0])
    array.delete_at(RANDOM_EMPTY_COLUMNS[1] - 1)

    @driver = array[0]
    @points = array[3, array.length].map { |s| s.to_i }
  end

  def total
    points.sum
  end

  def total_with_drops
    sorted = points.sort.reverse
    best = sorted[0, sorted.length - DROPS]
    best.sum
  end

  def display
    "#{driver}\t Total: #{total}\tWith Drops: #{total_with_drops}"
  end
end
