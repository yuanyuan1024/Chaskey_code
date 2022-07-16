#include<iostream>
#include<stack>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<functional>
#include<limits.h>
#include<utility>
#include<queue>
#include<algorithm>
#include<cstring>
#include<iomanip>
#include<bitset>
#include<unordered_map>
#include<fstream>
#include<math.h>
#include<chrono>
#include<random>
#include<assert.h>
#include <thread>
#define lowbit(x) ((x)&(-x))
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

using namespace std;
//
const int maxn = 5e5 + 19;
const int maxm = 1e6 + 19;
const int inf = 0x3f3f3f3f;
const ll mod = 998244353;
const double eps = 1e-10;
typedef pair<int, int> pii;
int dir[4][2] = { {0,1},{1,0} ,{0,-1},{-1,0} };
mt19937 rnd((unsigned int)chrono::steady_clock::now().time_since_epoch().count());

typedef unsigned int u32;
int total = 1 << 20;
u32 move(u32 val, int n)
{
	return (val >> (32 - n) | (val << n));
}
vector<u32> round(vector<u32>& t)
{
	vector<u32> miao(4);
	u32 v1 = t[0];
	u32 v0 = t[1];
	u32 v2 = t[2];
	u32 v3 = t[3];
	u32 t0, t1, t2, t3, t4, t5;
	t0 = v0 + v1;
	t2 = (move(v0, 7) ^ t0);
	t1 = v2 + v3;
	t3 = (move(v3, 13) ^ t1);
	t4 = t1 + t2;
	t5 = t3 + move(t0, 16);
	miao[3] = (move(t3, 8) ^ t5);
	miao[0] = t2;
	miao[1] = (move(t2, 5) ^ t4);
	miao[2] = move(t4, 16);
	return miao;
}

vector<u32> mask(4);
string s_mask[4] = { "00002000","00600008","20000000","00000008" };
int main()
{
	for (int i = 0; i < 4; i++)
	{
		u32 cnt = 31;
		for (int j = 0; j < s_mask[i].size(); j++)
		{
			u32 p = s_mask[i][j] - '0';
			for (int k = 3; k >= 0; k--,cnt--)
			{
				if (p & (1 << k))
					mask[i] |= (1 << cnt);
			}
		}
	}
	int mm = 0;
	vector<u32> miao(4), rmiao(4);
	for (int x = 0; x < 10; x++)
	{
		int ans = 0;
		for (int j = 0; j < total; j++)
		{
			for (int i = 0; i < 4; i++)
			{
				miao[i] = rnd();
				rmiao[i] = move(miao[i], 1);
			}
			miao = round(miao);
			rmiao = round(miao);
			miao = round(miao);
			rmiao = round(rmiao);
			miao = round(miao);
			rmiao = round(rmiao);
			for (int i = 0; i < 4; i++)
			{
				move(miao[i], 1);
				miao[i] ^= rmiao[i];
			}
			int tmp = 0;
			for (int i = 0; i < 4; i++)
			{
				miao[i] &= mask[i];
				for (int k = 0; k < 32; k++)
				{
					if (miao[i] & (1 << k))
						tmp++;
				}
			}
			if (tmp % 2 == 0)
				ans++;
			
		}
		cout << abs(ans - total / 2) << endl;
		mm += abs(ans - total / 2);
	}
	mm /= 10;
	cout << mm;
	
	
	return 0;
}
