import numpy as np
def directa (theta1, theta2, theta3,d4):

    a11=np.cos(theta3)*np.cos(theta1+theta2)-np.sin(theta1+theta2)*np.sin(theta3)
    a21=np.sin(theta1+theta2)*np.cos(theta3)+np.sin(theta3)*np.cos(theta1+theta2)
    a12=a21
    a22=-a11
    a14=350*np.cos(theta1)+300*np.cos(theta1+theta2)
    a24=350*np.sin(theta1)+300*np.sin(theta1+theta2)
    result = np.array([[a11,a12,0,a14],
                       [a21,a22,0,a24],
                       [0,0,-1,d4],
                       [0,0,0,1]])
    return result

def inversa (px,py,pz,orientacion):
    c2=(px*px+py*py-350*350-300*300)/(2*350*300)
    s2=np.sqrt(1-c2*c2)
    theta2=np.arctan2(s2,c2)
    c1=((350+300*c2)*px+300*s2*py)/(px*px+py*py)
    s1=((350+300*c2)*py-300*s2*px)/(px*px+py*py)
    theta1=np.arctan2(s1,c1)
    theta3=orientacion-theta1-theta2
    d4=pz
    return np.array([theta1,theta2,theta3,d4])

def jacobiana(theta1, theta2, theta3,d4):
    a11 = -350*np.sin(theta1)-300*np.sin(theta1+theta2)
    a12 = -300*np.sin(theta1+theta2)
    a21 = 350*np.cos(theta1)+300*np.cos(theta1+theta2)
    a22 = 300*np.cos(theta1+theta2)
    result = np.array([[a11,a12,0,0],
                       [a21,a22,0,0],
                       [0,0,0,-1],
                       [0,0,0,0],
                       [0,0,0,0],
                       [1,1,-1,0]])
    return result
print(directa(0,0,0,0))
print(directa(0,np.pi/2,0,0))
print(directa(-np.pi/2,np.pi/2,0,210))
print(directa(np.pi,0,np.pi/2,105))
print(inversa(650,0,0,0))
print(inversa(350,300,0,np.pi/2))
print(inversa(300,-350,210,0))
print(inversa(-650,0,105,3*np.pi/2))
print(jacobiana(0,-np.pi/2,np.pi/2,105))
print(jacobiana(0,np.pi/90,0,0))
print(jacobiana(np.pi/4,-np.pi/4,0,210))
print(jacobiana(-np.pi/90,np.pi/90,0,0))
