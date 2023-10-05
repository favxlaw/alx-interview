#!/usr/bin/python3
"""
Unlock Boxes 

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""
def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which
        contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """ check if all boxes can be opened
    Args: 
        boxes (list): List which contains all the boxes with the keys
        returns: bool; true if all the boxes can be opened, else fale
    """
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True  # The first box is initially opened.

    # Initialize a queue for BFS (breadth-first search)
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not opened_boxes[key]:
                opened_boxes[key] = True
                queue.append(key)

    # Check if all boxes have been opened
    return all(opened_boxes)
        
      #  return len(aux) == len(boxes)
    
    def main():
        """Entry Point"""
        canUnlockAll([[]]
                     )
    if __name__ == "__main__":
        main()
