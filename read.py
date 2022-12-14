import numpy
import matplotlib.pyplot
def draw(X,Y,Z):
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(X)):
        ax.scatter(X[i],Y[i],Z[i],c="grey")
        ax.set_xlabel('h')
        ax.set_ylabel('l')
        ax.set_zlabel('rate')
    tmp=numpy.argmax(Z)
    ax.scatter(X[tmp],Y[tmp],Z[tmp],c="red")
    matplotlib.pyplot.show()                                                                    
f=open("out.txt",mode="r")
tmp=f.readlines()
f.close()
t=tmp[0].split(" ")
h=numpy.asfarray(t[:len(t)-1])
t=tmp[1].split(" ")
l=numpy.asfarray(t[:len(t)-1])
t=tmp[2].split(" ")
rate=numpy.asfarray(t[:len(t)-1])
print(h)
print(l)
print(rate)
i=numpy.argmax(rate)
print(h[i])
print(l[i])
print(rate[i])
draw(h,l,rate)
