#include<stdio.h>
int main()
{
int n,i,m,rev,r;
printf("enter n");
scanf("%d",&n);
m=n;
while(m>0)
{
	r=m%10;
	m=m/10;
	rev=rev*10+r;
if(n==rev)
{
	printf(" %d is palindrome",n);
}
}
}
