'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 온라인 강의
def dfs(v):
    print(v)
    visited[v] = 1

    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)

V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    v, w = graph[i * 2], graph[i * 2 + 1]

    adj_list[v].append(w)
    adj_list[w].append(v)

print(adj_list)

visited = [0] * (V + 1)
dfs(1)

# # 오프라인 강의
# V, E = map(int, input().split())
# edges = list(map(int, input().split()))
# # 인접행렬로 변환
# # 인접행렬에서는 정점의 번호를 인데스로 사용(정점이 7번까지 있으니까 8칸짜리 만들기)
# adj = [[0] * (V + 1) for _ in range(V + 1)]
# # edges가 연결 정보니까 2개씩 끊어서 읽기
# for i in range(0, E * 2, 2):
#     # edges[i]번과 edges[i + 1]번 정점이 연결되어 있음
#     s = edges[i]
#     e = edges[i + 1]
#     adj[s][e] = 1
#     adj[e][s] = 1

# for row in adj:
#     print(row)

# def dfs(start):
#     # 그래프의 모든 정점을 순회하기
#     # 일단 경로를 찾으면 해당 경로로 이동하고
#     # 경로가 없으면 이전 정점으로 되돌아가서 다시 길 찾기

#     # 현재 정점과 연결된 정점 찾기
#     # adj[3] <<< 이 행이 3번 정점과 연결된 정보
#     # i번 열에 값이 1이라면, 3번과 i번은 연결된 거임

#     # 경로를 저장할 stack
#     stack = []
#     # 시작 정점 추가
#     stack.append(start)
#     # 한 번 방문한 정점을 재방문하지 않기 위해서 방문 여부 검사
#     visited = [0] * (V + 1)
#     # 시작 정점 방문 처리
#     visited[start] = 1   

#     # 현재 위치에서 갈 수 있는 길 찾아보기
#     # 현재 위치: 경로상 마지막 정점
#     current = stack[-1]
#     # adj[current]를 살펴보자

#     pass