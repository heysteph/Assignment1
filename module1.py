import matplotlib.pyplot as plt

# I was inspired by https://stackoverflow.com/questions/43971138/python-plotting-colored-grid-based-on-values
# I changed it accordingly to look like a chessboard!
def chessboard():
    fig = plt.subplots()
    #Create an 8x8 matrix with alternating entries of 0 and 1
    a = [[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1]]

    #Plot the matrix with color
    plt.imshow(a,cmap='copper')
    #plt.axis('off') #remove axis

    #Create labels for x-axis
    plt.text(-0.1, 7, 'a', dict(size=10), color='white')
    plt.text(0.9, 7, 'b', dict(size=10))
    plt.text(1.9, 7, 'c', dict(size=10), color='white')
    plt.text(2.9, 7, 'd', dict(size=10))
    plt.text(3.9, 7, 'e', dict(size=10), color='white')
    plt.text(4.9, 7, 'f', dict(size=10))
    plt.text(5.9, 7, 'g', dict(size=10), color='white')
    plt.text(6.9, 7, 'h', dict(size=10))
    
    #Create labels for y-axis
    plt.text(-1,7,'1')
    plt.text(-1,6,'2')
    plt.text(-1,5,'3')
    plt.text(-1,4,'4')
    plt.text(-1,3,'5')
    plt.text(-1,2,'6')
    plt.text(-1,1,'7')
    plt.text(-1,0,'8')

    plt.axis('off')
    plt.show()
    plt.savefig('chessboard.png')
        