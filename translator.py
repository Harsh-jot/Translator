#An application to help translate between languages

from googletrans import Translator statement=str(input("Statement:")); 
#translator 
translator=Translator(); 
#translating the statement 
translated_statement=translator.translate(statement,src='en',dest='language in which you want to translate the statement'); 
#to print the 
translated statement print(translated_statement.text);
