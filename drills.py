#Creating a class for drills to be based off

class Drill:
    def __init__(self, drill_id, drill_name, drill_description, drill_duration, drill_diagram):
        self.drill_id = int(drill_id)  #drill_id can only be an integer
        self.drill_name = drill_name
        self.drill_description = drill_description
        self.drill_duration = int(drill_duration)  #drill_duration can only be an integer
        self.drill_diagram = "drill_diagrams/"+drill_diagram+".png"

#Class to manage all drills and related functions
class Drill_manager:
    def __init__(self):
        d1 = Drill("0001", "Cincinnati Drill", "1 passes to 2 who pivots and passes to 3 cutting to the basket for a shot or layup. 3 keeps going to the opposite outlet position, 2 rebounds, 1 replaces 2 and 2 outlets to 3. Encourage strong passing, cutting and finishing", "5", "Cincinnati")


        self.drills = [d1]