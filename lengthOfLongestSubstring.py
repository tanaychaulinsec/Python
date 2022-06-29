**Solution:-**
scaning string from left to right 
store the char index in ascii position
update Left pointer if char repeat 
store res as max lenght of right -left

**JAVA**

```
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0;
        int l=0;
        int[] cache = new int[128];
        for (int r = 0; r < s.length(); r++) {
            l =Math.max(l, cache[s.charAt(r)]);
            cache[s.charAt(r)] = r + 1;
            result = Math.max(result, r - l + 1);
        }
        return result;
    }
}
```

**Python**

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=l=0
        cache=[0]*128
        for r in range(len(s)):
            l=max(l,cache[ord(s[r])])
            cache[ord(s[r])]=r+1
            res=max(res,r-l+1)
        return res
        
```
	
