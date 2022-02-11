import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pipe
#object class part

class Planet:

    def __init__ (self,PlanetName,solardata):
        
        __solar_data = solardata    
        __pos = np.array([0,0],float)
        __vel = np.array([0,0],float)
        
        self.PlanetName = str(PlanetName)
        
        self.position = __pos+np.array([__solar_data.loc[self.PlanetName][0],0],float) #Nowstate position
        self.velocity = __vel+np.array([0,__solar_data.loc[self.PlanetName][1]],float) #Nowstate velocity
        
        self.mu = float(__solar_data.loc[self.PlanetName][2])
        self.distance = float(__solar_data.loc[self.PlanetName][0]) #Distance from the Sun 
        
    def update (self, new_position, new_velocity):      
        self.position = new_position
        self.velocity = new_velocity

    def info(self):
        print('Planet Name:',self.PlanetName)
        print('Distance From Sun:',self.distance)
        print('Now Coordinate:',self.position)
        print('Now Velocity:',self.velocity)
        print('Planet standard gravitational parameter (mu):',self.mu)

    def __str__(self):
        return ("This is '{0}' ".format(self.PlanetName))

class Solarsystem(list):
    def __init__(self,solardata):
        super().__init__
        self.extend(Planet(name,solardata) for name in solardata.index )

    def position(self):
        for i in range(len(self)):
            print (f" {self[i].PlanetName}" , self[i].position)

#Calculation function part

def f(m_obj,data,planetindexnumber):
    
    coord = np.split(data,2)[0]
    v = np.split(data,2)[1]    
    r0 = m_obj[planetindexnumber].distance
    
    #next position
    fr = v    
    #next velocity 
    fv = np.array([0,0],float)

    for z in range(0,len(m_obj)):
        
        if z == planetindexnumber:
            continue
        else:
            dist = np.sqrt(np.sum((coord - m_obj[z].position)**2))
            
            if r0<m_obj[z].distance:
                fv += m_obj[z].mu*coord/dist**3
            else:
                fv -= m_obj[z].mu*coord/dist**3

    answer = np.concatenate((fr,fv),axis=None,dtype=float)

    return answer

def update(conn,m_obj,function,h,k):
    
    data =  np.concatenate((function.position,function.velocity),axis=None, dtype=float)     
    
    k1 = h * f(m_obj,data,k)
    k2 = h * f(m_obj,data+k1/2,k)
    k3 = h * f(m_obj,data+k2/2,k)
    k4 = h * f(m_obj,data+k3,k)
    
    data += (k1+(2*k2)+(2*k3)+k4)/6    
    conn.send(function.update(np.split(data,2)[0],np.split(data,2)[1]))
    conn.close()
    