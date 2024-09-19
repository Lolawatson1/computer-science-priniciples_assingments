#include <stdio.h>
#include <string.h>

int main(void){
char fname[50];
char fname[] = ">>>";
char prefix[] = "<<<";
printf("please tell me your name: ");
scanf("%s", fname);
strcat(prefix,fname);
printf("%s\n",prefix);
return 0;
}