#palindrome
palindrome =input("Enter a word : ")
reversed_word= palindrome[::-1]
if palindrome==reversed_word :
    print("The Input word is Palindrome")
else :
    print('Not A palindrome') 
