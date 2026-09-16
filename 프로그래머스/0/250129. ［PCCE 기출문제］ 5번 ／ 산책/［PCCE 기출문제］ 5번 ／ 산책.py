def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north = north - 1
        elif i == "E" :
            east = east + 1
        elif i == "W" :
            east = east - 1
    return [east, north]
