



class Point:

    def __init__(self,x,start=True):
        self.x = x
        self.start = start

    
    def __lt__(self,point):
        if isinstance(point,Point):

            if self.x == point.x:
                if not self.start and point.start:
                    return True
                elif not point.start and self.start:
                    return False
                else:
                    return True
            else:
                return self.x < point.x

    def __repr__(self):
        return f"Point({self.x},{self.start})"


def room_scheduling(intervals):

    points = []
    for start,end in intervals:
        points.append(Point(start))
        points.append(Point(end,start=False))


    points.sort()

    count = 0
    maximum = 0

    for point in points:
        if point.start:
            count += 1
        else:
            count -= 1

        maximum = max(count,maximum)
    
    return maximum




if __name__ == "__main__":
    

    points = [(30,75),(0,50),(60,150)]

    print(room_scheduling(points))
