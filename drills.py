#Creating a class for drills to be based off

class Drill:
    def __init__(self, drill_id, drill_name, drill_tags, drill_age, drill_description, drill_duration, drill_diagram):
        self.drill_id = int(drill_id)  #drill_id can only be an integer
        self.drill_name = drill_name
        self.drill_tags = drill_tags
        self.drill_age = drill_age
        self.drill_description = drill_description
        self.drill_duration = int(drill_duration)  #drill_duration can only be an integer
        self.drill_diagram = "drill_diagrams/"+drill_diagram+".png"

#Class to manage all drills and related functions
class Drill_manager:
    def __init__(self):
        d1 = Drill("0001", "Cincinnati Drill", "Shooting, Passing", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "1 passes to 2 who pivots and passes to 3 cutting to the basket for a shot or layup. 3 keeps going to the opposite outlet position, 2 rebounds, 1 replaces 2 and 2 outlets to 3. Encourage strong passing, cutting and finishing", "5", "Cincinnati")
        d2 = Drill("0002", "Star Drill", "Passing", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "One player is in each corner of the half court, or closer depending on team age/ability. Ball starts under the ring and is passed diagonally. The passer follows their pass moving to that spot. The drill continues with the ball being passed in the shape of a star, the final reciever completes a layup. Add jumpshots to extend drill", "5", "Star")
        d3 = Drill("0003", "3-Man Weave", "Passing, Offence", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Create 3 lines on the baseline with the ball starting in the middle. The first player passes ahead before running behind that person, the reciever then passes to the other player and runs behind them. The general rule, whoever you pass to you run behind. Once the ball reaches half court the last person runs back to play defence creating a 2v1", "6", "3-Man weave")
        d4 = Drill("0004", "1v1 Chase Drill", "Offence, Defence", "U8s, U10s, U12s, U14s, U16s, U18s, U20s","Offence starts above the wing whilst defence starts on the free throw line extended. Coach or teamate passes the ball to offence initiating the 1v1. Both players must run around their respective cone with defence aiming to get a stop and offence aiming to score", "5", "1 v 1 Chase")
        d5 = Drill("0005", "1v1 Lanes defence", "Offence, Defence", "U12s, U14s, U16s, U18s, U20s","In this drill offence should be going 50% whilst defence goes 100%. Defence must keep their arms out using their length and chest to slide and force offence to make a crossover. Offence should only cross when they reach the sideline or split line. Once at halfcourt the drill can be extended to a 1v1 to the opposite ring. This drill can be done in either a half-court or full-court", "10", "1 v 1 Lanes")
        d6 = Drill("0006", "5-Spot Shooting", "Shooting", "U12s, U14s, U16s, U18s, U20s", "Players must reach a certain number of made shots from each of the 5 spots on the court. To make it competitive split players into teams, making the winner the first to finish", "5", "5-Spot shooting")
        d7 = Drill("0007", "7-Up Shooting", "Shooting", "U12s, U14s, U16s, U18s, U20s", "Put players into pairs with one ball. One player is assigned the rebounder the other the shooter. Set a timer for 5 minutes, the shooter shoots from 3pt line, make or miss he move to mid range and shoots, make or miss he completes a layup, then returns to 3pt line. This process continues until the player reaches 7 points. 1 point is awared for a made layup, 2 for a mid-range and 3 for a 3. After 7 the player moves to the next spot. Continue untill all 5 spots are complete or until time is up.", "10", "7-Up")
        d8 = Drill("0008", "L-Cut Shooting Drill", "Shooting, Offence", "U10s, U12s, U14s, U16s, U18s, U20s", "Create two lines, one with balls one without. You decide where those two lines will be, an example is in the diagram. A player cuts in before returing out to the free-throw line, completing an L-cut. They recieve a pass and then either make a layup or shoot. Set a time and add a target, eg. 5 min, 10 layups, 10 free-throws, 5 3s", "10", "L-cut")
        d9 = Drill("0009", "Zig-Zag Dribbling", "Dribbling", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "This drill can be performed on a half-court or full-court. Players dribble with speed to each cone, performing a crossover the propelling themselves to the next cone. Ensure player practice different crossovers throughout the drill. Finish with a layup at the ring", "6", "Zig-zag")
        d10 = Drill("0010", "Dribble Knockout", "Dribbling", "U8s, U10s, U12s, U14s, U16s, U18s", "Create an imaginary boundary, I usually start with the free-throw line. Each player has a ball and must continue dribbling throughout the entire drill. Whilst dribbling players attempt to hit others ball out of the boundary whilst maintaining controll of their own ball. As more players get out shrink the boundary to make it harder", "5", "Dribble knockout")



        self.drills = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]