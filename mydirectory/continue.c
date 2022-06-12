#include<stdio.h>

int main(){
    int a=1;
    printf("enter no\n");
    for(a=1;a<=10;a++)
    {
        if(a==6)
        {
        continue;
        }
        printf("%d",a)
        a++
        
    }
    return 0;
}