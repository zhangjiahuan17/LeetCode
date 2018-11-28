class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        result = []
        dict = Counter()
        for cpdomain in cpdomains:
            count = int(cpdomain.split()[0])
            domains = cpdomain.split()[1]
            domains = domains.split('.')
            for i, domain in enumerate(domains):
                dict['.'.join(domains[i:])] += count
        for i in dict:
            result.append('{} {}'.format(dict[i], i))
        return result


if __name__ == "__main__":
    cpdomains = ["900 google.mail.com", "50 yahoo.com",
                 "1 intel.mail.com", "5 wiki.org"]
    print Solution().subdomainVisits(cpdomains)
