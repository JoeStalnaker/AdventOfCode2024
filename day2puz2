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

def isValidGame ( results, bagContents ) :
  valid = True
  for result in results:
    keys = result.keys()
    for key in keys:
      if int(result[key]) > int(bagContents[key]):
        valid = False
  return(valid)

games = parseInput()
bagContents = {"red":12, "green":13, "blue":14}
total = 0
keys = games.keys()
for key in keys:
  results = games[key]
  if isValidGame(results, bagContents):
    total += int(key)
print(total)
