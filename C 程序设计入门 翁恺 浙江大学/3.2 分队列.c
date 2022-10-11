#include <stdio.h>

int main()
{
	int x, i=1, y;
	scanf("%d", &x);
	for (i=1; i<=x; i++) {
		if (i%2 != 0) {  /*取奇数*/
			printf("%d", i);
			y = x-1;
			if (i!=y) {    /*测试值为20或2*/
				if (i!=x) {
					printf(" ");				
				}
			}
		}
	}
	return 0;
}
