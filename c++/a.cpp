//pervaya programma
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

struct Auto{
	int hzorutyun;
	float aragutyun;
	string guyn;
	string model;
};

int main(int argc,const char * argv[]){
	Auto Mers={200,270.5,"spitak","Mersedes e230"};
    //Auto Mers;
    //Mers.hzorutyun=200;
    //Mers.aragutyun=270.5;
    //Mers.guyn="spitak";
    //Mers.model="Mersedes e230";
    cout<<"dzer meqenai modelne - "<<Mers.model<<",sharjichi hzorutyun@ - "<<Mers.hzorutyun<<" dziauj,"<<"aragutyun@ - "<<Mers.aragutyun<<",guyn@ - "<<Mers.guyn<<endl;
	

    
       
    return 0;
}
