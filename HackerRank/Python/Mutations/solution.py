def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    s=''.join(l)
    return s

