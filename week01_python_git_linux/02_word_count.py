text = "hello world hello python world ai edge ai"
words = text.split()

print("Original text:")
print(text)
print("words:")
print(words)
print("_"*20)

word_count = {}
for word in words:
    if word in word_cousnt:#注意if这里要加:
        word_count[word]+=1
    else:
        word_count[word]=1

print("word count results:")
for word, count in word_count.items():#在字典里把word和count拆开，分包，然后复制给变量word和count
    print(f"{word}: {count}")#f"{word}"，问的是word变量里面是什么；word_count[word]，表示word这个变量对应的东西，在word_count字典里查到什么