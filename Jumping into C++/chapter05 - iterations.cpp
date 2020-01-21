#include <iostream>
using namespace std;

// for문 예시 - 정확히 몇번 반복해야 하는지 알 때 유용
// int main()
// {
//   for (int i =0; i<10; i++)
//   {
//     cout << i<< '\n';
//   }
//   return 0;
// }

// while문 예시 - 조건을 만족할때까지 계속 반복해야 할 때 유용
// int main()
// {
//   int i = 0;
//   while (i < 10)
//   {
//     cout << i << '\n';
//     i++;
//   }
//   return 0;
// }

// ex5-3 사용자가 입력하는 수를 누적하여 더하는 프로그램. 0을 입력하면 중단
int main()
{
  int a = 1;
  int sum = 0;
  while (a != 0)
  {
    cout << "enter a number: ";
    cin >> a;
    sum = sum + a;
    cout << "the sum is " << sum << '\n';
  }
  return 0;
}
