import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

result_label=""
def get_file_path1():
    global path1
    path1 = filedialog.askopenfilename()  # 파일 선택 다이얼로그 띄우기
    print(f"선택한 파일 경로 (버튼 1):", path1)
    path_label1.config(text=f"선택한 파일 경로 (버튼 1): {path1}")

def get_file_path2():
    global path2
    path2 = filedialog.askopenfilename()  # 파일 선택 다이얼로그 띄우기
    print(f"선택한 파일 경로 (버튼 2):", path2)
    path_label2.config(text=f"선택한 파일 경로 (버튼 2): {path2}")

def getKeyInUrl(url):
    return url.rsplit('/', 1)[1]  # 'https://www.nike.com/kr/t/v2k-TeZkXP2L/FD0736-001' /뒷부분제거

def compare_dictionaries(dict1, dict2):
    for key in dict1:
        if key in dict2 and dict1[key] != dict2[key]:
            #print(f"Key: {key}, Value in dict1: {dict1[key]}, Value in dict2: {dict2[key]}")
            write_csv(["변경된 모델", getKeyInUrl(key), f"{key}"])
    for key in dict1.keys():
        value_in = dict2.get(key)
        if value_in is None:
            write_csv(["위의 파일에만 있는 모델", getKeyInUrl(key), f"{key}"])
    for key in dict2.keys():
        value_in = dict1.get(key)
        if value_in is None:
            write_csv(["아래의 파일에만 있는 모델", getKeyInUrl(key), f"{key}"])

def getFilePath():
    # 현재 날짜와 시간 가져오기
    now = datetime.now()
    # 날짜를 원하는 형식으로 변환 (년-월-일)
    formatted_date = now.strftime("%Y-%m-%d")

    global csv_file_path
    # CSV 파일 경로 정의
    csv_file_path = 'nike_shoes_result_' + formatted_date + '.csv'

def write_csv(data_list):
    # 딕셔너리 값을 CSV 파일로 저장
    # CSV 파일 쓰기
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_list)
    return csv_file_path

def delete_file():
    try:
        os.remove(csv_file_path)
        print(f"파일 {csv_file_path} 삭제되었습니다.")
    except OSError as e:
        print(f"Error: {e.strerror}")

def compapre():
    if len(path1) == 0 or len(path2) == 0:
        result_label.config(text="선택한 파일이 잘못되었습니다.")
        return

    # 사용 예시
    my_dict1 = read_csv_to_dict(path1)
    my_dict2 = read_csv_to_dict(path2)

    getFilePath()

    delete_file()

    compare_dictionaries(my_dict1, my_dict2)

    result_label.config(text="축하 합니다. 파일이 생성되었습니다.")
    pass

# CSV 파일을 읽어서 딕셔너리로 저장하는 함수
def read_csv_to_dict(file_path):
    result_dict = {}
    with open(file_path, 'r', encoding='cp949') as csvfile:
        file_read = csv.reader(csvfile)
        array = list(file_read)
        for row in array:
            result_dict[row[0]] = row[1:]
    return result_dict




# 기본 프로그램 창 생성
root = tk.Tk()
root.title("파일 선택 프로그램")
root.geometry("600x200")  # 창 크기 설정

# 첫 번째 버튼 추가
select_button1 = tk.Button(root, text="파일 선택 1", command=get_file_path1, font=("Arial", 12))
select_button1.pack()

# 두 번째 버튼 추가
select_button2 = tk.Button(root, text="파일 선택 2", command=get_file_path2, font=("Arial", 12))
select_button2.pack()

# 선택한 파일 경로를 보여줄 라벨 추가
path_label1 = tk.Label(root, text="", font=("Arial", 10))
path_label1.pack()

# 선택한 파일 경로를 보여줄 라벨 추가
path_label2 = tk.Label(root, text="", font=("Arial", 10))
path_label2.pack()

# 결과 화면을 보여주는 라벨
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack()

select_button_compare = tk.Button(root, text="비교하기", command=compapre, font=("Arial", 12))
select_button_compare.pack()

# 프로그램 실행
root.mainloop()
