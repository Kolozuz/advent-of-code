current_pos = 50
with open('./2025/01/input.txt','r') as input_file:
    sequence = input_file.readlines()

    zeros_count = 0

    for item in sequence:
        move_by = int(item[1:]) # comes from input
        direction = item[0] # comes from input
        
        print(f"current pos is: {current_pos}")
        print(f"moving by: {move_by}")
        if direction == 'R':
            positions_sum = current_pos + move_by
            if positions_sum > 99:
                remainder = positions_sum % 100
                print(f"remainder is: {remainder}")
                current_pos = remainder
            else:
                current_pos = positions_sum

        else:
            positions_substraction = current_pos - move_by
            if positions_substraction < 0:
                remainder = positions_substraction % 100
                current_pos = remainder
            else:
                current_pos = positions_substraction
        
        if current_pos == 0:
            zeros_count += 1

    print(f"final pos is: {current_pos}")
    print(f"the arrow pointed at zero {zeros_count} times")
