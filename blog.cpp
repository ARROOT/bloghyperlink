#include <iostream>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;
int main()
{
    string bword, wlink;
    ifstream link("link.txt",ios::in);
    ifstream blog("blog.txt",ios::in);
    fstream edblog("Edblog.txt",ios::app);

    while(!blog.eof()){
        blog>>bword;
        for(int i=0;i<=5;i++){
            getline(link, wlink);
            if (bword==wlink){
                getline(link, wlink);
                edblog<<"<a href="<<wlink<<"'"<<bword<<"</a>";
                bword="";
                cout<<"ok";
            }
        }
        edblog<<bword<<" ";
    }

}
