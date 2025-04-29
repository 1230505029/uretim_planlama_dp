from typing import List

def uretim_planlama_suresi(sureler: List[List[int]]) -> int:
    """
    sureler[i][j] = i. işin j. makinadaki işlem süresi
    DP tablosu ile toplam minimum süre hesaplanır.
    """
    n = len(sureler)      # iş sayısı
    m = len(sureler[0])   # makine sayısı

    # DP tablosu
    dp = [[0]*m for _ in range(n)]

    # İlk işin ilk makinesinin süresi
    dp[0][0] = sureler[0][0]

    # İlk işin diğer makinelerdeki sürelerini doldur
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + sureler[0][j]

    # Diğer işler için ilk makinenin sürelerini doldur
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + sureler[i][0]

    # Diğer hücreleri doldur (önceki iş ve önceki makine etkili)
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + sureler[i][j]

    return dp[n-1][m-1]  # son işin son makinede bitiş süresi

# Örnek kullanım
sureler = [
    [2, 3, 2],  # 1. iş: makine1=2dk, makine2=3dk, makine3=2dk
    [4, 1, 3],  # 2. iş: ...
    [3, 2, 4]
]

sonuc = uretim_planlama_suresi(sureler)
print(f"Toplam minimum üretim süresi: {sonuc} dk")
