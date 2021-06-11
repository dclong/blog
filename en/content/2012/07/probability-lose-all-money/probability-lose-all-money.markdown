UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Probability to Lose All Money
Date: 2012-07-22 03:56:28
Tags: cache, C++, simulation, statistics, map, probability, recursive, condition, fun problems, hash table, money, lose
Category: Fun Problems
Slug: probability-lose-all-money
Author: Ben Chuanlong Du
Modified: 2015-11-22 03:56:28

[mitbbs]: http://www.mitbbs.com/

<img src="http://www.legendu.net/media/object/money-1.jpeg"
width="240" height="200" align="right" />

A few days ago I found someone asking an interview questions on [mitbbs][].
The question is as follows. 
A gambler plays a fair game and bet 1 dollar each time. 
If he lose all his money, 
the game stops. 
Suppose he has 10 dollars and is only allowed to play 50 rounds at most, 
what is the probability that he lose all his money?

This is a problem of random work. 
I am pretty sure that there are very neat solutions to 
this problem using *reflection*. 
However, 
as I mentioned in my book *Statistics Thinkings*, 
there is a universal way to solve this kind of problems. 
The key is to find a recursive forumula using conditional expectation/probability. 
First, 
we can generalize the problem to the following one. 
A gamber palys a fair game and bet 1 dollar each time. 
If he lose all his money, 
the game stops. 
Suppoe he has $m_0$ dollars and is only allowed to play $k$ rounds at most,
what is the probability that he end up with $m$ dollars?

Let's use $P_{n,m}$ to stand the probability 
that the player end up with $m$ dollars after $n$ steps. 
Conditioning on step $n-1$, 
we have
$$
P_{n,m} = 0.5 P_{n-1,m+1} + 0.5 P_{n-1,m-1} I(m>1)
$$
with initial condition 
$$
P_{0,m} = I(m=m_0),
$$
where $I$ is the indicator function. 
As I mentioned in my book *Statistics Thinkings* and other similar posts on my blog,
there are several ways (e.g., moment generating function) to solve for $P_{n,m}$. 
A pratical way is write a program to do this. 

I recently learned C++11, so I wrote a program in C++11 to solve this problem just for practice. 
The core code is just a recursive function. 
Though recursive algorithms are convenient, they are usually not efficient. 
A simple way to improve the speed of recursive algorithm is to use cache. 
In my code, I used a ordered map to store previous calculated probabilities 
to avoid duplicated computations. Since the code uses the standard library of C++11, 
it has to be compiled with option `-std=c++0x`. 
```C++
#include<iostream>
#include<string>
#include<map>
using namespace std;

string key(int init_money, int step, int final_money){
return to_string(init_money) + '-' + to_string(step) + '-' + to_string(final_money);
}

double hit_probability(int init_money, int step, int final_money){
    static map<string,double> hp_table;
    string hp_key = key(init_money,step,final_money);
    auto i = hp_table.find(hp_key);
    if(i!=hp_table.end()){
        return i->second;
    }
    if(step==0){
        if(final_money==init_money){
            hp_table[hp_key] = 1;
            return 1;
        }
        hp_table[hp_key] = 0;
        return 0;
    }
    double p = 0.5 * hit_probability(init_money, step - 1, final_money + 1);
    if(final_money>1){
        p += 0.5 * hit_probability(init_money, step - 1, final_money - 1);
    }
    hp_table[hp_key] = p;
    return p;
}

double lose_probability(int init_money, int step){
    double p = 0;
    for(int i=0; i<=step; ++i){
        p += hit_probability(init_money,i,0);
    }
    return p;
}

int main(){
    int init_money;
    int step;
    double p;
    cout<<"Please type in the initial amount of money:"<<endl;
    cin>>init_money;
    cout<<"Please type in the stop step:"<<endl;
    cin>>step;
    p = lose_probability(init_money,step);
    cout<<"The probablity to lose all money is: "<<p<<endl;
}
```
