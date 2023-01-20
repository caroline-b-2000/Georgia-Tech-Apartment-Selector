def GTApartmentSelector(csv, roomnum, location, floor, laundry):
    import requests
    afile = open(csv, 'r')
    header = afile.readline()
    data = afile.readlines()
    newlist = []
    aDict = {}
    aDict['perfect fit (all 4 parameters fit!)'] = []
    aDict['good fit (2 or 3 parameters fit!)'] = []
    aDict['ok fit (one parameter fits)'] = []
    aDict["don't live there (none of the parameters align)"] = []
    for item in data:
        item = item.strip()
        newlist.append((item.split(',')))
    for item in newlist:
        name = item[0]
        totalRooms = item[1]
        side = item[2]
        totalFloors = item[3]
        laundryRoom = item[4]
        count = 0
        if roomnum == totalRooms:
            count += 1
        if location == side:
            count += 1
        if floor <= int(totalFloors):
            count += 1
        if bool(laundry) == bool(laundryRoom):
            count += 1
        if count == 4:
            aDict['perfect fit (all 4 parameters fit!)'] += [name + ": (a " + str(totalRooms) + " person apartment)"] 
        elif count == 3 or count == 2:
            aDict['good fit (2 or 3 parameters fit!)'] += [[name + ": (a " + str(totalRooms) + " person apartment)"]]
        elif count == 1:
            aDict['ok fit (one parameter fits)'] += [[name + ": (a " + str(totalRooms) + " person apartment)"]]
        elif count == 0:
            aDict["don't live there (none of the parameters align)"] += [[name + ": (a " + str(totalRooms) + " person apartment)"]]
    for key in aDict:
        print("\n")
        print("category: " + key + ":")
        if aDict[key] == []:
                print("None :(")
        else:
            for item in aDict[key]:
                print(str(item).replace("[", "").replace("]", "").replace("'", ""))

#example cases
'''
print(GTApartmentSelector('gt-apartments.csv', 4, 'East', 3, True))
print(GTApartmentSelector('gt-apartments.csv', 1, 'West', 150, False))
print(GTApartmentSelector('gt-apartments.csv', 2, 'West', 1, True))
print(GTApartmentSelector('gt-apartments.csv', 4, 'East', 10, False))
print(GTApartmentSelector('gt-apartments.csv', 7, 'West', 4, True))
'''