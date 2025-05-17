marks = {
    "Harsh":100,
    "Shubham":23,
    "Rohan":223,
    "Harry":123,
    0:"Harry"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Harsh":99})
print(marks)
print(marks.get("Harsh2")) #in this case it returns none
print(marks["Harsh2"]) #in this case it returns error