
def merge(left, right):
    result = []

    i = 0
    j = 0

    # Compare elements from both lists
    while i < len(left) and j < len(right):

        left_key = (left[i]["priority"], left[i]["deadline"])
        right_key = (right[j]["priority"], right[j]["deadline"])

        if left_key <= right_key:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(parcels):

    # Base condition
    if len(parcels) <= 1:
        return parcels

    # Divide the list into two halves
    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    # Merge both sorted halves
    return merge(left, right)


def prioritize_parcels(parcels):
    return merge_sort(parcels)
