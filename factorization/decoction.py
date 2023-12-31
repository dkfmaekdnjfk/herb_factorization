#######################################
### !!! 주석 작성을 일상화합니다 !!! ###
#######################################


### STATUS 사용법
# -- 특정 STATUS에서는 적용 후 바로 예외처리로 에러를 발생시켜 알고리즘을 종료시킵니다.
# -- 정상 STATUS은 도중에 현재 어떤 상태인지를 체크하기 위해 사용합니다.


### 주석 작성 규칙 ###

# 코드에 대한 해설으로, 단순 주석을 기입합니다.
# N. 초기 계획에 따른 알고리즘의 논리 순서입니다.
# NA. 초기 계획에서 중간에 추가된 알고리즘의 논리 순서입니다. 
# **PLAN** 코드를 작성할 계획을 작성합니다.
### YYMMDD IDEA : 해당 일자에 생각한 아이디어를 기록합니다.


### 에러 코드 규칙 ###
# 0 : 입력값 없음

# -------------------------------------------------------- #

import pandas as pd
import numpy as np
import re

# -------------------------------------------------------- #

class HerbMedicine:
    # 입력된 처방을 인스턴스화하는 클래스입니다.
    def __init__(self, name=None, source=None, indication=None, effect=None, note=None, composition=None, factorization=None):
        # 처방명, 출전, 주치, 효능, 비고, 구성, 인수분해
        self.name = name
        self.source = source
        self.indication = indication
        self.effect = effect
        self.note = note
        # **PLAN** 입력된 내용들을 하나하나 분리해서 리스트로 저장하도록 작성해야 합니다.

        self.composition = self.save_list(composition) if composition is None or not isinstance(composition, list) else composition
        self.factorization = None

    # 국문, 한자, 라틴어, 영문으로 입력된 처방명을 상호적으로 사용할 수 있도록 하는 함수
    # 입력받은 리스트를 저장할 때 요소가 괄호가 있다면 괄호를 분해하고 한글과 한자 중 하나만 저장하는 함수
    def input_normalization(list_data):
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

    def save_list(self, composition):
        # composition을 알맞은 형식으로 저장하기 위해 사용되는 함수입니다.
        # Split the text using a comma as the delimiter
        text_list = composition.split(', ')
        return text_list

    # **PLAN** 입력한 내용을 조작하는 함수만 본 클래스에 제작합니다.
    # list를 넘파이 배열로 저장하는 함수
    def list_to_numpy(self, list_data):
        numpy_array = np.array(list_data)
        return numpy_array

    # 개발예정) 속성들을 활용해서 내용을 정리하여 출력하는 함수


class HerDataBase:
    # 데이터베이스를 클래스로 인스턴스화합니다.
    # 개발자의 능력 부족으로 현재로서는 이 편이 편하기 때문에 이렇게 하는 것이지만,
    # 실제 데이터베이스를 연결할 때에는 다른 방법을 고안해야 합니다.
    def __init__(self, address, factorization_sheet=None, decoction_sheet=None, basic_sheet=None, herb_sheet=None):
        # 인수분해 결과 시트, 처방구성 시트, 기본 시트, 약재 시트
        self.address = address
        self.factorization_sheet = factorization_sheet
        self.decoction_sheet = pd.read_excel(self.address, sheet_name="처방")
        self.basic_sheet = pd.read_excel(self.address, sheet_name="기본")
        self.herb_sheet = pd.read_excel(self.address, sheet_name="약재")

    # 개발예정) 입력받은 리스트를 저장할 때 요소가 괄호가 있다면 괄호를 분해하고 한글과 한자 중 하나만 저장하는 함수

    # **PLAN** 검색과 관련한 모든 함수를 본 클래스에 제작합니다.

    def addrest_check(self):
        # 입력받은 주소가 올바른 주소인지 확인하는 함수. : 아래 내용이 올바르게 지정되어 있는지 확인합니다.
          # - 파일형식 : 엑셀, 스프레드시트
          # - 시트구성 : 인수분해, 처방구성, 기본, 약재
          # - 열  구성 : 이름, 출전, 주치, 효능, 비고, 구성, (인수분해)    
        return True


    # 각 sheet를 넘파이 배열로 저장하는 함수
    def sheet_to_numpy(self, pandas_data):
        # 대분류, 소분류, 처방명, 출전, 주치, 효능, 비고, 구성, 인수분해
        numpy_array = pandas_data.to_numpy()
        header = np.array(['대분류', '소분류', '이름', '주치', '효능', '출전', '비고', '구성', '한문명'])
        numpy_data = np.vstack((header, numpy_array))
        return numpy_data


    # 개발예정) 처방명을 저장소에서 검색하는 함수
    def find_decoction_name(self):
        raise Exception("제작되지 않은 함수입니다.")


    # 데이터베이스에서 입력한 데이터에 포함되는 기본방이 있는지 검색하는 함수
    # 제공한 비율을 기준으로 포함 여부를 계산합니다.
    # 제공한 처방구성을 DB를 바탕으로 기본방의 포함 여부를 넘파이 배열로 출력합니다.
    # 처방명, 구성, 포함여부, 주치, 효능, 출전
    def basic_search(self, composition_numpy, ratio):
        # composition_numpy는 제공한 처방구성을 넘파이 어레이로 변경한 것으로, HerbMedicine 클래스에서 제작한 구성입니다.
        # 처방명, 구성, 포함여부, 효능, 주치를 인덱스로 하는 빈 넘파이 배열을 선언합니다.
        factorization_decoction = np.array(['name', 'composition', 'TrueOrFalse', 'indication', 'effect', 'source'], dtype=object)

        # 8번째 열이 구성이므로 DB의 basic_np에서 8번째 열을 가져와 새로운 넘파이 배열로 저장합니다.        
        basic_np = self.sheet_to_numpy(self.basic_sheet)
        basic_sheet = basic_np[1:, :]           # DB

        for line in basic_sheet:
            basic_list = line[7].split(', ')
            # 제공한 처방구성의 구성들 중에 기본방의 구성 리스트에 있는지를 확인합니다. True/False로 반환합니다.
            result = [element in composition_numpy for element in basic_list]
            # 리스트에서 True의 비율을 계산합니다.
            true_percentage = (sum(result) / len(result)) * 100

            # **PLAN**
            # 1. True가 절반 이상 있는지 확인합니다.
            if true_percentage >= ratio:
            # 2. 절반 이상 있다면 해당 처방의 이름과 포함된 약재, 포함되지 않은 약재를 저장합니다.
                name = line[2]
                composition = line[7].split(', ')
                trueorfalse = result
                indication = line[3]
                effect = line[4]
                source = line[5]
                
                new_data = np.array([name, composition, trueorfalse, indication, effect, source], dtype=object)

                ### 230925 IDEA : 넘파이 배열로 저장해서 원하는 정보를 쉽게 가져오도록 합니다.
                # Add the new row to the last row of the existing array
                factorization_decoction = np.vstack((factorization_decoction, new_data))
        
        return factorization_decoction

    # basic_search 함수로 출력된 넘파이 배열의 인수분해 결과를 제공한 처방구성의 넘파이 배열과 함께 조작합니다.
    def herb_info_search(self, factorization_decoction, composition_numpy):    
        # 처방명, 구성, 포함여부, 주치, 효능
        Name = factorization_decoction[1:, 0]
        Composition = factorization_decoction[1:, 1]
        TrueOrFalse = factorization_decoction[1:, 2]
        Indication = factorization_decoction[1:, 3]
        Effect = factorization_decoction[1:, 4]
        Source = factorization_decoction[1: 5]

        herb_np = self.sheet_to_numpy(self.herb_sheet)
        herb_sheet = herb_np[1:, :]             # DB

                # 2.1. 포함된 약재들과 포함되지 않은 약재들의 '비고' 정보를 '약재' 시트에서 가져와 저장합니다.
        herb_in = {}        # 포함된 약재 리스트
        herb_out = {}       # 포함되지 않은 약재 리스트
        herb_else = {}      # 나머지 추가해야 할 약재 리스트
        
        # 포함된 처방 및 구성 딕셔너리
        decoction_in = {}
        for i in range(Name.shape[0]):
            decoction_in[Name[i]] = Composition[i]

        # **PLAN**
        # trueorfalse 열에서 T/F 리스트를 찾아내고
        for i in range(TrueOrFalse.shape[0]):
            trueorfalse = TrueOrFalse[i]
            composition = Composition[i]
            # trueorfalse에서 true인 경우에 해당하는 해당 행의 composition 열에서 약재들을 고르고
            for i in range(len(trueorfalse)):
                if trueorfalse[i] == True:
                    herb_in[composition[i]] = ""
                else:
                    herb_out[composition[i]] = ""

        # 고른 약재들을 약재 시트에서 찾아내어서
        # 대분류, 소분류, 처방명, 출전, 주치, 효능, 비고, 구성, 인수분해
        Herb_Name = herb_sheet[:, 2]
        Herb_Composition = herb_sheet[:, 7]
        Herb_Indication = herb_sheet[:, 3]
        Herb_Effect = herb_sheet[:, 4]
        Herb_Info = herb_sheet[:, 6]
        Herb_Source = herb_sheet[:, 5]

        # 찾아낸 약재와 대응되는 비고 정보를 가져와서
        # 약재 이름과 함께 저장합니다.
        for i in range(Herb_Name.shape[0]):
            herb = Herb_Name[i]
            for key in herb_in.keys():
                if herb == key:
                    ### 231013 효능, 주치, 비고 정보를 모두 가져옵니다.
                    herb_in[key] = [ Herb_Effect[i], Herb_Indication[i], Herb_Info[i] ]

        for i in range(Herb_Name.shape[0]):
            herb = Herb_Name[i]
            for key in herb_out.keys():
                if herb == key:
                    ### 230927 IDEA 현재 비고 정보가 완성되지 않아 '효능' 정보를 가져옵니다.
                    herb_out[key] = [ Herb_Effect[i], Herb_Indication[i], Herb_Info[i] ]

            # 3. 기본방에서 포함된 것으로 판단된 약재들을 제외하고 남는 약재를 추려냅니다.
        herb_else_name = [name for name in composition_numpy if name not in herb_in]
        for i in range(Herb_Name.shape[0]):
            herb = Herb_Name[i]
            for key in herb_else_name:
                if herb == key:
                # 3.1. '약재' 시트에서 해당 약재들의 '비고' 정보를 가져옵니다.
                ### 230927 IDEA 현재 비고 정보가 완성되지 않아 '효능' 정보를 가져옵니다.    
                    herb_else[key] = [ Herb_Effect[i], Herb_Indication[i], Herb_Info[i] ]

        return [decoction_in, herb_in, herb_out, herb_else]                             

# **PLAN** 개발예정) 입력받은 처방구성 리스트가 올바른 형식인지 확인하는 함수.
# **PLAN** 데이터를 전달받으면 본 함수로 먼저 검사를 하고 다음 단계로 진행합니다.
def list_check(composition_text):
    # 리스트 체크이지만 아직 텍스트 형태라는 것을 유의합시다.
    # 형식이 맞는지 확인하는 것입니다.
    return True

# **PLAN** 판단을 위한 함수들을 모두 본 클래스로 옮겨야 합니다.
# **PLAN** 메모리 효용을 위해 DB 클래스에서 필요한 데이터만 정리해서 넘겨줍니다.
class factorization:
    def __init__(self, composition_numpy, factorization_decoction, herb_info_search_result, medicine):
        self.composition_numpy = composition_numpy
        self.factorization_decoction = factorization_decoction
        self.herb_info_search_result = herb_info_search_result
        self.medicine = medicine

    def show_factorization_result(self, herb_info_search_result, composition_numpy, medicine):
            # 4. 다음과 같이 정리하여 출력합니다.
                # -- 1.0) 처방 관련 정보
                    # -- 1.1) 처방구성 : 처방명-@@@@, 구성-약재1, 약재2, 약재a, 약재d, 약재X, 약재Y, 약재Z
                    # -- 1.2) 처방효능 : @#$, %&^, *&^, %$#
                # -- 2.0) 인수 처방 정보
                    # -- 2.1) 포함처방 : A(약재1(+), 약재2(+), 약재3(-), 약재4(-)), B(약재a(+), 약재b(-), 약재c(-), 약재d(+))
                    # -- 2.2) 포함효능 : 약재1-@@, 약재2-##, 약재a-$$, 약재d-%%
                    # -- 2.3) 추가효능 : 약재X-@#$, 약재Y-#$%, 약재Z-%&*
                    # -- 2.4) 제외효능 : 약재3-^^, 약재4-&&, 약재b-**, 약재c-~~
                # -- 3.0) 기타

        decoction_in = herb_info_search_result[0]
        herb_in = herb_info_search_result[1]
        herb_out = herb_info_search_result[2]
        herb_else = herb_info_search_result[3]

        print(f"1.0) 처방 관련 정보\n"
              f"    1.1) 처방명   : {medicine.name}\n"
              f"    1.2) 처방구성 : \n        {composition_numpy}\n"
              f"    1.3) 처방효능 : {medicine.effect}\n"
              f"    1.4) 처방주치 : {medicine.indication}\n"
              )
              
        print(f"2.0) 인수 처방 정보")
        print(f"    2.1) 포함처방 : ")

        # Iterate through the decoction_in dictionary
        for key, value in decoction_in.items():
            transformed_list = []
            for item in value:
                if item in herb_in:
                    transformed_list.append(f'{item}(+)')
                else:
                    transformed_list.append(f'{item}(-)')
            decoction_in[key] = transformed_list

        # Print the transformed decoction_in dictionary
        for key, value in decoction_in.items():
            print(f"        {key}: {value}")

        print(f"    2.2) 포함효능 : ")
        for key in herb_in:
            print(f"        {key} : {herb_in[key][0]}")

        print(f"\n    2.3) 추가효능 : ")
        for key in herb_else:
            print(f"        {key} : {herb_else[key][0]}")

        print(f"\n    2.4) 제외효능 : ")
        for key in herb_out:
            print(f"        {key} : {herb_out[key][0]}")

        print(f"\n3.0) 기타\n")  


# -------------------------------------------------------- #

# 1. 처방명과 구성을 입력합니다. 내용이 없으면 'null'또는 빈칸으로 둘 수 있습니다.

### 230914 IDEA : 검색 기능을 구현해보자. 구글 고급 검색처럼 AND OR 등의 코드를 입력하면 내부에서 자체적으로 해석해서 코드를 짜 주는 형식...
### 230915 IDEA : 수정이 편리하게 해야 한다. 여러 기능들을 함수로 추가하면 얼마든지 사용 가능하게...

# 먼저 처방명을 입력받습니다.
decoction_name = input(">>> 처방명을 입력하세요 : ")
# 처방명이 입력되지 않으면 decoction_name 변수를 "null"으로 재지정하고 **ALERT**를 표기합니다.
if decoction_name == "":
   decoction_name = "null"
   print("\n**ALERT**\n- 처방명이 입력되지 않았습니다.\n- 구성을 반드시 입력하세요.")

print("\n(중요) 구성 약재를 입력하실 때에는 한글(한자)의 형식으로 쉼표로 구별해 입력해 주세요.\n"
      "(중요) 괄호 안의 '한자'는 생략할 수 있습니다.\n"
      "ex) 인삼(人參), 복령, 백출, 감초(甘草)\n"
      "\n(중요) 현재는 용량까지 분석할 수 없습니다. 약재명만 입력해 주세요.\n ")

# 처방 구성을 입력받습니다.
composition_list = input(">>> 구성을 입력하세요. : ")

# **PLAN** STATUS 변수를 사용해 if 구문에서 벗어나 알고리즘을 실행합시다.
# -- STATUS 변수는 현재 상태를 확인하고 if 구문이 과도하게 깊게 작성되는 것을 피하기 위한 방책입니다.
STATUS = "input_null"

# INPUT 단계
print("")
# 처방 구성이 입력되지 않으면 composition_list 변수를 "null"로 재지정하고 처방명의 입력 여하를 체크합니다.
if composition_list == "":
    composition_list = "null"
    # 만약 처방명 또한 입력되지 않았다면 **ALERT**를 표기하고 알고리즘을 종료합니다.
    if decoction_name == "null":
        STATUS = "input_nulNnul"
        ERROR_CODE = "0"
        raise Exception(f"\n**ALERT**\n- 처방명과 구성이 모두 입력되지 않았습니다.\n- 알고리즘을 종료합니다.\n>>> ERROR CODE : {ERROR_CODE}")
    # 만약 처방명이 입력되었다면 **ALERT**를 표기하고 입력된 처방명을 바탕으로 DB에서 처방 구성을 검색합니다.
    else:
        STATUS = "input_nulNdec"
        print("**ALERT**\n- 구성이 입력되지 않았습니다.")
        # **PLAN** DB 검색 기능
# 처방 구성이 입력되었다면 처방명의 입력 여하를 체크합니다.
else:
    # 처방명이 입력되지 않았다면 **ALERT**를 표기하고 제공된 처방구성을 바탕으로 분석을 시작합니다.
    if decoction_name == "null":
        STATUS = "input_comNnul" 
        print("**ALERT**\n- 처방명이 입력되지 않았습니다.")
  # 처방명이 입력되었다면 처방 및 구성이 모두 입력되었음을 알리고 분석을 시작합니다.
    else:
        STATUS = "input_comNdec"
        print(f"\n- 처방({decoction_name})과 구성({composition_list})이 모두 입력되었습니다.")

print("________________________________________________\n")

# 1A. 데이터베이스를 연결합니다.
print("(중요) 데이터베이스는 다음과 같은 형식을 따르고 있어야 합니다.\n"
      "- 파일형식 : 엑셀, 스프레드시트\n"
      "- 시트구성 : 인수분해, 처방, 기본, 약재\n"
      "- 열  구성 : 이름, 출전, 주치, 효능, 비고, 구성, (인수분해)\n"
      "\n(중요) 입력하신 주소를 바탕으로 데이터베이스의 형식을 확인합니다.\n ")

print("(beta) 다음 주소를 입력하세요.")
print("C:/Users/jhgol/Desktop/개발/프론트엔드/CDS/factorization/database.xlsx")
address_DB_input = input(">>> 데이터베이스 주소를 입력하세요. : ")

# 1A.1. (test) 데이터베이스가 잘 연결되어 있는지 확인합니다.
herb_DB = HerDataBase(address=address_DB_input)
if herb_DB.addrest_check():
    pass
else:
    # address_check의 출력에 단계별 에러코드를 삽입합니다.
    # 출력되는 에러코드를 입력합니다.
    # 현재(230918)는 에러코드가 지정되지 않았습니다.
    ERROR_CODE = "에러코드가 지정되지 않았습니다."
    # address_check 함수를 통과하지 못하면 에러를 발생시키고 알고리즘을 종료합니다.
    raise Exception(f"\n**ALERT**\n- 제공하신 DB가 옳은 형식이 아닙니다.\n- 알고리즘을 종료합니다.\n>>> ERROR CODE : {ERROR_CODE}"    )

print("________________________________________________\n")

  # 1-1. '처방명'만 입력하면 먼저 기본 시트에서, 다음으로는 처방구성 시트에서 해당 처방명을 검색해 구성을 불러옵니다.
if STATUS == "input_nulNdec":
    print("- 제공하신 처방명으로 DB에서 처방구성을 검색합니다.")
    # 1.1.1. 처방명으로 DB에서 검색하는 단계
    # 구성을 composition_list 변수에 저장해서 넘겨줍니다.
    medicine_org = HerbMedicine(name=decoction_name, composition=composition_list)
  # 1-2. '구성'만 입력하면 바로 다음 task로 넘어갑니다.
elif STATUS == "input_comNnul":
    print("- 제공하신 처방구성으로 분석을 시작합니다.")
    # 1.2.1. 처방구성을 올바른 리스트 형태로 저장하여
    # 1.2.2. composition 속성에 전달합니다.
    medicine_org = HerbMedicine(composition=composition_list)
  # 1-3 모두 입력하면 그대로 분석을 시작합니다.
elif STATUS == "input_comNdec":
    print("- 분석을 시작합니다.")
    # 1.3.1. 처방구성을 올바른 리스트 형태로 저장하여
    # 1.3.2. composition 속성에 전달합니다. 처방명도 name 속성에 함께 전달합니다.
    medicine_org = HerbMedicine(name=decoction_name, composition=composition_list)

# **PLAN** 입력받은 처방구성 리스트가 올바른 형식인지 확인합니다.
if STATUS == "input_nulNdec":
    print("- 처방 구성이 입력되지 않았으므로 형식 검토 과정을 생략합니다.\n")
elif STATUS == "input_comNdec" or STATUS == "input_comNnul":
    if list_check(composition_list):
        print("- 입력하신 처방 구성이 옳은 형식입니다.\n")
    else:
        # list_check의 출력에 단계별 에러코드를 삽입합니다.
        # 출력되는 에러코드를 입력합니다.
        # 현재(230918)는 에러코드가 지정되지 않았습니다.
        ERROR_CODE = "에러코드가 지정되지 않았습니다."
        # list_check 함수를 통과하지 못하면 에러를 발생시키고 알고리즘을 종료합니다.
        raise Exception(f"\n**ALERT**\n- 입력하신 처방 구성이 옳은 형식이 아닙니다.\n- 알고리즘을 종료합니다.\n>>> ERROR CODE : {ERROR_CODE}")

# 입력된 처방 구성을 한글 구성으로 변경합니다.
# 0 : 한글 / 1 : 한자 / 2 : 영문
composition_list_kr = HerbMedicine.input_normalization(medicine_org.composition)[0]
composition_list_cn = HerbMedicine.input_normalization(medicine_org.composition)[1]
composition_list_en = HerbMedicine.input_normalization(medicine_org.composition)[2]

medicine = HerbMedicine(name=decoction_name, composition=composition_list_kr)

print("________________________________________________\n")


# SHEET 단계

# 2.  입력된 '구성'에 '기본' 시트의 '구성'이 포함되어 있는지 검색합니다.
# *(미리 제작된 class를 이용해 '처방명' 또는 '구성'을 이름으로 가지는 객체를 생성합니다.)*

# DB의 각 sheet를 넘파이 배열로 저장합니다.
basic_np = herb_DB.sheet_to_numpy(herb_DB.basic_sheet)
decoction_np = herb_DB.sheet_to_numpy(herb_DB.decoction_sheet)
herb_np = herb_DB.sheet_to_numpy(herb_DB.herb_sheet)

# composition이 입력된 경우에는 medicine에서 composition을 numpy 배열로 저장합니다.
if STATUS == "input_comNdec" or STATUS == "input_comNnul":
    composition_numpy = medicine.list_to_numpy(medicine.composition)
# composition이 입력되지 않은 경우에는 처방명을 통해 '처방' sheet에서 '구성'을 검색합니다.
else:
    # 개발예정) 처방명을 검색해서 구성을 저장하는 과정  
    ERROR_CODE = "에러코드가 지정되지 않았습니다."
    # address_check 함수를 통과하지 못하면 에러를 발생시키고 알고리즘을 종료합니다.
    raise Exception(f"\n**ALERT**\n- 처방명을 검색하는 기능이 구현되지 않았습니다.\n- 알고리즘을 종료합니다.\n>>> ERROR CODE : {ERROR_CODE}")

# 7번째 열이 구성이므로 DB의 basic_np에서 7번째 열을 가져와 새로운 넘파이 배열로 저장합니다.
basic_composition = basic_np[1:, 6]   # DB

  # 2-1. 먼저 '기본' 시트의 '구성' 중 전체가 그대로 포함되어 있는지 검색합니다.
  # **PLAN** class 내부의 함수로 다시 작성해야 합니다!

### 230926 IDEA 간단하게 로직을 짰습니다. 
# ratio를 조정하면 판단의 비율을 조정할 수 있습니다.
basic_search_result = herb_DB.basic_search(composition_numpy, ratio=50)
herb_info_search_result = herb_DB.herb_info_search(basic_search_result, composition_numpy)

factorization = factorization(composition_numpy, basic_search_result, herb_info_search_result, medicine)
factorization.show_factorization_result(herb_info_search_result, composition_numpy, medicine)

    # 2-1-1. 만약 그대로 포함되어 있다면 기본 '처방명'과, 그의 '주치'와 '효능'을 불러와서 함께 저장합니다.
  # 2-2. 그대로 포함되어 있지 않다면 '기본' 시트의 '구성' 중 '주약'이 모두 포함되어 있는 '처방명'이 있는지 검색합니다.
    # 2-2-1. '주약'이 모두 포함되어 있는 '처방명'이 있음이 확인되면, 해당 '처방명'의 다른 '구성' 요소 중 입력된 '구성'에 포함된 것이 있는지 확인합니다. 있다면 기본 '처방명'과, 그의 '주치'와 '효능', 그리고 포함된 '구성'을 불러와서 함께 저장합니다.
  # 2-3. 이 모든 과정은 중복으로 이뤄집니다. 포함된 기본 '구성'이 있다 한들 제외하고 다음 검색을 실행하지 않습니다.

print("________________________________________________\n")

# 3. 포함된 것으로 판단되어 저장된 '구성'의 요소를 제외하고 남은, 입력된 '구성'의 요소. 즉 약재들을 따로 저장하고, 그의 주치/효능을 '약재' 시트에서 검색합니다.
  # 3-1. 검색 결과가 존재하는 것들은 그 주치/효능을 약재명과 함께 저장합니다.
  # 3-2. 검색 결과가 존재하지 않는 것들은 약재명과 함께 'null'을 함께 저장합니다.

print("________________________________________________\n")

# 4. 원래 입력된 '구성'의 모든 요소들, 즉 모든 약재들의 주치/효능을 '약재' 시트에서 검색하여 딕셔너리의 형태로 따로 저장합니다. 이 딕셔너리는 요청시에만 출력합니다.
