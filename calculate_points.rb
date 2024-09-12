require 'points_calculator'

lines = File.open('sbrr-2024-points.csv') { |f| f.readlines }
standings = []
lines.each do |line|
  standings << PointsCalculator.new(line)
end

standings.sort { |a, b| b.total_with_drops <=> a.total_with_drops }.each do |driver|
  puts driver.display
end
