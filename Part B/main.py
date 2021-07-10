import ctypes
from numpy.ctypeslib import ndpointer
import numpy as np
from time import time
import matplotlib.pyplot as plt

x = ctypes.CDLL(r"D:/eng mariam/3rd/2nd/2nd semester/DSP/Tasks/Task_Dsp3/test.so")

DFT=x.dft
DFT.restype=None
DFT.argtypes=[ndpointer(ctypes.c_double,flags="C_CONTIGUOUS"),
              ndpointer(ctypes.c_double,flags="C_CONTIGUOUS"),
              ctypes.c_double]

FFT=x.fft
FFT.restype=None
FFT.argtypes=[ndpointer(ctypes.c_double,flags="C_CONTIGUOUS"),
              ctypes.c_int]


input_signal=[]
output_signal=[]
input_output_signal=[]
time_dftSample=[]
time_fftSample=[]
NUM_samples=[]
mean_samples=[]

def testSample():
    No_Samples=2
    for i in range(12):
        Ts=1/No_Samples
        t=np.arange(0,10+Ts,Ts)
        x=1*np.cos(2*np.pi*500*t)+1*np.cos(2*np.pi*100*t)+1*np.cos(2*np.pi*200*t)+1*np.cos(2*np.pi*120*t)+1*np.cos(2*np.pi*3*t)+1*np.cos(2*np.pi*50*t)+1*np.cos(2*np.pi*1000*t)+1*np.cos(2*np.pi*50*t)+1*np.cos(2*np.pi*60*t)+1*np.cos(2*np.pi*50*t)+1*np.cos(2*np.pi*70*t)+1*np.cos(2*np.pi*50*t)+1*np.cos(2*np.pi*80*t)
        y=0*np.sin(2*np.pi*3*t)
        z=np.column_stack((x,y))
        input_signal.append(z) 
        output_signal.append(z)
        input_output_signal.append(z)
    
        No_Samples*=2
         
testSample()

N=2
for i in range(12):
    #compute time takes by dft function
    start=time()
    DFT(input_signal[i],output_signal[i],N)
    end=time()
    timer=(end-start)*1000
    time_dftSample.append(timer)
    #------------------
    #compute time takes by fft function
    start2=time()
    FFT(input_output_signal[i],N)
    end2=time()
    timer2=(end2-start2)*1000
    time_fftSample.append(timer2)
    #----------------------
    #compute error
    squared_array = np. square(np.subtract(output_signal[i],input_output_signal[i]))
    mse = squared_array. mean()
    mean_samples.append(mse)
    # end of error

    NUM_samples.append(N)
    N*=2

plt.plot(NUM_samples,mean_samples)
plt.show()
plt.plot(NUM_samples,time_dftSample)
plt.show()
plt.plot(NUM_samples,time_fftSample)
plt.show()

