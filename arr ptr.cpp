#include <stdio.h> 

int fun(int ptr[]) 
{ 
int x = 20; 

// size of a pointer is printed 
printf("sizeof(ptr) = %d\n", sizeof(ptr)); 

// This allowed because ptr is a pointer, not array 
ptr = &x; 

printf("*ptr = %d ", *ptr); 

return 0; 
} 
// Driver code 
int main() 
{ 
int arr[] = {10, 20, 30, 40, 50, 60}; 
fun(arr); 
printf("%d",arr);
return 0; 
} 

