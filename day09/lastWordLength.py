def lengthOfLastWord(self, s):
    s = s.strip()
    return len(s.split(' ')[-1])

print(lengthOfLastWord(0, "   fly me   to   the moon  "))