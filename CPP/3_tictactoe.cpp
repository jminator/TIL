#include <iostream>
#include <string>

using namespace std;

int n = 0;
string r1c1=".", r1c2 = ".", r1c3 = ".", r2c1 = ".", r2c2 = ".", r2c3 = ".", r3c1 = ".", r3c2 = ".", r3c3 = ".";

int n_row = 0;
int n_col = 0;
int i = 0;
int *iter = &i;

string mark = ".";
string playern ="1";

void printboard()
{
	cout << r1c1 << "\t" << r1c2 << "\t" << r1c3 << endl;
	cout << r2c1 << "\t" << r2c2 << "\t" << r2c3 << endl;
	cout << r3c1 << "\t" << r3c2 << "\t" << r3c3 << endl << endl;
}

void show_player(int n)
{
	int w_player = n % 2;

	enum players
	{
		player1 = 0,
		player2 = 1
	};

	switch (w_player)
	{
	case(player1):
	    mark = "O";
	    cout << "player 1's turn (" << mark << ") \n";

		break;
	case(player2):
	    mark = "X";
	    cout << "player 2's turn (" << mark << ") \n";
		break;
	}
}

int print_winner()
{
    printboard();
    cout << "\n" << "player " << playern << " wins!"<< "\n" << endl;
    r1c1=".", r1c2 = ".", r1c3 = ".", r2c1 = ".", r2c2 = ".", r2c3 = ".", r3c1 = ".", r3c2 = ".", r3c3 = ".";
    *iter = 1;
    return 0;
}

int check_winner(int i)
{
    if((r1c1 == r1c2 && r1c2 == r1c3)) // r1 match
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;

    if((r2c1 == r2c2 && r2c2 == r2c3)) // r2 match
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;

    if((r3c1 == r3c2 && r3c2 == r3c3)) // r3 match
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;

    if((r1c1 == r2c1 && r2c1 == r3c1)) // c1 match 
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;

    if((r1c2 == r2c2 && r2c2 == r3c2)) // c2 match 
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;
    if((r1c3 == r2c3 && r2c3 == r3c3)) // c3 match 
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;

    if((r1c1 == r2c2 && r2c2 == r3c3)) // diag left->right match 
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;

    if((r1c3 == r2c2 && r2c2 == r1c1)) // diag right->left match 
       {
         print_winner();
       }
    else
        n++;
        return *iter = 0;

}

int main()
{
	while(i==0)
    {

	printboard();

	show_player(n);

	if(n % 2 ==  0)
        {playern="1";}
	else playern="2";

	cout << "choose row: ";
	cin >> n_row;
	cin.ignore(1, '\n');

	cout << "choose column: ";
	cin >> n_col;
	cin.ignore(1, '\n');


	switch (n_row)
	{
	case(1) :
		switch (n_col)
		{
		case(1): r1c1 = mark;
			break;
		case(2):r1c2 = mark;
			break;
		case(3):r1c3 = mark;
			break;
		}
		break;
	case(2):
		switch (n_col)
		{
		case(1): r2c1 = mark;
			break;
		case(2):r2c2 = mark;
			break;
		case(3):r2c3 = mark;
			break;
		}
		break;
	case(3):
		switch (n_col)
		{
		case(1): r3c1 = mark;
			break;
		case(2):r3c2 = mark;
			break;
		case(3):r3c3 = mark;
			break;
		}
		break;
	}


	check_winner(i);

	}
return 0;
}
