# from turtle import Turtle,Screen
# tinny =Turtle()
# print(tinny)
# tinny.shape("turtle")
# # tinny.bgcolor("black")
# # tinny.bgcolor()
# tinny.color("Coral")
# tinny.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# from prettytable import PrettyTable

# table=PrettyTable()

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

# table.add_column("Pokemon Name",["Pikachu","Squirtle","Charander"])
# table.add_column("Type",["Electric","Water","Fire"])
# table.align["Pokemon Name"]="l"
# table.align["Type"]="c"
# table.align="c"


# print(table)




class User:
    def __init__(self,user_id,username):
        # print("New user is created everytime")
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1


user_1=User("001","Harsh")

# user_1.id="001"
# user_1.username="Harsh"

user_2=User("002","hhahg")

# user_2.id="002"
# user_2.username="ABHJBAh"
print(user_1.username,user_1.id)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
