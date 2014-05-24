# -*- coding: utf-8 -*-

import sys, scipy
import numpy 
import scipy.stats
import matplotlib.pyplot as plt
import pylab
from collections import Counter
import scipy.stats as stats
import matplotlib.ticker as ticker

######################################################


def plotDEM(DEM, title):
    DATA = numpy.loadtxt(DEM,) # lädt die Daten! 
    Trans = DATA[:,0] # lädt erste Spalte in Trans     	
    Band = DATA[:,1]     	
    n = 25   # Auf 25 festgelegt, da 25 gleich große Blöcke!
    


    ### Zerlegt die Messwerte in gleich große Blöcke
    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out
    
    

    #### Wendet die Funktion chunkIt auf unsere Messwerte an---bildet 25 gleich große Blöcke
    Chunks= chunkIt(Trans,25)
    #print 'Hier Chunks'
    #print Chunks    
     
    #print 'Mittelwerte'
    
    x = [] #Liste mit Mittelwerten
    for i in range(25):
        average = numpy.mean(Chunks[i]) # Berechnet Mittelwert von jedem Block
        #print average 
        x.append(average) # Fügt jeden Mittelwert der Liste hinzu
   


    

    av = numpy.mean(x) # Mittelwerlt von GESAMTEN 25 Blöcken berechnen!!
    err=stats.tstd(x)  # Unbekannt Standartabweichung berechnen
    

    #print err 
    #t = scipy.stats.t._ppf(0.95,n) #Student t faktor Aber einseitig!
    
    t =2.060 #beidseitig aus Wikipedia
    


    ### Konfidenzintervall

    con = (err*t)/(n**(1/2.)) #Konfidenzintervall
    #print 'Mittelwert'
    #print av

    print ' Konfidenzintervall'
    ob = av + con
    ub = av - con
    print ob
    print ub
    
    ###Chi Quadrat Test
    normal=stats.normaltest(x)
    print 'Chi-Quadrat-Test'
    print normal

    ### Histogramm --- Wird aber NICHT benötigt!
    

    #p211=plt.subplot(211)
    ##p211.set_title('Hauptseminar')
    #p211.set_xlabel('Transfer [MBytes]')
    #p211.set_ylabel('Anzahl')
    #
    # 
    #counts = Counter(x)    
    #heights = [counts[num] for num in x]
    #p211.bar(x, heights, align='center', width=.001)
    #
    #x_formatter = ticker.ScalarFormatter(useOffset=False)
    #p211.xaxis.set_major_formatter(x_formatter) 

    #p211.axvline(x=av,ymin=0,ymax=3, color='green')
    #p211.axvline(x=ob,ymin=0,ymax=3, color='red')
    #p211.axvline(x=ub,ymin=0,ymax=3, color='red')
    #plt.grid() 

    ### Normaler Graph
    p212 = plt.subplot(211)    
    p212.set_xlabel('Anzahl')
    p212.set_ylabel('Transfer [MBytes]')
    p212.set_title(title)
    p212.plot(x)
   

    #### Schönere Darstellung der y- Achse! 
    y_formatter = ticker.ScalarFormatter(useOffset=False)
    p212.yaxis.set_major_formatter(y_formatter) 
    
    
    plt.grid()    
    #plt.xticks(x)
    plt.tight_layout()
    plt.savefig(title+'.pdf')     	

if __name__=='__main__':
	plotDEM(\
		sys.argv[-2],\
		sys.argv[-1],\
		)
