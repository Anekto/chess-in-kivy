def layout(start, layout):
    if start == True:
        for i in range(9):
            #Generating the layout
            print()
            for j in range(9):
                print(layout[i][j], end="  ")
    return layout