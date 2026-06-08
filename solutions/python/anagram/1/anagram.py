"""
    List and string assessment
"""
def find_anagrams(word, candidates):
    """
        The program defines the code to return the list of anagrams for the given string
        Parameters: Stirng word and list candidates
        returns a list of anagrams
    """
    sorted_word="".join(sorted(word.lower()))
    ans=[]
    for candidate in candidates:
        sorted_candidate="".join(sorted(candidate.lower()))
        if word.lower()!=candidate.lower() and sorted_word==sorted_candidate:
            ans.append(candidate)
    return ans