class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build freq mpa and initialise values
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        have = 0
        need_count = len(need)
        l = 0
        best = ""
        # 
        for r in range(len(s)):
            ch = s[r]
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                # We only increment have when we've just
                # satisfied the required frequency for this char
                if window[ch] == need[ch]:
                    have += 1
            # Window is valid
            while have == need_count:
                # Save smallest valid window
                if best == "" or r - l + 1 < len(best):
                    best = s[l:r + 1]
                left = s[l]
                if left in need:
                    window[left] -= 1
                    # We just fell below the required frequency
                    if window[left] < need[left]:
                        have -= 1
                l += 1
        return best



