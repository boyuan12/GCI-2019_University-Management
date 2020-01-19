from pyexcel_ods import get_data
import json
import operator
import sys

# function for calculating academinc
def academic(file):
    """Setup Basic Dict/List"""
    subjects = {}
    grades = []

    """Check whether file exist or is it readable"""
    try:
        data = get_data(file)
    except:
        raise Exception("Can't read/find file")
    list = json.loads(json.dumps(data))['Sheet1'][2]
    i = 0

    """Factor by 2 for subjects: Maths (Algebra & Geometry) and Physics"""
    for item in list:
        subjects[i] = item
        if (item == 'Algebra'):
            global algebra_id
            algebra_id = i
        if (item == 'Geometry'):
            global geometry_id
            geometry_id = i
        if (item == 'Physics'):
            global physics_id
            physics_id = i
        i+=1

    """Get total row number"""
    ctr = sum(map(len, json.loads(json.dumps(data)).values()))

    """Append candidate information to list: grade"""
    g = 3
    for i in range(ctr - 3):
        grades.append(json.loads(json.dumps(data))['Sheet1'][g])
        g+=1

    """ if empty row exists, delete them """
    if (x for x in grades if x != []):
        list2 = [x for x in grades if x != []]
    else:
        list2 = grades

    """ Multiply by the factor """
    for i in list2:
        i[algebra_id] = i[algebra_id] * 2
        i[geometry_id] = i[geometry_id] * 2
        i[physics_id] = i[physics_id] * 2

    """ grade dict to keep track individual student grade """
    grade = {}

    # Loop through the grades
    for i in list2:
        for j in i:
            if (type(j) == str):
                del i[0]
                grade[j] = i

    """ append the grade """
    for i in grade:
        grade[i] = sum(grade[i]) / len(grade[i]) * 0.4

    """return grade dict as final result for this function"""
    return grade

# function for calculating IELTS (based on academic function)
def ielts(file):
    """ Create a list and dict & read/find file"""
    ielts = []
    ielts_dict = {}
    try:
        data = get_data(file)
    except:
        raise Exception("Can't read/find file")

    """ same approach as first function, read info and append to ielts"""
    ctr = sum(map(len, json.loads(json.dumps(data)).values()))
    g = 3
    for i in range(ctr - 3):
        ielts.append(json.loads(json.dumps(data))['Sheet1'][g])
        g+=1

    """ Append detail information (name, score) to idelts_dict """
    for i in ielts:
        for j in i:
            if (type(j) == str):
                del i[0]
                ielts_dict[j] = i

    """ AVG the score and multiple by overall factor """
    ielts_list = []
    for i in ielts_dict:
        ielts_dict[i] = sum(ielts_dict[i]) / len(ielts_dict[i]) * 0.3
        ielts_list.append(ielts_dict[i])

    """ return idelts_dict as final solution """
    return ielts_dict


# function for calculating interview
def interview(file):
    """ setup and read info """
    interview = []
    interview_dict = {}
    try:
        data = get_data(file)
    except:
        raise Exception("Can't read/find file")

    """ read info and append info"""
    ctr = sum(map(len, json.loads(json.dumps(data)).values()))
    g = 3
    for i in range(ctr - 3):
        interview.append(json.loads(json.dumps(data))['Sheet1'][g])
        g+=1

    """ append information to dict """
    for i in interview:
        for j in i:
            if (type(j) == str):
                del i[0]
                interview_dict[j] = i

    """ AVG the score and multiply an overall factor """
    interview_list = []
    for i in interview_dict:
        interview_dict[i] = sum(interview_dict[i]) / len(interview_dict[i]) * 0.3
        interview_list.append(interview_dict[i])

    """ return inter_dict as final output """
    return interview_dict

# main function for using function & creating file
def main():

    # See if user provide right number of command-line args
    try:
        result1 = academic(sys.argv[1])
        result2 = academic(sys.argv[2])
        result3 = academic(sys.argv[3])
        result4 = academic(sys.argv[4])
        result5 = ielts(sys.argv[5])
        result6 = interview(sys.argv[6])
    except:
        raise Exception('No/Not enough file provided')

    overall = {}

    # average all academic score
    for i in result1:
        overall[i] = (result1[i] + result2[i] + result3[i] + result4[i]) / 4

    # add along with IELTS score and Interview score
    for i in result5:
        overall[i] = overall[i] + result5[i] + result6[i]

    # sort the dict is desc order
    sorted_d = sorted(overall.items(), key=operator.itemgetter(1), reverse=True)

    # store name of the candidate
    name = []

    # Append name
    for i in sorted_d:
        name.append(i[0])

    # write file
    file = open("result.txt","w")
    for i in name:
        file.write(i + '\n')
    file.close()

if __name__ == "__main__":
    main()