"""
https://www.pramp.com/challenge/BrLMj8M2dVUoY95A9x3X

up 1 mile: losses 1kWh
down 1 mile: gains 1kWh
sideways doesn't matter

find min energy needed for a drone to make the trip

input:  route = [ [0,   2, 10], (x,y,z)
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than `5` kWh and it’d end up with excess energy


Diagram: (spacing relative)
                            .
            .


                                    .

                                        
                    .
                .
            _ _ _ _ _ _ _ _ _ _ _ _

Always start at altitude you're given

start: 10
highest = 15

1. iterate through the array
2. look at z coordinate. try to update highest
3. return highest - start


Stats:
  O(n) time (where n is the # of coordinates given)
  O(1) space

Follow up: if you had to consider x,y, and z... ?
    use Euclidean distance = sqrt()
"""
def calc_drone_min_energy(route):
  Z_POSITION = 2
  
  #init vars
  starting_coord = route[0]
  start = starting_coord[Z_POSITION]
  highest = start

  for coord in route:
    z_height = coord[Z_POSITION]
    highest = max(highest, z_height)

  #calc the max energy needed
  return highest - start