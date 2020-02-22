




def calcAngle(hour,minutes):


    hour_angle = 0.5 * minutes + 30 * hour
    minute_angle = 6 * minutes

    
    angle = abs(minute_angle - hour_angle)

    return min(360 - angle,angle)




if __name__ == "__main__":
    

    print(calcAngle(12,30))

