"""
You have to sort the inner content of every word of a string in descending order.

The inner content is the content of a word without first and the last char.

Some examples:

"sort the inner content in descending order"  -->  "srot the inner ctonnet in dsnnieedcg oredr"
"wait for me"        -->  "wiat for me"
"this kata is easy"  -->  "tihs ktaa is esay"
Words are made up of lowercase letters.
The string will never be null and will never be empty.
words will be separated by a single space character
the string will have neither leading nor trailing spaces
Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""

def sort_the_inner_content(words):
    words_list = words.split(" ")
    result = []

    for word in words_list:
        if len(word) > 2:
            reversed_inner_content = "".join(sorted(word[1:-1], reverse=True))
            result.append(word[0] + reversed_inner_content + word[-1])
        else:
            result.append(word)

    return " ".join(result)
