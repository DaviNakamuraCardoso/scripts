cities = [
  "New York",
  "Paris",
  "Tallahassee",
  "Tokyo"
]

visited = [
  "New York",
  "Tokyo"
]

puts "Not visited: #{(cities - visited).join(", ")}"

