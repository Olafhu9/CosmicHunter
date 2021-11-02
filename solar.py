import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def find_ticks( nticks, xmin, binwidth ):
	nbins = nticks-1
	xmax = xmin + nbins * binwidth
	bins = np.linspace( xmin, xmax, nticks )
	return bins

def find_bins( xmin, xmax, binwidth ):
    n = int( (xmax-xmin) / binwidth ) + 1
    bins = np.linspace( xmin, xmax, n )
    return bins

d = pd.read_csv('/Users/rapuz/Desktop/CosmicHunter/Data/monthly/07.23/CSMHUNT_12300_2021-7-23_6-0-8.csv', sep='\s*[;]\s*', skipinitialspace=True)
d = d.loc[ d['COINC']>0 ]
d['num']=d['num']-2

d = d.loc[ d['num']%6==0 ]

d['Rate'] = d['COINC']/600
d = d.loc[ d['Rate']<.55]
err = np.std( d['Rate'] )

d['h'] = pd.to_numeric( d.time.str.split(':').str[0] )+8
d['m'] = pd.to_numeric( d.time.str.split(':').str[1] )+3
d['real time'] = d['h'].map(str)+':'+d['m'].map(str)
d['date time'] = d['date']+' '+d['real time']

plt.rcParams['figure.figsize'] = (12, 4)
plt.errorbar(d['date time'], d['Rate'], yerr=err, ecolor='black', elinewidth=0.7, linewidth=2, color='red', capsize=1, fmt='o-', markersize=4)
#plt.plot( d['date time'], d['Rate'], 'ro-', markersize=5 )

plt.title('Cosmic Rate vs Time', fontsize=15)
plt.xlabel('Time [dd/mm/yyyy hh:mm]', fontsize=12)
plt.ylabel('Rate [Hz]', fontsize=12)

#xtick = find_ticks( 4, 0, 96 )
xtick = find_ticks( 8, 0, 48 )
ytick = find_bins( 0.35, 0.5, 0.05 )
plt.xticks( xtick, rotation=-30, fontsize=9 )
plt.yticks( ytick ) 
plt.savefig('solar_july.pdf',bbox_inches='tight')
plt.show()
