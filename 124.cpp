#include <iostream>
#include <cstdio>

using namespace std ;


#define modx %1000000007
#define ll long long int 

typedef struct Matrix
{
	ll m[2][2] ;
}matrix;


matrix mul(matrix a , matrix b)
{
	matrix ans ;
	for(int i = 0 ; i < 2 ; i ++)
		for(int j = 0 ; j < 2 ; j ++)
		{
			ll temp = 0 ;
			for(int inner = 0 ; inner < 2 ; inner ++)
			{
				temp += (a.m[i][inner] modx )*(b.m[inner][j] modx );
				temp = temp modx ;
			}
			ans.m[i][j] = temp modx ;
		}
	return ans;
}

void print_matrix(matrix a)
{
	for(int i = 0 ; i < 2 ; i ++)
	{
		for(int j = 0 ; j < 2 ; j ++)
			cout << a.m[i][j] << " ";
		cout << "\n" ;     
	}
}

matrix quickpow(matrix a,ll n)//calculate a^n
{ 	
	if(n == 1) return a ;
	matrix temp = quickpow(a,(n/2)) ;
	if(n % 2 == 0 )
		return(mul(temp,temp));
	else
		return(mul(a,mul(temp,temp)));
}

int main()
{
	matrix a ;

	ll t ;
	// cin >> t ;
	scanf("%lld",&t) ;
	ll i = 0 ;
	for(i = 0 ; i < t ; i ++)
	{
		matrix a ;
		ll a1,a2,x,y,n ;
		// cin >> a1 >> a2 >> x >> y >> n ;
		scanf("%lld %lld %lld %lld %lld",&a1,&a2,&x,&y,&n);
		a.m[0][0] = x ;
		a.m[0][1] = y ;
		a.m[1][0] = 1 ;
		a.m[1][1] = 0 ;
		if(n == 1)
		{
			cout << a1 ;
			return 0 ;
		}
		else if(n == 2)
		{
			cout << a2 ;
			return 0 ;
		}
		matrix final_matrix = quickpow(a,n-2) ;
		cout << ((final_matrix.m[0][1] modx )*( a1 modx ) modx +(final_matrix.m[0][0] modx )*(a2 modx ) modx ) modx ;
	}
	return 0 ;
}
