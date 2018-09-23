mapper = {"1": "*", "2": ["a","b","c"], "3": ["d","e","f"],"4": ["g","h","i"],"5": ["j","k","l"],"6": ["m","n","o"],"7": ["p","q","r","s"],"8": ["t","u","v"],"9": ["w","x","y","z"]}
        if digits == "":
            return []
        res = []
        def backtrack(mapper, num, acc):
            if len(acc) == len(digits):
                res.append("".join(acc))
                return
                
            for i in mapper[digits[num]]:
                acc.append(i)
                backtrack(mapper, num+1, acc)
                acc.pop()
                
        backtrack(mapper, 0, [])
        return res
