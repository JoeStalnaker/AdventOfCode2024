#dictionaries of games and results
#dictonary of games - key is game number value is a list of results
#dictionary of results - key is a color and value is a number
games = {}

def parseInput ( ):
  games = {}
  with open ( "input.txt" ) as f:
    for line in f:
      line = line.strip( )
      game = line.split( ":" )
      gameNum = game[0].split()[1]
      resultStrings = game[1].split( ";" )
      result = {"red":0,"green":0,"blue":0}
      results = []
      for resultString in resultStrings:
        colorStrings = resultString.split(",")
        for colorString in colorStrings:
          colorResult = colorString.split()
          result[colorResult[1]] = colorResult[0]
        newResult = result.copy()
        results.append(newResult)
      games[gameNum] = results
  return games

def findMinCubes ( results ):
  minCubes = {"red":0, "green":0, "blue":0}
  for result in results:
    keys = minCubes.keys()
    for key in keys:
      if result[key] > minCubes[key]:
        minCubes[key] = result[key]
  return minCubes

def getPower ( minCubes ):
  power = 1
  for key in minCubes.keys():
    power *= minCubes[key]
  return power

games = parseInput()
total = 0
keys = games.keys()
for key in keys:
  total += getPower(FindminCubes(games[key]))
print(total)
