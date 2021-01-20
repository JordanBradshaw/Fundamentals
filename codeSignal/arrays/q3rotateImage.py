# Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.
#
# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
def rotateImage(a):
    returnList = []
    for i in range(0, len(a)):
        returnList.append([])
    for i in range(0, len(a)):
        y = len(a) - i - 1
        for x in range(0, len(a)):
            returnList[x].append(a[y][x])
    return returnList


rotateImage(a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
