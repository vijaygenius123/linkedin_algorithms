"""
Author: Vijayaraghavan Sundararaman
Date : 02/Nov/2019
Desc : Find GCD Of A Number
"""

"""
 
 .______   .______        ______   .______    __       _______ .___  ___. 
 |   _  \  |   _  \      /  __  \  |   _  \  |  |     |   ____||   \/   | 
 |  |_)  | |  |_)  |    |  |  |  | |  |_)  | |  |     |  |__   |  \  /  | 
 |   ___/  |      /     |  |  |  | |   _  <  |  |     |   __|  |  |\/|  | 
 |  |      |  |\  \----.|  `--'  | |  |_)  | |  `----.|  |____ |  |  |  | 
 | _|      | _| `._____| \______/  |______/  |_______||_______||__|  |__| 

 Find the greatest common denominator of two numbers using Euclids Algorithm                                                                       
 
"""

"""
 
      ___       __        _______   ______   .______       __  .___________. __    __  .___  ___. 
     /   \     |  |      /  _____| /  __  \  |   _  \     |  | |           ||  |  |  | |   \/   | 
    /  ^  \    |  |     |  |  __  |  |  |  | |  |_)  |    |  | `---|  |----`|  |__|  | |  \  /  | 
   /  /_\  \   |  |     |  | |_ | |  |  |  | |      /     |  |     |  |     |   __   | |  |\/|  | 
  /  _____  \  |  `----.|  |__| | |  `--'  | |  |\  \----.|  |     |  |     |  |  |  | |  |  |  | 
 /__/     \__\ |_______| \______|  \______/  | _| `._____||__|     |__|     |__|  |__| |__|  |__| 

    In README.md                                                                                      
"""


def gcd(num1, num2):
    """ Find the greatest common denominator

    Args:
        num1: The first number for which we want to find GCD
        num2: The second number for which we want to find GCD

    Returns: 
        gcd : the greatest common denominator for the two numbers provided
    """

    if(num1 <= 0 | num2 <= 0):
        print("Please ensure both number are greater than 0")

    else:
        while(num2 != 0):
            temp = num1
            num1 = num2
            num2 = temp % num2

        return num1


if __name__ == '__main__':
    print(gcd(60, 96))
