class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            parts = email.split("@") #["alice.z", "neetcode.io"]
            local_name = parts[0]
            domain_name = parts[1]
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            clean = local_name + "@" + domain_name
            seen.add(clean)

        return len(seen)





#local name = alice
#domain name = neetcode.io

#alice.z same as alicez

#m.y+name@email.com same as my@email.com


        