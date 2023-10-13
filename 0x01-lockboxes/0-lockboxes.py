#!/usr/bin/python3
'''working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    to other boxes can be opened..
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxId = unseen_boxes.pop()
        if not boxId or boxId >= n or boxId < 0:
            continue
        if boxId not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxId])
            seen_boxes.add(boxId)
    return n == len(seen_boxes)
