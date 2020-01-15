



def dfs_visit(courses,course,visited,stack):

    visited.add(course)

    for next_course in courses[course]:
        if next_course not in visited:
            dfs_visit(courses,next_course,visited,stack)


    stack.append(course)

def course_prerequisites(courses):
    

    prereq_to_courses = {c: set() for c in courses}

    for course,prereqs in courses.items():
        for prereq in prereqs:
            prereq_to_courses[prereq].add(course)
    
    print(prereq_to_courses)
    stack = []
    visited = set()

    for course in prereq_to_courses:
        if course not in visited:
            dfs_visit(prereq_to_courses,course,visited,stack)


    stack.reverse()

    return stack





if __name__ == "__main__":
    

    courses = {
            'CSC300': ['CSC100','CSC200'],
            'CSC200': ['CSC100'],
            'CSC100': []
            }

        

    print(course_prerequisites(courses))
