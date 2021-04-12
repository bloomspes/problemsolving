class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        copy_perm = perm.copy()

        arr, count = [0]*n, 0

        while arr != copy_perm:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[int(i/2)]

                else:
                    arr[i] = perm[int(n/2 + (i-1)/2)]
            perm = arr.copy()
            count += 1

        return count
