# 본초학_목차정리 파일의 내용을 정리하기 위한 코드입니다.

import re

with open("references/herb_index.txt", "r", encoding="UTF-8") as herb_index_file:
    herb_index_lines = herb_index_file.readlines()

herb_index_list = []

for line in herb_index_lines:
    herb_index_list.append(line.split())
    # print(line.split())
  
# print(herb_index_list)

for line in herb_index_list:
    if len(line) != 0:
        # ChatGPT 코드 참고해서 작성하기
        pass
    

# 아래가 ChatGPT 코드

import re

def check_data_type(text):
    # Define a regular expression pattern to match numbers with multiple periods
    pattern = r'\d+(\.\d+)+'

    # Use the re.search() function to find the pattern in the text
    match = re.search(pattern, text)

    if match:
        # If a match is found, it's data with numbers and multiple periods
        return "Data with numbers and multiple periods"
    else:
        # If no match is found, it's data with numbers and a single period
        return "Data with numbers and a single period"

# Example usage:
text1 = "This is 1. a sample text."  # Data with numbers and a single period
text2 = "This is 1.1. a sample text."  # Data with numbers and multiple periods

result1 = check_data_type(text1)
result2 = check_data_type(text2)

print(result1)  # Output: Data with numbers and a single period
print(result2)  # Output: Data with numbers and multiple periods
