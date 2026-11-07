def my_func(game_data):
    try:
        # 🔁 방향 벡터: [우, 상, 좌, 하] 순서로 이동 시 사용할 델타
        dr = [0, -1, 0, 1]
        dc = [1, 0, -1, 0]
        direction_map = ['R', 'U', 'L', 'D']  # 방향 인덱스를 문자열로 매핑

        # 입력된 게임 데이터를 파싱하여 map_data, codes, allies 등의 전역 변수 초기화
        parse_data(game_data)

        my_matrix = map_data  # 맵 정보 저장 (예: 'A', 'X', 'G', 'R' 등)
        start_position = [-1, -1]   # 'A'의 시작 위치 (플레이어)
        target_position = [-2, -2]  # 'X'의 목표 위치 (적 탱크)

        # 맵 전체를 순회하면서 시작 지점과 목표 지점을 찾음
        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                if map_data[i][j] == 'A':
                    start_position = [i, j]
                if map_data[i][j] == 'X':
                    target_position = [i, j]

        # BFS 탐색을 위한 큐 초기화 (위치 좌표와 방향)
        pq = [(start_position[0], start_position[1], None)]
        visited = [[0] * len(map_data[0]) for _ in range(len(map_data))]  # 방문 체크 배열
        parent = {(start_position[0], start_position[1]): None}  # 각 노드의 부모 위치 저장
        order = []  # 최종 이동 경로 저장용 리스트

        # BFS 탐색 시작
        while pq:
            row, col, _ = pq.pop(0)

            # ✅ 적 탱크와 수직 방향으로 거리가 1~3칸 이내면서 같은 열
            if target_position[0] + 1 <= row <= target_position[0] + 3 and col == target_position[1]:
                if row - target_position[0] == 1 or \
                   (row - target_position[0] == 2 and my_matrix[row - 1][col] != 'R') or \
                   (row - target_position[0] == 3 and my_matrix[row - 1][col] != 'R' and my_matrix[row - 2][col] != 'R'):
                    # 포탄 사거리 내에 있고 바위가 가로막지 않으면 사격 가능한 위치
                    goal_row, goal_col, target_direct = row, col, "U F"
                    break

            # ✅ 적 탱크와 수평 방향으로 거리가 1~3칸 이내면서 같은 행
            if target_position[1] - 3 <= col <= target_position[1] - 1 and row == target_position[0]:
                if target_position[1] - col == 1 or \
                   (target_position[1] - col == 2 and my_matrix[row][col + 1] != 'R') or \
                   (target_position[1] - col == 3 and my_matrix[row][col + 1] != 'R' and my_matrix[row][col + 2] != 'R'):
                    # 포탄 사거리 내에 있고 바위가 가로막지 않으면 사격 가능한 위치
                    goal_row, goal_col, target_direct = row, col, "R F"
                    break

            # 사방 탐색 (우, 상, 좌, 하)
            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                if 0 <= nr < len(my_matrix) and 0 <= nc < len(my_matrix[0]) and my_matrix[nr][nc] == 'G' and not visited[nr][nc]:
                    pq.append((nr, nc, i))
                    visited[nr][nc] = 1
                    parent[(nr, nc)] = (row, col)

        # 목표 지점에서 시작하여 역으로 parent를 따라 경로 추적
        k = (goal_row, goal_col)
        while k is not None:
            order.append(k)
            k = parent.get(k)
        order.reverse()

        # 각 연속된 위치 쌍에 대해 방향 계산 후 '방향 A' 명령어 저장
        order_output = []
        for i in range(len(order) - 1):
            cr, cc = order[i]
            nr, nc = order[i + 1]

            for d in range(4):  # 방향 비교 (dr, dc 이용)
                if cr + dr[d] == nr and cc + dc[d] == nc:
                    order_output.append(f"{direction_map[d]} A")
                    break

        # 이동 명령이 존재하면 첫 번째 이동만 반환, 없다면 사격 명령 반환
        return order_output[0] if order_output else target_direct

    except:
        # 예외 발생 시 정지 명령 'S' 반환
        return 'S'