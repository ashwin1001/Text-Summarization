#Program to find summary and related rouge scores
import networkx as nx
import math as m
import sys
from rouge import Rouge
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
import nltk
nltk.download('punkt')
ps=PorterStemmer()
node=""
summarylines=0
k=0
listfinal=[]
score=0
list3=[]
t1=""
t2=""
t=()
numsentence=0
p=()
G = nx.DiGraph()#creating graph data structure for forward variant 
G2=nx.DiGraph()#creating graph data structure for backward variant
numlines=0
sentence1=""
sentence2=""
sentence=[]
l1=[]
l2=[]
lenedges=0
with open(sys.argv[1],'r') as f: #opening the input txt file
  line=f.read() 
			
  line.strip()
  sentence = line.split(".")  #splitting the sentences
  #print sentence
  for j in range(0,len(sentence)-1):
   #print sentence[j]
   G.add_node(sentence[j].lower())# adding nodes in the graph for forward variant
   G2.add_node(sentence[j].lower())# adding nodes in the graph for backward variant
   numlines+=1#counting number of lines
  
  
#print G.nodes()[0]
#print G.nodes()[1]  
#print G.nodes()[2]  
#print G.nodes()[3]    
#print numlines
summarylines=sys.argv[2]
#for m in range(1,numsentence):
# list1=(G.nodes()[m]).split(" ")
# list2=len(list1)
# list3.insert(m,list2)
#print list3'''
#for i in range(0,numlines):
# if G.nodes[i]=='\n':
#  del G.nodes[i]
#print G.nodes()
#print summarylines
for k in range(0,numlines):
 g1=[]
 sentence1=""
 sentence1=G.nodes()[k]
 p1=sentence1
  
 
 stop_words = set(stopwords.words('english'))#forming a set of the stopwords
 
 word_tokens = word_tokenize(p1)
 
 filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
 filtered_sentence = []
 
 for w in word_tokens:
  if w not in stop_words:
   filtered_sentence.append(w)#sentence after removing stopwords
 
 
 #print sentence1
# l1=[]
# l1=p1.split()
 for w in filtered_sentence:
  g1.append(ps.stem(w))
 n1=len(g1)
 #print l1
 for i in range(k+1,numlines):
    g2=[]
    sentence2=""
    sentence2=G.nodes()[i]
    #print sentence2
    p2=sentence2
    stop_words = set(stopwords.words('english'))#forming a set of the stopwords
 
    word_tokens = word_tokenize(p1)
 
    filtered_sentence2 = [w for w in word_tokens if not w in stop_words]
 
    filtered_sentence2 = []
 
    for w in word_tokens:
     if w not in stop_words:
      filtered_sentence2.append(w)#sentence after removing stopwords
    for w in filtered_sentence:
     g2.append(ps.stem(w)) 
    l2 = []
    l2=p2.split(" ")
    #print l1,l2
    n2=len(g2)
    #print l1
    intersection=set(g1) & set(g2)#finding common words between two sentences
    #print intersection
    n=len(intersection)
    #print n
    #print k,j
   # print k,i
    
    calculation=n/(m.log(n1)+m.log(n2))#calculating similarity scores
    
    if n!=0:
     #print calculation
     G.add_edge(sentence1,sentence2,weight=calculation)#forming weighted edges between nodes
  
        
 n=0
lenedges=len(G.edges())
 
#print lenedges
#print G.nodes()
#for i in range(0,numlines):
#pagerank(G.nodes()[0])
print "                      BY FORWARD VARIANT                "
print "--------------------------------------------------------------"
pr=nx.pagerank(G,alpha=0.9)#pagerank function call
#print pr
listfinal=sorted(pr,key=pr.get)
#print type(summarylines)

for i in range (numlines-1,numlines-int(summarylines)-1,-1):
 print listfinal[i]#printing summary of desired no of lines


listfinal_str= ''.join(map(str,listfinal))
#print(type(listfinal_str))

with open(sys.argv[3], 'r') as myfile:
    data=myfile.read().replace('\n', '')
#print(type(data)) 
#Rouge score calculation for forward variant   
print "_________________Rouge Score for backward variant _________________________"
rouge = Rouge()
scores = rouge.get_scores(listfinal_str,data)
print scores
for k in range(0,numlines):
 g1=[]
 sentence1=""
 sentence1=G2.nodes()[k]
 p1=sentence1
  
 
 stop_words = set(stopwords.words('english'))#forming set of the stopwords
 
 word_tokens = word_tokenize(p1)
 
 filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
 filtered_sentence = []
 
 for w in word_tokens:
  if w not in stop_words:
   filtered_sentence.append(w)#sentence after removing stopwords
 for w in filtered_sentence:
  g1.append(ps.stem(w))
 
 #print sentence1
# l1=[]
# l1=p1.split()
 
 n1=len(g1)
 #print l1
 for i in range(k+1,numlines):
    g2=[]
    sentence2=""
    sentence2=G2.nodes()[i]
    #print sentence2
    p2=sentence2
    stop_words = set(stopwords.words('english'))#forming set of the stopwords
 
    word_tokens = word_tokenize(p1)
 
    filtered_sentence2 = [w for w in word_tokens if not w in stop_words]
 
    filtered_sentence2 = []
 
    for w in word_tokens:
     if w not in stop_words:
      filtered_sentence2.append(w)#sentence after removing stopwords
 
    l2 = []
    l2=p2.split(" ")
    for w in filtered_sentence:
     g2.append(ps.stem(w))
    #print l1,l2
    n2=len(g2)
    #print l1
    intersection=set(g1) & set(g2)#finding common words between two sentences
    #print intersection
    n=len(intersection)
    #print n
    #print k,j
   # print k,i
    
    calculation=n/(m.log(n1)+m.log(n2))#calculating similarity scores
    
    if n!=0:
     #print calculation
     G2.add_edge(sentence2,sentence1,weight=calculation)#adding weighted edges between nodes
  
        
 n=0
lenedges=len(G.edges())
 
#print lenedges
#print G.nodes()
#for i in range(0,numlines):
#pagerank(G.nodes()[0])
print "                       BY BACKWARD VARIANT                     "
print "_____________________________________________________________"
pr=nx.pagerank(G2,alpha=0.9)#running pagerank algorithm
#print pr
listfinal=sorted(pr,key=pr.get)
#print type(summarylines)
for i in range (numlines-1,numlines-int(summarylines)-1,-1):
 print listfinal[i] 
listfinal_str=""
listfinal_str= ''.join(map(str,listfinal))
#print(type(listfinal_str))
data=""
with open(sys.argv[3], 'r') as myfile:
    data=myfile.read().replace('\n', '')
#print(type(data))     
#print G.edges()
#print (G.has_edge(1,0)) 
#Rouge score calculation for backward variant 
print "_________________Rouge Score for backward variant __________________"
rouge = Rouge()
scores = rouge.get_scores(listfinal_str,data)
print scores
     
       
	    
	    
