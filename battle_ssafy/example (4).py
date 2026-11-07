"""이 파일에 직접 풀이를 작성하고 저장한 뒤 F5로 실행하세요.
참고: 60점_이상_노리기_코드.py / 100점_노리기_코드.py
문제와 입력 형식: docs/battle_ssafy_user_problem.pdf
"""

# 필요한 import, 함수, 전역 변수는 이곳에 자유롭게 작성하세요.

import heapq
D=[(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]
def decide(state):
    """현재 상태를 받아 'R A', 'R F', 'R F M', 'G 평문', 'S' 중 하나를 반환."""
    # state는 매 턴 새로 전달되는 딕셔너리입니다. 아래 숫자는 형식 예시입니다.
    #
    # state = {
    #     'map_data': [['M', 'G', 'E1']],  # 실제로는 단계 크기의 2차원 리스트
    #     'allies': {'M': ['100', 'R', '1', '0']},
    #     'enemies': {'E1': ['10']},      # 6단계에는 E1, E2, E3, X가 있음
    #     'codes': [],                   # 보급소 옆이면 ['SRKKCVJJRWP']
    #     'stage_id': 1,                 # 단계 번호 (int)
    #     'turn': 0,                     # 이미 소비한 턴 (int)
    #     'turn_limit': 100,             # 최대 턴 (int)
    #     'rules': {
    #         'target': 'E1',            # 1~5단계 E1, 6단계 X (좌표 아님)
    #         'caesar_shift': 17,        # 연습용 암호 이동값 (int)
    #         'normal_damage': 30,       # 일반탄 피해 (int)
    #         'mega_damage': 70,         # 메가탄 피해 (int)
    #         'shot_range': 3,           # 사거리 (int)
    #         'enemies_move': False,     # 정지한 적 가정 (bool)
    #     }
    # }
    #
    # allies['M'] 순서: [체력, 방향, 일반탄 수, 메가탄 수]. 모두 str입니다.
    # enemies는 적 이름별 [체력 문자열]입니다. 제거한 적은 다음 입력에서 빠집니다.
    # 목표 좌표는 주지 않으므로 map_data에서 목표 기호를 직접 찾으세요.
    #
    # 값 꺼내기 예시:
    # board = state['map_data']         # board[행][열], 각 칸은 str
    # normal = int(state['allies']['M'][2])
    # mega = int(state['allies']['M'][3])
    # target = state['rules']['target']
    # hp = int(state['enemies'][target][0])
    # codes = state['codes']            # 비어 있으면 codes[0] 접근 불가

    # ==================== 직접 작성할 영역 ====================
    board= state['map_data']
    height,weight=(len(board),len(board[0]))
    target=state['rules'].get('target','X' if 'X' in state['enemies'] else 'E1')

    objects,health={},[]
    start=goal=None
    normal,mega=map(int,state['allies']['M'][2:4])
    cap=0
    for r in range(height):
        for c in range(weight):
            tile=board[r][c]
            if tile=='M':
                start=(r,c)
            if tile==target:
                goal=(r,c)
            if tile =='T' or tile in state['enemies']:
                hp=1 if tile =='T' else int(state['enemies'][tile][0])
                objects[r,c]=len(health)
                health.append(hp)
                cap+=(hp+69)//70
    if start is None or goal is None:
        return 'S'
    goal_index=objects[goal]
    cap= max(cap,mega)

    initial=(*start,normal,mega,tuple(health))
    queue,distance=[(0,initial,'')],{initial:0}
    while queue:
        cost,st,first=heapq.heappop(queue)
        if cost!=distance[st]:
            continue
        r,c,n,m,remaining=st
        if remaining[goal_index]==0:
            if first !='SUPPLY':
                return first
            shift= state['rules']['caesar_shift']
            return 'G '+''.join(chr((ord(ch)-ord('A')-shift)%26+ord('A'))for ch in state['codes'][0])
        def tile_at(r,c):
            if (r,c) in objects and remaining[objects[r,c]]==0:
                return 'G'
            return board[r][c]

        def push(nxt,action):
            if nxt not in distance or cost+1<distance[nxt]:
                distance[nxt]=cost+1
                heapq.heappush(queue,(cost+1,nxt,first or action))

        for dr,dc,d in D:
            nr,nc=r+dr,c+dc
            if 0<=nr<height and 0<=nc<weight:
                tile= tile_at(nr,nc)

                if tile in ('G','M'):
                    push((nr,nc,n,m,remaining),d+' A')
                if tile =='F' and m<cap:
                    push((r,c,n,m+1,remaining),'SUPPLY')
            for k in range(1,4):
                nr,nc=r+dr*k,c+dc*k
                if not(0<=nr<height and 0<=nc<weight):
                    break
                tile=tile_at(nr,nc)
                if tile in ('G','M','W'):
                    continue
                if (nr,nc) in objects:
                    index=objects[nr,nc]
                    for use_mega,ammo,damage in((False,n,30),(True,m,70)):
                        if ammo==0:
                            continue
                        after= list(remaining)
                        after[index]=0 if tile=='T' else max(0,after[index]-damage)
                        push((r,c,n-(not use_mega), m-use_mega,tuple(after)),
                            d+' F'+(' M' if use_mega else ''),     
                        )
                break
                

    return 'S'

    # ==================== 직접 작성할 영역 끝 =================


# 아래는 F5 실행용 연결 코드입니다. 수정할 필요 없습니다.
if __name__ == '__main__':
    from pathlib import Path
    import subprocess
    import sys

    folder = Path(__file__).resolve().parent
    result = subprocess.run(
        [sys.executable, str(folder / 'run_all.py'), '--agent', 'mine'],
        cwd=folder,
    )
    raise SystemExit(result.returncode)