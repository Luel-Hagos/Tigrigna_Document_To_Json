#import requerd libraries
import docx2txt  # for working with docx and texts
import zipfile   #for zip files
import json      # for  json files
import re        # for regular expressions

#The name of the output json file
output_fileName = 'ETL_SAMPLE_DICT01.json'   # variable for the output json file name
update_fileName = 1                          # for creating another name file


#changes document format to text format and returns as text format
def docx_to_text(document):
	text = docx2txt.process(document)
	return text


#removes meaningles characters( like tabes,xa0 and others)
#and returns adjusted (meaningful) text
def remove_trash_and_make_adjusment(text):
	text=re.sub(r'(\t)+|(\d\.)|(\xa0)',r'',text)          #replace tabes,xa0, and meaningless digits by empty
	text = re.sub(r'(\[\ተመፍ\])|(\[\ተፃፍ\])',r',',text)   #replace [ተመፍ] & [ተፃፍ] by ',' since they indicate for multi meaning
	adjusted_text = re.split(r"\n+", text)
	return adjusted_text


#mergs meanings of the same word separeted by ',' to one 
#and returns  update of the adjusted_text
def merge_multi_meanings(adjusted_text):
	upadate_adjusted_text = []
	if len(adjusted_text[0]) == 1:
		adjusted_text = adjusted_text[1:]
	else:
		adjusted_text = adjusted_text[:]
	m_meaning = ''
	types = ['-ሓግ-','-ግ-','-ተሳግ-','-ስ-','-ቅ-','-ዘይግ-','-ብሂ-','-ቃኣ-','-ተወግ-','-ተሳግ-','-ኣበሃ-']
	for i in range(len(adjusted_text)):
		if any(typ in adjusted_text[i] for typ in types):  
			if m_meaning != '':
				upadate_adjusted_text.append(m_meaning)
			upadate_adjusted_text.append(adjusted_text[i])
			m_meaning = ''
		else:
			m_meaning += ',' + adjusted_text[i]   #concatnate by ',' for multi meaning of the same word 
	upadate_adjusted_text.append(m_meaning)
	return upadate_adjusted_text


#checks for multiple meaning of the same word from upadate_adjusted_text that are separated by '፣' 
#and returns the updated one
def check_multi_meaning_and_merge(merged):
	multi_merged = []
	for i in merged:
		if '፣' in i:
			tempv = i[:]
			lower = 0
			count =tempv.count('፣' )
			for q in range(count):
				index = tempv.index('፣',lower,len(i))
				if '('  in i[lower:index] and ')'  in i[lower:index] or '(' not in i[lower:index] and ')' not in i[lower:index]:
					tempv = tempv[:index] + ',' + tempv[index+1:]
					lower = index
			multi_merged.append(tempv)
		else:
			multi_merged.append(i)
	return multi_merged


# mergs all words , types and meanings with thier respective values in dictionary format
# makes some adjusmens 
# and return all together
def merge_all(mult_merged):
	output = []
	for index in range(0, len(multi_merged)-1, 2):
		first = mult_merged[index]           #contains word and type 
		second = mult_merged[index + 1]      #contains the meaning
		tempi = first.index('-')
		type = first[tempi:]
		word = first[:tempi]
		if "[" in word:        
			tempi1 = word.index("[")
			word = word[:tempi1]
		if "=" in word:
			tempi1 = word.index("=")
			word = word[:tempi1]
		if '/' in word:
			tempi1 = word.index("/")
			word = word[:tempi1]
		type = type.strip("-") 
		meaning = [sentence.strip() for sentence in second.split(",")]
		output.append({"word": word, "type": type, "meaning": meaning[1:]})
	return output


# chenges the dictionary to JSON structure and saves it as .json file
def to_json_text(output):
	with open(output_fileName, 'w', encoding='utf8') as json_file:
		json.dump(output,json_file, indent=4, ensure_ascii=False)
	json_file.close()

	
# All methods of the problem
# 1st it unzips 'ETL_SAMPLE_DICT.zip'
# then it access the documents inside the zip file
# finally for each documents inside the zip file it performs an operation by calling the respective methods 
zip_file = zipfile.ZipFile('ETL_SAMPLE_DICT.zip','r')       #create zip object
zip_file.extractall()                                        #extract the zipped file
for document in zip_file.namelist():
	text = docx_to_text(document)
	adjusted_text = remove_trash_and_make_adjusment(text)
	upadate_adjusted_text=merge_multi_meanings(adjusted_text)
	multi_merged=check_multi_meaning_and_merge(upadate_adjusted_text)
	output=merge_all(multi_merged)
	output_fileName = 'ETL_SAMPLE_DICT0' + str(update_fileName) + '.json'
	update_fileName += 1      
	to_json_text(output)
zip_file.close()