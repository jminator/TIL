#include <iostream>
using namespace std;

// // ex1-1
// int main()
// {
//   cout <<"joosung min"
// }

// // ex1-2
// int main()
// {
//   int a;
//   int b;
//
//   cout << "enter two numbers: ";
//   cin >> a >> b;
//   cout << a+b;
// }

// // ex1-3
// int main()
// {
//   float a, b;
//   cout << "enter two numbers: ";
//   cin >> a >> b;
//   cout << (a/b);
// }

// // practice
// int main()
// {
//   string username;
//   string password;
//   cout << "enter your username: ";
//   getline(cin, username, '\n');
//
//   cout << "enter your password: ";
//   getline(cin, password, '\n');
//   if (username == "root" && password == "xyzzy")
//   {
//     cout << "access allowed!";
//   }
//   else
//   {
//     cout << "access denied!";
//     return 0;
//   }
//
// }

// ex4-1 사용자 두명의 나이를 물어 누가 더 연장자인지 알려주는 프로그램
int main()
{
  int age1, age2;

  cout <<"enter player1 and 2's age: ";
  cin >> age1 >> age2;
  if (age1>100 && age2>100)
  {
    cout << "wow they are very old!";
    return 0;
  }
  else
  {
    if (age1>age2)
    {
      cout << "player1 aged " << age1 << " is older by " << (age1-age2);
    }
    else if(age1==age2)
    {
      cout <<"they are the same!";
    }
    else
    {
      cout << "player2 aged " << age2 << " is older by" << (age2-age1);
      return 0;
    }
  }
}
