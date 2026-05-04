#include <studio.h>
int sum_array(int arr[], int n) {
#自己定义函数，int表示函数会返回一个整数，sum_array是函数名，int arr[]表示是整数数组，int n表示数组长度（未知长度）
  int sum = 0;
  int i;
  for(i=0;i<n;i++){
  sum += arr[i];
  }
  return sum;
}

int main(){
	int nums[]={1,2,3,4,5}
	printf("sum = %d\n", sum_array(nums, 5) );
	printf("adress_nums[0] = %d\n", (void*)&nums[0] );
	#读取内存地址 
	printf("adress_nums[1] = %d\n", (void*)&nums[1] );
	
	return 0;
}
   
   
 
