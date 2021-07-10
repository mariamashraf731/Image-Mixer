#include<math.h>
#include<vector>
#include<iostream>
#include<complex>
#include<iomanip>
using namespace std;

extern "C"
void dft(complex<double>signal[],complex<double>OUTPUTER[],double N);
extern "C"
void fft(complex<double>inputSignal[],int size);

void dft(complex<double>signal[],complex<double>OUTPUTER[],double N)
{

// determine number of samples
int K = N;

complex<double> intSum;
vector<complex<double>> output;
vector<double> taken;
output.reserve(K);

// loop through each K
for (int k=0 ; k < K; k++){

    // loop through each n
    intSum = complex<double>(0,0);
    for (int n=0; n<N ;n++){
        int z= k*n;
        taken.push_back(z);
        double realPart=cos(((2*M_PI)/N)*k*n);
        double imgPart=sin(((2*M_PI)/N)*k*n);
        complex<double> w (realPart, imgPart);
        intSum += signal[n]*w;


    }
    output.push_back(intSum);

    OUTPUTER[k]=intSum;

}
}

void fft(complex<double>inputSignal[],int size)
{
    const size_t N= size;
    if (N==1){
        return;}
    // split the sample into even and odd subsums
    // find half the toltal number of samples
    int M = size/2;

    // Declare an even and an odd compelex vector 
    complex<double>* Xeven=new complex<double>[M];
    complex<double>* Xodd=new complex<double>[M];
    for ( int i= 0; i<M; i++)
    {
        Xeven[i]= inputSignal[2*i];
        Xodd[i]= inputSignal[2*i+1];
    }
    
    fft(Xeven,M);
    fft(Xodd,M);


    // combine the values found 
    for ( size_t k=0 ; k < N/2 ; k++)
    {
        complex<double> cmplxexponential = polar(1.0,-2*M_PI*k/N)*Xodd[k];
        inputSignal[k]=Xeven[k]+cmplxexponential;
        inputSignal[k+N/2]=Xeven[k]-cmplxexponential;

    }
}



int main(){

}