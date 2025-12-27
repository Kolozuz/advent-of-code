current_pos = 50
with open('./2025/01/input.txt','r') as input_file:
    sequence = input_file.readlines()

    zeros_count = 0

    for item in sequence:
        move_by = int(item[1:]) # se saca del array
        direction = item[0] # se saca del array
        
        print(f"current pos is: {current_pos}")
        print(f"moving by: {move_by}")
        if direction == 'R':
            positions_sum = current_pos + move_by
            if positions_sum > 99:
                remainder = positions_sum % 99
                print(f"remainder is: {remainder}")
                current_pos = remainder - 1
            else:
                current_pos += move_by

        else:
            positions_substraction = current_pos - move_by
            if positions_substraction < 0:
                current_pos = positions_substraction + 100
            else:
                current_pos -= move_by
        
        if current_pos == 0:
            zeros_count += 1

    print(f"final pos is: {current_pos}")
    print(f"the arrow pointed at zero {zeros_count} times")
