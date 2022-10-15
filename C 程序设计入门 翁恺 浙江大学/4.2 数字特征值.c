#include <stdio.h>
int main()
{
	int x;
	scanf("%d",&x);
	int t = x, ten=1, digit=0;
	int num=0;
	int par_num, par_digit, same_par;
	int bi=1, bi_num=0;

	while (t>0) {
	ten *= 10;
	digit ++;    /*位数*/
	num = ((x%ten)-num)/(ten/10);    /*数字*/
	
	if (num%2 == 0) {    /*判断奇偶性*/
		par_num = 0;
	} else {
		par_num = 1;
	}
	
	if (digit%2 == 0) {
		par_digit = 0;
	} else {
		par_digit = 1;
	}
	
	if (par_digit == par_num) {
		same_par = 1; 
	} else {
		same_par = 0;
	}

	bi *= 2;    /*二进制换算十进制*/
	bi_num += same_par*(bi/2);
	t /= 10;
	}
  
	printf("%d", bi_num);
	
	return 0;
}
