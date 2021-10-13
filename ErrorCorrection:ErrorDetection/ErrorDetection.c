#include<stdio.h>
#include<string.h>
#define N strlen(g)
char s[28],t[28],g[28];
int a,e,c;
void xor()
{
	for(c=1;c<N;c++)
	s[c]=((s[c]==g[c]?'0':'1'));
}
void crc()
{
	for(e=0;e<N;e++)
	s[e]=t[e];
	do{
		if(s[0]=='1')
		xor();
		for(c=0;c<N-1;c++)
		s[c]=t[e++];
	}
	while(e<=a+N-1);
}
int main()
{
	printf("\n Enter The Message:");
	scanf("%s",g);
	printf("\nEnter Data:");
	scanf("%s",t);
	printf("\n-------------------");
	printf("\nGenerating Polynomial:%s",t);
	a=strlen(t);
	for(e=a;e<a+N-1;e++)
	t[e]='0';
	printf("\n-------------------");
	printf("\nModified Data is:%s",t);
	printf("\n-------------------");
	crc();
	printf("\nChecksum is :%s",s);
	for(e=a;e<a+N-1;e++)
	t[e]=s[e-a];
	printf("\n---------------------");
	printf("\nFinal codeword is :%s",t);
	printf("\n--------------------");
	printf("\nTest erro detection 0(yes) 1(no)?:");
	scanf("%d",&e);
	if(e==0)
	{
		do{
			printf("\nEnter the position where error is to be inserted:");
			scanf("%d",&e);
		}
	
		while(e==0||e>a+N-1);
		t[e-1]=((t[e-1]=='0')?'1':'0');
		printf("\n--------------------");
		printf("\n--------------------");
		printf("\nErroneous Data:%s\n",t);
	}
}