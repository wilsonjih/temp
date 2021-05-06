#include <iostream>

using namespace std ;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int N = 0 ;
	cin >> N ;
	int array[N] ;

	for(int i = 0 ;i < N ; i ++)
		cin >> array[i] ;

	int count[100001] = {0};
	for(int i = 0 ; i < N ; i ++)
		count[array[i]] ++ ;

	int target = 0 ;
	for(int i = 0 ; i < max+1 ; i ++)
	{
		target += count[i] ;
		if(target >= ((N+1)/2))
		{	
			cout << i << endl ;
			break ;
		}
	}
	return 0 ;
}