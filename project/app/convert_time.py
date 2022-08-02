def convertTime (time):
    temp = time.split(':')
    timeMinutes = (int(temp[0])*60)+int(temp[1])+int(temp[2])/60
    return timeMinutes

def create_time_columns(bare_frame):

    # convert to integers
    bare_frame["Swim Minutes"] = bare_frame["Swim"].apply(convertTime)
    bare_frame["T1 Minutes"] = bare_frame["T1"].apply(convertTime)
    bare_frame["Bike Minutes"] = bare_frame["Bike"].apply(convertTime)
    bare_frame["T2 Minutes"] = bare_frame["T2"].apply(convertTime)
    bare_frame["Run Minutes"] = bare_frame["Run"].apply(convertTime)
    # bare_frame["Elapsed Minutes"] = bare_frame["Chip Elapsed"].apply(convert_time)

    # create cumulative times
    bare_frame["Swim+T1"] = round(bare_frame["Swim Minutes"] + bare_frame["T1 Minutes"], 2)
    bare_frame["Plus Bike"] = round(bare_frame["Swim+T1"] + bare_frame["Bike Minutes"], 2)
    bare_frame["Plus T2"] = round(bare_frame["Plus Bike"] + bare_frame["T2 Minutes"], 2)
    bare_frame["Total"] = round(bare_frame["Plus T2"] + bare_frame["Run Minutes"], 2)

    return bare_frame

# start_ages = []
# end_ages =[]
# for start in range(20, 85, 5):
#     start_ages.append(start)
# for end in range (24, 89, 5):
#     end_ages.append(end)

start_ages = [10, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
end_ages = [17, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 100]

def determine_agegroup(row):
    age = int(row['Age'])
    for start, stop in zip(start_ages, end_ages):
        if start<=age<=stop:
            return '%d-%d' %(start, stop)