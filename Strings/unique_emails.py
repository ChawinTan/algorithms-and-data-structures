class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            #remember! when trying to parse a string into different parts, we can just split it!
            user, domain = email.split('@')
            user.replace('.', '')
            user.split('+')
            unique.add(user[0] + domain)
        return len(unique)
