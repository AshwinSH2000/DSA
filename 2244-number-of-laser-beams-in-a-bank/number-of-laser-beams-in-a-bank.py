class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []
        for i in bank:
            x=sum(1 for room in i if room =="1")
            if x!=0:
                devices.append(x)
        ans = 0
        for i in range(len(devices)-1):
            ans += devices[i]*devices[i+1]

        return ans
