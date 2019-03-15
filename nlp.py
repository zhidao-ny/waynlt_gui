from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import os
import codecs
import math
import operator
import sqlite3
import nltk

  """
  Input:
   topic:      key word (string)
   db:         database of the data (string)
   table:      table of the data (string)
   score_func: the method to calculate the score of the input
  Return:
   score: (compound score, positive score, neutral score , negtive score)
  """
  def sentiment(topic,db="data/twitter.db",table="tweets",score_func=analyzer, self):
     
      analyzer = SentimentIntensityAnalyzer().polarity_scores
      connection = sqlite3.connect(db)
      cursor = connection.cursor()
      cursor.execute("SELECT text FROM {table};".format(table="tweets"))
      results = cursor.fetchall()
      i = 0
      neg = 0
      compound = 0
      pos = 0
      neu = 0
      for r in results:
          if topic in r[0]:
              # print(r[0],score_func(r[0]))
              i += 1
              compound += score_func(r[0])["compound"]
              pos += score_func(r[0])["pos"]
              neu += score_func(r[0])["neu"]
              neg += score_func(r[0])["neg"]
      if i > 0:
          return {"compound":(compound/i), "pos":(pos/i), "neu":(neu/i), "neg":(neg/i)}
          print("compound: %.2f" % (compound/i))
          print("pos:      %.2f" % (pos/i))
          print("neu:      %.2f" % (neu/i))
          print("neg:      %.2f" % (neg/i))
      else:
          return null, null, null, null
          print("no record with keyword:", topic)
      #print(i)
      cursor.close()
      connection.close()
