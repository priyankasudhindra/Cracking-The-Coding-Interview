#Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
#write a method to rotate the image by 90 degrees. Can you do this in place?


def rotateMatrix(matrix):
    final_matrix = ['x'] * len(matrix)
    i = 0
    pos = 0
    while pos < len(matrix) - 1:
        new_pos = pos + pos + 1 + (i)
        if new_pos > len(matrix):
            new_pos = new_pos % 10
        final_matrix[new_pos] = matrix[pos]
        i += 1
        pos += 1
    new_pos = pos + pos + 1 + (i)
    if new_pos > len(matrix):
        new_pos = new_pos % 10
    final_matrix[new_pos] = matrix[pos]
    return final_matrix


if __name__ == "__main__":
    mx = input("Enter the elements of the matrix: ")
    mx = list(mx)
    res = rotateMatrix(mx)
    print(res)


