#Задание 3
def longest_words(file):
    with open(file, 'r') as tt:
        a = tt.read()
    wrds = a.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
print(longest_words('article.txt'))
  
#Задание 4
def text_editor():
    file_name = input()
    file_name += '.txt'
    with open(file_name, 'w') as t:
        while True:
            l = input()
            if l.strip() == '' or not l.isprintable():
                break
            t.write(l + '\n')
text_editor()
