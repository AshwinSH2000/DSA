class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = False
        heavy = False
    
        if length*width*height >= 1e9 or length >= 1e4 or width >= 1e4 or height >= 1e4:
            bulky = True
        if mass >= 100:
            heavy = True

        print(bulky, heavy)
        if bulky and heavy:
            return "Both"
        elif not bulky and not heavy:
            return "Neither"
        elif bulky and not heavy:
            return "Bulky"
        else:
            return "Heavy"
        