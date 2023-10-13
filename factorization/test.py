import re


def extract_parts(list_data):
    korean_list = []
    chinese_list = []
    english_list = []

    for text in list_data:

        korean_part = ''
        chinese_part = ''
        english_part = ''
        current_part = ''

        # 정규 표현식을 사용하여 문자가 한글, 영어, 또는 한자인지 판별
        for char in text:
            if re.match(r'[ㄱ-ㅎ가-힣]', char):
                korean_part += char
            elif re.match(r'[a-zA-Z]', char):
                english_part += char
            elif re.match(r'[\u4e00-\u9fff]', char):
                chinese_part += char
            current_part += char

        korean_list.append(korean_part)
        chinese_list.append(chinese_part)
        english_list.append(english_part)

    return korean_list, chinese_list, english_list


print(extract_parts(['인삼(人蔘)', '복령(茯苓)', '백출(白朮)', '감초(甘草)']))