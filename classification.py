import sys

def set_date():
    try: 
        set_date = sys.argv[1]
    except:
        set_date = input("Enter a date (yyyy-mm-dd): ")
    
    return set_date

# def title_artist(list1, list2):
#     title_artist = []
#     for i in range(len(list1)):
#         title_artist.append((list1[i], list2[i]))

#     return title_artist

def artist_song_tuple(list1, list2):
    item1 = []
    item2 = []
    for i in range(100):
        item1.append(list1[i])
        item2.append(list2[i])
    # print(item1, item2)
    return (item1, item2)