#include <stdio.h>

int main()
{
	int x, y, m, t=1;
	scanf("%d", &x);
	if (x<0) {
		printf("fu ");
		x *= -1;
	}
	m = x;
	while (m>9) {
		m /= 10;
		t *= 10;
	}
	do {
		y = x/t;
		if (y==0) {
			printf("ling");
		} else if (y==1) {
			printf("yi");
		} else if (y==2) {
			printf("er");
		} else if (y==3) {
			printf("san");
		} else if (y==4) {
			printf("si");
		} else if (y==5) {
			printf("wu");
		} else if (y==6) {
			printf("liu");
		} else if (y==7) {
			printf("qi");
		} else if (y==8) {
			printf("ba");
		} else if (y==9) {
			printf("jiu");
		}
		x %= t;
		t /= 10;
		if (t>0) {
			printf(" ");
		}
	} while (t>0);
	return 0;
}
