def designerPdfViewer(h, word):
    alp = []
    for i in range(97,123):
        alp.append(chr(i))
    comp = []
    for i in word:
        comp.append(h[alp.index(i)])
    return max(comp)*len(word)
print(designerPdfViewer([1,3,1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,5],"abc"))