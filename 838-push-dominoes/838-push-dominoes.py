class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        info = {0: '.', -1: 'L', 1: 'R'}
        
        n = len(dominoes)
        status = [0] * n
        
        q = []
        for i in range(n):
            if dominoes[i]=='L':
                q.append((i, -1))
            elif dominoes[i]=='R':
                q.append((i, 1))
        
        ans = [dominoes[i] for i in range(n)]
        while len(q)>0:
            q1 = set([])
            for pi, di in q:
                pj = pi + di
                if pj>=0 and pj<=n-1 and ans[pj]=='.':
                    status[pj] += di
                    q1.add(pj)
            q = []
            for pj in q1:
                if status[pj]!=0:
                    ans[pj] = info[status[pj]]
                    q.append((pj, status[pj]))

        ans = "".join(ans)
        return ans