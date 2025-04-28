def canUnlockAll(boxes):
    opened_boxes = set([0])  # Start with box 0 opened
    keys = boxes[0][:]       # Copy keys from box 0

    while keys:
        key = keys.pop()

        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])  # Add new keys from this box

    return len(opened_boxes) == len(boxes)
