# Lab7.py (Campbell)

def main():
    #print(twice([4, 3, 2, 5]))

    #triangle(5)

    #print(min_grid([[4, 5, 6],[1, 2, 3]]))
    
    print(has_most([[1, 2, 2],[3, 1, 3]], 3))
    print(has_most([[1, 2, 2],[3, 1, 3]], 2))

    #print(is_descending([]))
    #print(is_descending([4]))
    #print(is_descending([4, 3]))
    #print(is_descending([4, 4]))

    # print(all_same([]))    # t
    # print(all_same([[1]])) # t
    # print(all_same([[1,2,1,1],[1,1,1,1]])) # f
    # print(all_same([[1,1,1,1],[1,1,1,1]])) # t

    # print(all_different([])) # t
    # print(all_different([[1]])) # t
    # print(all_different([[1,2,1,1],[1,1,1,1]])) # f
    # print(all_different([[1,1,1,1],[1,1,1,1]])) # f
    # print(all_different([[1,2,3,4],[5,6,7,8]])) # t

    # grid1 = [[1,2,2,4],
    #          [5,2,2,8]]
    # print(find_box(grid1, 2))

    # print(find_rectangle(grid1, 1, 1, 8))
    # print(find_rectangle(grid1, 2, 2, 2))
    # print(find_rectangle(grid1, 2, 3, 2))
    pass

def get_dimensions(grid):
    """ return the number of rows and columns in a grid """
    return (len(grid), 0 if len(grid)==0 else len(grid[0]))

def twice(lst):
    new_lst = []
    for element in lst:
        new_lst.append(element)
        new_lst.append(element)
    return new_lst

def triangle(n):
    for layer in range(n):
        print((n-layer)*' '+(1+layer*2)*'*')

def min_grid(grid):
    small_number_list = grid[0][0]
    small_number_grid = grid[0][0]
    for lst in grid:
        for number in lst:
            small_number_list = min(small_number_list,number)
        small_number_grid = min(small_number_list,small_number_grid)
    return (small_number_grid)

def has_most(grid, target):
    for lst in grid:
        occurence = 0
        for number in lst:
            if target == number:
                occurence += 1
            occurences.append(occurence)


def is_descending(lst):
    pass

def all_same(grid):
    pass

def all_different(grid):
    pass

def find_box(grid, target):
    pass

def find_rectangle(grid, H, W, target):
    pass


if __name__ == "__main__":
    main()
