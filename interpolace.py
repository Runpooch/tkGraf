import scipy.interpolate as ip
import pylab as lab

x = "0 0.3 0.5 0.8 1  2  3".split()
y = "0 0.1 0.5 1   3 10 30".split()

x = list(map(float,x))
y = list(map(float,y))

newX = lab.linspace(0,3 ,333)
spl = ip.UnivariateSpline(x,y)
newY = spl(newX)

lab.plot(x,y,"o", label = "body")
lab.plot(newX, newY,":", label = "interpolate" )
lab.grid()
lab.legend()
lab.show()