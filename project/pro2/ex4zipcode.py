# 우편정보 파일 자료 읽기
# 키보드에서 입력한 동이름으로 해당 주소 정보 출력

def zipProcess():
    # dongIrum=input('동 이름 입력: ')
    dongIrum='개포1동'
    # print(dongIrum)

    with open(r'zipcode.txt',mode='r',encoding='uth-8') as f:
        # line = f.read()   # 전체 행 읽기
        line = f.readline()  # 한 행 읽기
        # print(line)
        # lines=line.split('\t')
        # lines=line.split(chr(9))
        # print(lines)

        while line:
            lines = line.split(chr(9))
            if lines[3].startswith(dongIrum):
                print(f'우:{lines[0]},{lines[1]},{lines[2]},{lines[3]}')

            line = f.readline()

if __name__ =='__main__':
    zipProcess()