"""
    Strings assessment
"""
def to_rna(dna_strand):
    """
        This program converts given dna to rna strand
        Parameters: Accept a single parameter dna_strand of type string
        returns rna_strand as string
    """
    dna_to_rna_transcribe={'G':'C','C':'G','T':'A','A':'U'}
    rna_strand=""
    for char in dna_strand:
        rna_strand+=dna_to_rna_transcribe[char]
    return rna_strand
