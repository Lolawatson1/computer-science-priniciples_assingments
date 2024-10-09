#include <stdio.h>
char sibs[7][20] = {"Max", "Barrett", "Xander", "Jacq", "Lola", "William", "Oliver"};
int i; 
int main (){
    while(i<10){
        printf("%s\n", sibs[i]);
        i++;

    }
    return 0;
}