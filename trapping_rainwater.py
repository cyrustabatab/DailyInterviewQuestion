


def trapping_rainwater(elevations):
    
    assert elevations,"empty elevations"

    #ignore first and last index
    current_max= 0
    max_to_left = [current_max]
    for i in range(1,len(elevations)):
        height = elevations[i] 
        max_to_left.append(current_max)

        current_max = max(current_max,height)

    current_max = elevations[-1]

    rain_water = 0 

    amounts = []

    for i in range(len(elevations) -2,0,-1): #ignore first hieght 
        height = elevations[i]
        
        if height < current_max and height < max_to_left[i]:
            value = min(max_to_left[i],current_max) - height
            amounts.append(value)
            rain_water += min(max_to_left[i],current_max) - height

        current_max = max(current_max,height)


    return rain_water






if __name__ == "__main__":
    

    elevations = [0,8,0,0,5,0,0,10,0,0,1,1,0,3]

    print(trapping_rainwater(elevations))
    


