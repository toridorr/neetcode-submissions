class Solution:
    def isPalindrome(self, s: str) -> bool:
        # You are going to create an empty string and use the loop to ONLY add 
        # letters and numbers. This method then removes all special characters such as 
        # question marks and blanks 
        cleaned = ""
        for char in s:
            if char.isalnum(): # this will run if the loop encounters a letter or digit and will skip if it encounters a special character 
                cleaned += char.lower() # I can make the character lowercase and add it at the same time. Creates "wasitacaroracatisaw"
        return cleaned == cleaned[::-1]
