import xml.etree.ElementTree as ET
from tkinter import messagebox

#Class for drills to be based off
class Drill:
    def __init__(self, drill_id, drill_name, drill_tags, drill_age, drill_description, drill_duration, drill_diagram):
        self.drill_id = int(drill_id)  #drill_id can only be an integer
        self.drill_name = drill_name
        self.drill_tags = [tag.strip() for tag in drill_tags.split(",")]  #turns values into list at each comma
        self.drill_age = [age.strip() for age in drill_age.split(",")]
        self.drill_description = drill_description
        self.drill_duration = int(drill_duration)  #drill_duration can only be an integer
        self.drill_diagram = "drill_diagrams/"+drill_diagram+".png"

#Class to manage all drills and related functions
class Drill_manager:
    def __init__(self):

        #Function to save drills onto xml file
        def save_to_xml(self, filepath):
            pass
            root = ET.Element("drills")
            for drill in self.drills:
                drill_elem = ET.SubElement(root, "drill")

                ET.SubElement(drill_elem, "drill_id").text = drill.drill_id
                ET.SubElement(drill_elem, "drill_name").text = drill.drill_name
                ET.SubElement(drill_elem, "drill_tags").text = ",".join(drill.drill_tags) #Returns list to just be string
                ET.SubElement(drill_elem, "drill_age").text = drill.drill_age
                ET.SubElement(drill_elem, "drill_description").text = drill.drill_description
                ET.SubElement(drill_elem, "drill_duration").text = drill.drill_duration
                ET.SubElement(drill_elem, "drill_diagram").text = drill.drill_diagram
            
            tree = ET.ElementTree(root)
            tree.write(filepath, encoding="utf-8", xml_declaration=True)

        #Function to load drills from xml file onto software
        def load_from_xml(self, filepath):
            pass
            try:
                tree = ET.parse(filepath)
                root = tree.getroot()
                #Loops through each drill element 
                for drill_elem in root.findall("drill"):
                    drill_id = drill_elem.find("drill_id").text
                    drill_name = drill_elem.find("drill_name").text
                    drill_tags = (drill_elem.find("drill_tags").text).split(",")
                    drill_age = drill_elem.find("drill_age").text
                    drill_description = drill_elem.find("drill_description").text
                    drill_duration = drill_elem.find("drill_duration").text
                    drill_diagram = drill_elem.find("drill_diagram").text
                    #Create drill and add it to the list of drills
                    drill = Drill(drill_id, drill_name, drill_tags, drill_age, drill_description, drill_duration, drill_diagram)
                    self.drills.append(drill)
            except FileNotFoundError:
                messagebox.showerror("Error", "Drills xml file could not be found")



        d1 = Drill("0001", "Cincinnati Drill", "Shooting, Passing", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "1 passes to 2 who pivots and passes to 3 cutting to the basket for a shot or layup. 3 keeps going to the opposite outlet position, 2 rebounds, 1 replaces 2 and 2 outlets to 3. Encourage strong passing, cutting and finishing", "5", "Cincinnati")
        d2 = Drill("0002", "Star Drill", "Passing", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "One player is in each corner of the half court, or closer depending on team age/ability. Ball starts under the ring and is passed diagonally. The passer follows their pass moving to that spot. The drill continues with the ball being passed in the shape of a star, the final reciever completes a layup. Add jumpshots to extend drill", "5", "Star")
        d3 = Drill("0003", "3-Man Weave", "Passing, Offence", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Create 3 lines on the baseline with the ball starting in the middle. The first player passes ahead before running behind that person, the reciever then passes to the other player and runs behind them. The general rule, whoever you pass to you run behind. Once the ball reaches half court the last person runs back to play defence creating a 2v1", "6", "3-Man weave")
        d4 = Drill("0004", "1v1 Chase Drill", "Offence, Defence", "U8s, U10s, U12s, U14s, U16s, U18s, U20s","Offence starts above the wing whilst defence starts on the free throw line extended. Coach or teamate passes the ball to offence initiating the 1v1. Both players must run around their respective cone with defence aiming to get a stop and offence aiming to score", "5", "1 v 1 Chase")
        d5 = Drill("0005", "1v1 Lanes defence", "Offence, Defence", "U12s, U14s, U16s, U18s, U20s","In this drill offence should be going 50% whilst defence goes 100%. Defence must keep their arms out using their length and chest to slide and force offence to make a crossover. Offence should only cross when they reach the sideline or split line. Once at halfcourt the drill can be extended to a 1v1 to the opposite ring. This drill can be done in either a half-court or full-court", "10", "1 v 1 Lanes")
        d6 = Drill("0006", "5-Spot Shooting", "Shooting", "U12s, U14s, U16s, U18s, U20s", "Players must reach a certain number of made shots from each of the 5 spots on the court. To make it competitive split players into teams, making the winner the first to finish", "5", "5-Spot shooting")
        d7 = Drill("0007", "7-Up Shooting", "Shooting", "U12s, U14s, U16s, U18s, U20s", "Pair players up with one ball. One player is assigned the rebounder the other the shooter. Set a timer for 5 minutes, the shooter shoots from 3pt line, make or miss they move to mid range and shoot, make or miss they complete a layup. This process continues until the player reaches 7 points. 1 point for a layup, 2 for a mid-range and 3 for a 3. After 7 the player moves to the next spot, aiming to complete all 5 before time ends", "10", "7-Up")
        d8 = Drill("0008", "L-Cut Shooting Drill", "Shooting, Offence", "U10s, U12s, U14s, U16s, U18s, U20s", "Create two lines, one with balls one without. You decide where those two lines will be, an example is in the diagram. A player cuts in before returing out to the free-throw line, completing an L-cut. They recieve a pass and then either make a layup or shoot. Set a time and add a target, eg. 5 min, 10 layups, 10 free-throws, 5 3s", "10", "L-cut")
        d9 = Drill("0009", "Zig-Zag Dribbling", "Dribbling, offence", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "This drill can be performed on a half-court or full-court. Players dribble with speed to each cone, performing a crossover the propelling themselves to the next cone. Ensure player practice different crossovers throughout the drill. Finish with a layup at the ring", "6", "Zig-zag")
        d10 = Drill("0010", "Dribble Knockout", "Dribbling", "U8s, U10s, U12s, U14s, U16s, U18s", "Create an imaginary boundary, I usually start with the free-throw line. Each player has a ball and must continue dribbling throughout the entire drill. Whilst dribbling players attempt to hit others ball out of the boundary whilst maintaining controll of their own ball. As more players get out shrink the boundary to make it harder", "5", "Dribble knockout")
        d11 = Drill("0011", "Square Passing", "Passing", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Create 3 lines on the baseline and 1 line on the sideline. The ball is passed to the adjacent line, the passer then sprints to the opposite spot, the ball continues around the half-court until it reaches the start, forming a square", "3", "Square")
        d12 = Drill("0012", "2v1 Drill","Offence, Defence", "U10s, U12s, U14s, U16s, U18s, U20s", "Create 3 lines along the baseline. The middle line is defence whilst the outside lines are offence. All players must run around their cone before playing a 2v1. Offence should identify scoring and passing lanes. Add restrictions to challenge players", "10", "2 v 1")
        d13 = Drill("0013", "Shell Drill", "Defence, Offence", "U12s, U14s, U16s, U18s, U20s", "Split players into two teams. Defence evenly spaces out on the baseline, offence on the three point line. The ball is passed to each player on the basline, each passer then sprints diagonally opposite to their player on the 3pt line. The ball is passed around the 3 pt line, with defence moving to appropriate spots. At the last player the game becomes live", "15", "Shell")
        d14 = Drill("0014", "2v2 Drill", "Offence, Defence", "U10s, U12s, U14s, U16s, U18s, U20s", "Defence starts below the 3 pt line opposite their player. The ball is passed to the wing initiating the 2v2 with the passer encourage to set a screen, ghost screen or dribble handoff, add rules to enforce concepts", "10", "2 v 2")
        d15 = Drill("0015", "Pop-Outs", "Shooting", "U10s, U12s, U14s, U16s, U18s, U20s", "Create two lines, with one ball each, on the lane lines. The first player runs around the key recieveing the ball and completing a layup, the passer then does the same. This process is done untill 20 layups, 15 block shots, 10 elbow shots and 5 3s have been made", "7", "Pop-outs")
        d16 = Drill("0016", "Team Rebounding Drill", "Rebounding, Offence, Defence", "U10s, U12s, U14s, U16s, U18s, U20s", "Split players into two teams, defence starts in the key, offence on the 3pt line. Coach shoots the ball and players sprint to box-out opponents and rebound the ball. The extend drill have offence aim to score if they get an o-board", "10", "Team rebounding")
        d17 = Drill("0017", "Competitive Rebounding Drill","Rebounding, Offence, Defence", "U12s, U14s, U16s, U18s, U20s", "Split players into two teams. Defence lines up in the key whilst offence space around the 3pt line. Coach passes to one of the offensive players who shoot. Defence sprints to box-out whislt offence attempt to get an o-board and score.", "10", "Competitive rebounding")
        d18 = Drill("0018", "1v1 Rebounding", "Rebounding", "U10s, U12s, U14s, U16s, U18s, U20s", "Assign one player, or coach as shooter. Two players are positioned in the key, they need to box each other out attemtping to get the rebound. Keep scores to ensure effort, 1 pt for a successful rebound.", "5", "1 v 1 Rebound")
        d19 = Drill("0019", "4v4 Rebounding", "Rebounding, Offence, Defence", "U12s, U14s, U16s, U18s, U20s", "One offensive player is place on each block and elbow, defence is placed within the key, standing next to their player. Defence must rotate to each offensive player until coach shoots, when the must box-out and obtain the rebound. Encourage teams to put shots back up attempting to score", "10", "4 v 4 Rebound")
        d20 = Drill("0020", "Russian Layups", "Passing, Shooting, Offence", "U12s, U14s, U16s, U18s, U20s", "Create one line on each baseline. This drill can be performed with coaches on the elbows or players rotating on the elbows. The elbow passer passes to the player running ahead, after recieving they pass to the other person on the elbow before recieving the ball back for a layup. Set a time and encourage speed", "5", "Russian")
        d21 = Drill("0021", "Driving Contact Drill", "Offence, Shooting", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Players drive towards the basket taking contact giving by coach, using a bump pad, and finishing. Expand the drill by adding spots to complete dribble moves and encouraging shots", "10", "driving contact")
        d22 = Drill("0022", "Collision Dribbling", "Dribbling, Offence", "U10s, U12s, U14s, U16s, U18s, U20s", "Create a line in each of the four corners, each player should have a basketball. On coaches whistle or go the first four players dribble with speed, when the meet in the middle the perform a crossover and continue to the diagonally opposite corner. Expand by changing type and amount of crossovers", "5", "Collision")
        d23 = Drill("0023", "Number Game", "Offence, Defence", "U8s, U10s, U12s, U14s", "Split players into two teams and line them on the baseline, assigning each a different number. When coach call out a players number they sprint to get the ball and score, the opposition number then has to try and stop them. Extend the drill by making it a 2v2, 3v3 etc.", "10", "Number")
        d24 = Drill("0024", "3-Spot-3-min Shooting Drill", "Shooting", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Create 3 lines, one on each elbow and one in the middle of the free throw line. Set a timer for 3 minutes. Players shoot from the designated spots rebounding their own ball back to the line they just shot at. Don't forget to rotate lines. Set a resonable target based on skill of team", "4", "3-spot")
        d25 = Drill("0025", "Defensive Footwork Drill", "Defence", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Set cones up as per diagram. Players sprint to the first cone closing-out with a high hand. They then backpedal to the next cone before defensivly slideing to the next. Players then sprint to closeout at the next cone before sliding again. Add more cones or more footwork, eg. crossover step to expand the drill.", "5", "footwork")
        d26 = Drill("0026", "Quick Decision Finishing Drill", "Offence, Defence, Passing, Shooting", "U10s, U12s, U14s, U16s, U18s, U20s", "Two offensive players begin on the block with one defence in the middle. Coach passes to either of the offensive players who need to quickly decide whether they shoot or pass. However there is a limit to only one pass. Therefore players must decide in a split seconde what the best option would be. No dribbling or steps are allowed", "5", "Quick decision")
        d27 = Drill("0027", "Finishing off Dribble Drill", "Dribbling, Shooting, Offence", "U10s, U12s, U14s, U16s, U18s, U20s","Set up cones in a diamond shape with one cone just above the charge-circle. Players perform a different dribble move at each cone, before finsing at the ring. As coach you add or change dribble move ie. spin move, step-through, euro, etc. Extend the drill by making players shoot instead of making a layup", "10", "Finishing off dribble")
        d28 = Drill("0028", "Rebound & Outlet Drill", "Rebounding, Offence, Passing", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Separate players into lines, one on each wing and one on each elbow. Start with two players under the ring ready to get rebounds. The first player on each elbow shoots, the rebounders get the ball, rip, then make an outlet pass to their respective wing. The wing passes to the middle who then repeats the process again. Players follow their pass/shot, joining that line", "5", "Rebound outlet")
        d29 = Drill("0029", "Rebound Relay Drill","Rebounding", "U12s, U14s, U16s, U18s, U20s", "Players line up and take turn throwing the ball up at the backboard and running to the back off the line. Players must jump up rebound the ball and throw it back up before landing on the groung", "3", "Rebound relay")
        d30 = Drill("0030", "Obstacle Course Dribbling", "Dribbling", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Set up cones similar to the diagram. Get players to dribble to each cone and perform a dribble move. Change up dribble moves adding complex ones as the drill progresses.", "5", "Obstacle")
        d31 = Drill("0031", "Freethrows", "Shooting", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Players take turn shooting two free throws each. As a total for the team aim for 50% +1. Eg. you have 6 players aim for 7 made shots", "2", "")
        d32 = Drill("0032", "Freethrow Knock out", "Shooting", "U8s, U10s, U12s, U14s, U16s, U18s, U20s", "Players line up on the free throw line. In continous version, players shoot and if they miss must make a layup. The player behind shoots immediately after and if the make their shot or layup before the person before them, that person is out.", "5", "")
        
        self.drills = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32]