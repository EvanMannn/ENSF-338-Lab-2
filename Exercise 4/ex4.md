Part 1:
The algorithm I would use to find the room is to check if my room is in between the room range on the left. 
Then tho only thing I can do after is check each door until I find the room.

Part 2:
It would take 15 steps to find the room assuming each "step" is checking one room number.

Part 3:
It is neither because you are not doing the maximum number of steps possible to find room 128

Part 4:
The best case scenario would either be getting to room 100 or to room 138 because you would find the door immediately. The worst case scenario is when you get room 130 where the layout and signage forces you to go 16 steps.

Part 5:
The way I would improve this algorithm is to remember that the middle room is 118 and have getting to room 118 be the maximum number of steps, essentially saying Rooms 100 - 118 are to the left and All Other Rooms are to the right
