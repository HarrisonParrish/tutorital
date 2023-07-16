def find_maximum_value(root):
    if root is None:
        return float("-inf")
    max_value = root.value
    for child in root.children:
        max_value = max(max_value, find_maximum_value(child))
    return max_value