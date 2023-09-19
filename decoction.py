### !!! 주석 작성을 일상화합니다 !!! ###


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

# -------------------------------------------------------- #

class HerbMedicine:
    # 입력된 처방을 인스턴스화하는 클래스입니다.
    def __init__(self, name=None, source=None, indication=None, effect=None, note=None, composition=None, factorization=None):
        # 처방명, 출전, 주치, 효능, 비고, 구성, 인수분해
        self.name = None
        self.source = None
        self.indication = None
        self.effect = None
        self.note = None
        # **PLAN** 입력된 내용들을 하나하나 분리해서 리스트로 저장하도록 작성해야 합니다.
        self.composition = composition if composition is None else self.save_list(composition)
        self.factorization = None

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

    # 개발예정) 속성들을 활용해서 내용을 정리하려 출력하는 함수

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

    # **PLAN** 검색과 관련한 모든 함수를 본 클래스에 제작합니다.

    def addrest_check(self):
        # 입력받은 주소가 올바른 주소인지 확인하는 함수. : 아래 내용이 올바르게 지정되어 있는지 확인합니다.
          # - 파일형식 : 엑셀, 스프레드시트
          # - 시트구성 : 인수분해, 처방구성, 기본, 약재
          # - 열  구성 : 이름, 출전, 주치, 효능, 비고, 구성, (인수분해)    
        return True

    # 각 sheet를 넘파이 배열로 저장하는 함수
    def sheet_to_numpy(self, pandas_data):
        numpy_array = pandas_data.to_numpy()
        header = np.array(['대분류', '소분류', '이름', '치료원리', '출전', '비고', '구성'])
        numpy_data = np.vstack((header, numpy_array))
        return numpy_data

    # 개발예정) 처방명을 저장소에서 검색하는 함수

# **PLAN** 개발예정) 입력받은 처방구성 리스트가 올바른 형식인지 확인하는 함수.
# **PLAN** 데이터를 전달받으면 본 함수로 먼저 검사를 하고 다음 단계로 진행합니다.
def list_check(composition_text):
    # 리스트 체크이지만 아직 텍스트 형태라는 것을 유의합시다.
    # 형식이 맞는지 확인하는 것입니다.
    return True

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
print("C:/Users/jhgol/Desktop/개발/프론트엔드/factorization/database.xlsx")
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
    medicine = HerbMedicine(name=decoction_name, composition=composition_list)
  # 1-2. '구성'만 입력하면 바로 다음 task로 넘어갑니다.
elif STATUS == "input_comNnul":
    print("- 제공하신 처방구성으로 분석을 시작합니다.")
    # 1.2.1. 처방구성을 올바른 리스트 형태로 저장하여
    # 1.2.2. composition 속성에 전달합니다.
    medicine = HerbMedicine(composition=composition_list)
  # 1-3 모두 입력하면 그대로 분석을 시작합니다.
elif STATUS == "input_comNdec":
    print("- 분석을 시작합니다.")
    # 1.3.1. 처방구성을 올바른 리스트 형태로 저장하여
    # 1.3.2. composition 속성에 전달합니다. 처방명도 name 속성에 함께 전달합니다.
    medicine = HerbMedicine(name=decoction_name, composition=composition_list)

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
for composition in basic_composition:
    basic_list = composition.split(', ')
    result = [element in composition_numpy for element in basic_list]
    print(result)

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
