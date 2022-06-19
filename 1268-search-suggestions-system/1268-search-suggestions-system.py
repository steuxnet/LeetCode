class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        list_ = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = list(filter(lambda p: p[i] == c if len(p) > i else False, products))
            list_.append(products[:3])
        return list_