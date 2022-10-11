#include <stdio.h>

int main()
{
	int uct, bjt, bjt_h, min, uct_h;
	scanf("%d", &bjt);
	
	bjt_h = bjt/100; /*bjt 小时*/
	min = bjt-100*bjt_h; /*bjt 分钟*/
	uct_h = bjt_h-8;  /*uct 小时*/

	if (uct_h>=0) {    /*未跨日*/
		if (uct_h==0) {
			printf("%d", min);
		} else {
			printf("%d", uct_h);
			if (min<10) {
				printf("0%d", min);
			} else {
				printf("%d", min);
			}
		}
	} else {    /*跨日*/
		uct_h += 24;
		printf("%d", uct_h);
		if (min<10) {
			printf("0%d", min);
		} else {
			printf("%d", min);
		}
	}
	return 0;
	}
