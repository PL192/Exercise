#include <stdio.h>

int main()
{
	int x, odd=0, even=0;
	scanf("%d", &x);
	while (x>=0) {
		if (x%2 == 0) {
			even ++;
		} else {
			odd ++;
		}
		scanf("%d", &x);
	}
	if (x==-1) {
		printf("%d %d", odd, even);	
	}
	return 0;
}
