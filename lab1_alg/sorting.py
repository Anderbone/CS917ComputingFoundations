import timeit

def inputfile(file):
    with open(file, 'r') as f:
        mydic = dict()
        for line in f:
            name_pri = line.split(',')
            name = name_pri[0]
            priority = int(name_pri[1])
            mydic[priority] = name
        return mydic

def get_key(dic):
    # mysort = dict()
    key_list = []
    # for key in sorted(dic.keys()):
    #      print(key, dic[key])
    # return mysort
    for k in dic.keys():
        key_list.append(int(k))
    return key_list


def in_sort(mylist):
    mylist.sort()
    return mylist


def bubble(mylist):
    length = len(mylist)
    count = length
    while count > 0:
        # count_in = length - count
        count_in = 0
        while count_in+1 < length:
            if mylist[count_in] > mylist[count_in+1]:
                # temp = mylist[count_in]
                # mylist[count_in] = mylist[count_in+1]
                # mylist[count_in+1] = temp
                mylist[count_in], mylist[count_in+1] = mylist[count_in+1], mylist[count_in]
            count_in += 1
        count -= 1
    return mylist

def merge_sort(mylist):
    length = len(mylist)
    if length == 1:
        return mylist
    else:
        mid = int(length/2)
        return merge(merge_sort(mylist[:mid]), merge_sort(mylist[mid:]))

def merge(list1, list2):
    p1 = p2 =0
    result = []
    if list1 is None and list2 is None:
        return None
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        result.extend(list1[p1:])
    if p2 <len(list2):
        result.extend(list2[p2:])

    return result





if __name__ == '__main__':
    timeStart = timeit.default_timer()
    mydic = inputfile('nameprioritiessmall.txt')
    # for i in mydic:
    #     print(i, mydic[i])
    all_key = get_key(mydic)
    # after = in_sort(all_key)
    # for k in after:
    #     print(k, mydic[k])
    # print(all_key)
    # bubble_list = bubble(all_key)
    # for k in bubble_list:
    #     print(k, mydic[k])

    merge_list = merge_sort(all_key)
    for k in merge_list:
        print(k, mydic[k])


    timeEnd = timeit.default_timer()
    time = timeEnd - timeStart
    print(time)