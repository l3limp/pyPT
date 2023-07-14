import os
import shutil
import sys

from langchain.chat_models import ChatOpenAI

import constants
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]
print(query)
repoName = query.split('/')[-1]
print(repoName)
os.system(f"cd dirs && git clone {query}")



# loads just one file
# loader = TextLoader('data.txt')

# loads a directory
loader = DirectoryLoader(f"./dirs/{repoName}", glob="*.dart")
index = VectorstoreIndexCreator().from_loaders([loader])

# print(index.query(query))
# print(index.query(query, llm=ChatOpenAI()))
while(True):
    q = input("Enter a ques: \n")
    if(q == "EXIT"):
        # shutil.rmtree(f"./{repoName}")
        # os.system("pwd")
        os.system(f"rmdir /S /Q .\dirs\{repoName}")
        # os.rmdir(".\dirs")
        break

    # print(index.query(q, llm=ChatOpenAI(temperature=0.2)))
    print(index.query(q))
