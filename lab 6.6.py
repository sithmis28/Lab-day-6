text=input("enter a string:")
vowels="aeiouAEIOU"
vowel_count=0
count=0
while count<len(text):
    if text [count] in vowels:
        vowel_count=vowel_count+1
    count=count+1
print("total number of vowel",vowel_count)
