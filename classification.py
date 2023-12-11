import sys
"""
creates the date to be found as well as sets up sys.argv
"""
def set_date():
    try:
        # 1.6 
        set_date = sys.argv[1]
    except:
        set_date = input("Enter a date (yyyy-mm-dd): ")
    
    return set_date

"""
retruns a tuple of lists 
"""
def artist_song_tuple(list1, list2):
    item1 = []
    item2 = []
    for i in range(100):
        item1.append(list1[i])
        item2.append(list2[i])
    # print(item1, item2)
    # 5.14
    return (item1, item2)