#include <stdio.h>
#include <math.h>


int main()
{
     long binary = 0,binary1=0,binary2=0;
    int rem,rem1,rem2, temp1 = 1,c=0,d=0,e=0,temp2 = 1,temp3 = 1;

    int a,b,sum=8,n;
    printf("Enter TWO Decimal Number: ");

    scanf("%d%d", &a,&b);
     sum=a+b;
     while (a!=0)
    {

        rem = a%2;
        a = a / 2;
        binary = binary + rem*temp1;
        temp1 = temp1 * 10;
        c++;
    }

     while (b!=0)
    {

        rem1 = b%2;
        b = b / 2;
        binary1 = binary1 + rem1*temp2;
        temp2 = temp2 * 10;
        d++;
    }


    if(c>d)
        n=c;
    else
        n=d;

      while (sum!=0)
    {

        rem1 = sum%2;
         sum = sum / 2;
        binary2 = binary2 + rem2*temp3;
        temp3 = temp3 * 10;
        e++;
    }



if(e>n)

 printf("OVERFLOW DETECTED");

 else
  printf("OVERFLOW NOT DETECTED");
    return 0;
}



