
#%%
# Jean-Marie Nshimiyimana
# The purpose of this code is to generate a list of all available 
# Times that the conference room is available. Once the list is 
# generatated, All the emplayees schedules will be compared to detemine 
# when they all have common time to meet between monday and Friday

conferenceRoom = [[8, 9, 13, 15], [9, 11, 16], [8, 9, 10, 12], [10, 12, 13, 15, 16], [8, 9, 10, 11, 12, 13, 14, 15, 16]]
yourself =       [[8, 12, 13, 15, 16], [8, 9, 11, 13, 14], [8, 12, 13, 15, 16], [8, 9, 11, 13, 14], [8, 9, 11, 13, 14, 15]]
anna =           [[9, 10, 11, 13, 15], [9, 10, 11], [8, 9, 10, 11, 13, 14, 15], [9, 10, 13], [8, 9, 11, 12, 15]]
bob =            [[10, 11, 13, 15], [8, 9, 10, 11], [10, 11, 13, 15], [8, 9, 13, 15], [8, 9, 11, 13]]
carrie =         [[8, 9, 10, 13, 14, 15], [11, 12, 13,14, 15], [8, 9, 10, 13,14], [12, 13, 14,15], [8, 9, 10, 11,13]]

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday']
schedule = [conferenceRoom, yourself, anna, bob, carrie]

def goal(*args): 
    # returns the count of the matching
    return len(set(args)) == 1

def generateAndTest(conferenceRoom, yourself, anna, bob, carrie):
    for a in conferenceRoom: 
        for b in yourself: 
            for c in anna: 
                for d in bob: 
                    for e in carrie: 
                        if goal(a, b, c, d, e): 
                            print ('- POTENTIAL MEETING at %s:00' %(a))

for i in range(len(schedule)): 
    print(days_of_week[i])
    generateAndTest(schedule[0][i], schedule[1][i], schedule[2][i], schedule[3][i], schedule[4][i])   
