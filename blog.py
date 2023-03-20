import string
import pyperclip
blog = pyperclip.paste() 
with open('blog.txt','w') as b:
   b.write(blog)
# open both files
word1 = 'πλατυποδια'
word2 = 'πλατυποδία'
word3 = 'παθηση πλατυποδια'
link1 = 'https://www.christou1910.com/paidiki-platypodia-antimetopiste/'

word4 = 'πάτοι για πλατυποδία'
word5 = 'πατοι για πλατυποδια'
word7 = 'πάτοι για πλατυποδια'
link2 = 'https://www.christou1910.com/product/anatomikoi-patoi-gia-paidia/'

word8 = 'πατοι σιλικονησ'
word9 = 'πάτοι σιλικόνησ'
word10 = 'πάτοι σιλικονησ'
link3 = 'https://www.christou1910.com/product/anatomikoi-patoi-silikonis/'

word11 = ''
word12 = ''
word13 = ''
word14 = ''
newblog=blog.replace(word1,"lol")
with open('second.html','a') as Edblog:
    Edblog.write(newblog)



















# for single word
# for word in line.split():
