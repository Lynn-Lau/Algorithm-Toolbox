### Algorithmic Toolbox

​        文件夹中是关于公开课[Coursera](https://www.coursera.org/)中的课后作业代码，涉及到的[数据结构和算法](https://www.coursera.org/learn/data-structures/home/welcome)的系列公开课，开课学校是*UC, San Diego*。

​        首先介绍的是算法的运行时间和压力测试，并布置课后作业。

#### 1.  The First Week

第一周主要对课程进行介绍，然后举例。

* 给定一个数列，在数列中寻找两个数是的其乘积大于任何其他一对数字乘积。

  * 要求Python程序的运行时间小于5s；
  * 要求内存占用量小于一定的内存量，512M；

  通过Python代码实现：

  [Calculate the SubPairwise Product](https://github.com/Lynn-Lau/Algorithm-Toolbox/blob/master/MaxSubArrayProduct.py);


#### 2. The Second Week

第二周，通过Fibonacci数列、最大公约数(*Greatest Common Divisor, GCD*)、最小公倍数(*Least Common Multiple, LCM*)等对*Naive*, *Smart*算法进行对比介绍，以及通过大O来表示算法的运算复杂度。

* [Fibonacci数](https://github.com/Lynn-Lau/Algorithm-Toolbox/blob/master/2nd%20week/01_Codes/fibonacci/myfib.py)，返回第n阶Fibonacci数。要求n阶Fibonacci数的n的范围在0~50 。

* 计算[Fibonacci数的最后一个数字](https://github.com/Lynn-Lau/Algorithm-Toolbox/blob/master/2nd%20week/01_Codes/fibonacci_last_digit/fibonacci_last_digit%20.py)，要求Fibonacci数比较大，比如23655阶Fibonacci数的最后一位数字。

  *Sample* 1

  ```python
  Input: 239
  Output: 8
  ```

* [最大公约数](https://github.com/Lynn-Lau/Algorithm-Toolbox/blob/master/2nd%20week/01_Codes/gcd/mygcd.py)，最大公约数的计算方法使用的是辗转相除法。

  原理：已知a, b, c为三个正整数，若a除以b余数为c，那么（a, b）=（b, c）

  ​            即gcd(a, b) = gcd(b, (a mod b))，当gcd( , )中第二个数为0时，第一个数便是

  ​            a, b的最大公约数。

  要求能够在上面约定的时间和内存占用范围内能够计算出任给两个数的最大公约数。

  *Sample* 1

  ```python
  Input:18 35
  Output:1
  ```

  *Sample* 2

  ```python
  Input: 28851538 1183019
  Output:17657
  ```

* [最小公倍数](https://github.com/Lynn-Lau/Algorithm-Toolbox/blob/master/2nd%20week/01_Codes/lcm/least_common_multiple.py)， 求最小公倍数的方法是两个正整数a, b相乘得到的乘积除以a, b的最大公约数得到的数就是a, b的最小公倍数。

  *Sample* 1

  ```python
  Input:6 8
  Output:24
  ```

  *Sample* 2

  ```python
  Input:28851538 1183019
  Output:1933053046
  ```

  ​

