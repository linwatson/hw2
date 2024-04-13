import os
import json
FILE_PATH = "students.json"


def get_student_info(student_id: str) -> str:
    '''
    根據給定的學生學號，返回該學生的詳細資訊。

    Args:
        student_id (str): 學生的學號。

    Raises:
        ValueError: 如果學號不存在，則引發錯誤。

    Returns:
        str: 包含學生詳細資訊的 JSON 字串，如果學號不存在則返回錯誤訊息。

    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
    try:
        if student_id not in [item["student_id"] for item in data_dict]:
            raise ValueError(f"=>發生錯誤: 學號 {student_id} 找不到.")
    except ValueError as e:
        print(e)
    else:
        for item in data_dict:
            if item["student_id"] == student_id:
                return json.dumps(item, ensure_ascii=False, indent=2)


def add_course(student_id: str, course_name: str, course_score: str) -> None:
    '''
    為指定學號的學生新增一門課程及其分數。

    Args:
        student_id (str): 要新增課程的學生學號。
        course_name (str): 要新增的課程名稱。
        course_score (str): 要新增的課程分數。

    Raises:
        ValueError: 如果課程名稱或分數為空白，則引發錯誤。

    Returns:
        None

    '''
    try:
        if course_name == '' or course_score == '':
            raise ValueError('=>其它例外: 課程名稱或分數不可空白.')
    except ValueError as e:
        print(e)
    else:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data_dict = json.load(file)

        student_info = get_student_info(student_id)
        if student_info is not None:
            student_info_list = json.loads(student_info)
            data = {'name': course_name, 'score': float(course_score)}
            for item in data_dict:
                if item['student_id'] == student_info_list['student_id']:
                    item['courses'].append(data)
            with open(FILE_PATH, 'w', encoding='utf-8') as file:
                json.dump(data_dict, file, ensure_ascii=False, indent=4)
                print('=>課程已成功新增。')


def calculate_average_score(student_data: dict) -> str:
    '''
    計算指定學號學生的平均分數並返回。

    Args:
        student_data: 要計算平均分數的學生學號。

    Returns:
        str: 平均分數的字符串表示，保留兩位小數。

    '''
    student_info = get_student_info(student_data)
    if student_info is not None:
        data_dict = json.loads(student_info)
        result = 0
        for item in data_dict['courses']:
            result += float(item['score'])
        return '%.2f' % (result/len(data_dict['courses']))


if __name__ == '__main__':
    id = ""
    while os.path.isfile(FILE_PATH):
        print("***************選單***************")
        print("1. 查詢指定學號成績",
              "2. 新增指定學號的課程名稱",
              "3. 顯示指定學號的各科平均分數",
              "4. 離開", sep='\n')
        print('**********************************')
        select = input('請選擇操作項目：')

        if select == '1':
            id = input('請輸入學號：')
            msg = get_student_info(id)
            if msg is not None:
                print('=>學生資料: ', get_student_info(id))
        elif select == '2':
            id = input('請輸入學號:')
            name = input('請輸入要新增課程的名稱:')
            score = input('請輸入要新增課程的分數:')
            add_course(id, name, score)
        elif select == '3':
            id = input('請輸入學號:')
            print(calculate_average_score(id))
        elif select == '4':
            print('=>程式結束。')
            break
        else:
            print('=>請輸入有效的選項。')
