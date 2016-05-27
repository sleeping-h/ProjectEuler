#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
double next_r(double r1,double r2,double r3){	// Descartes' theorem
    return 1/(1/r1+1/r2+1/r3+2*sqrt(1/r1/r2+1/r2/r3+1/r3/r1));
}
double big_R(double r1,double r2,double r3){
    return 1/(1/r1+1/r2+1/r3-2*sqrt(1/r1/r2+1/r2/r3+1/r3/r1));
}
double f(double x){
    return x>0?x*x:0;
}
double s(double r1,double r2,double r3,int n){	// Apollonian gasket
    if (n==9) return next_r(r1,r2,r3)*next_r(r1,r2,r3);
    return f(next_r(r1,r2,r3))+s(r1,r2,next_r(r1,r2,r3),n+1)+s(r3,r2,next_r(r1,r2,r3),n+1)+s(r1,r3,next_r(r1,r2,r3),n+1);
}
int main()
{
    double r1,r2,r3,big;
    r1=r2=r3=1; 
    big=big_R(r1,r2,r3);
    cout <<setprecision(8)<< (big*big-3-s(r1,r2,r3,0)-3*s(r1,r2,big,0))/big/big<< endl;
    return 0;
}
