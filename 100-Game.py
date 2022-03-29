#this game take numbers from two players in range (1,11) and calculate the sum, who arrive the sum=100,  he will be winner

sum = 0

while True:
    while True:
        first_player = input('first_player please enter num:')
        if first_player.isdigit():
            first_player = int(first_player)
            if first_player in range(1, 11) and first_player <= 100-sum:
                break

    sum += first_player
    print('the sum = ', sum)
    if sum == 100:
        print('first_player is winner')
        break
    else:
        while True:
            second_player = input('second_player please enter num:')

            if second_player.isdigit():
                second_player = int(second_player)
                if second_player in range(1, 11) and second_player <= 100-sum:
                    break

        sum += second_player
        print('the sum = ', sum)
        if sum == 100:
            print('second_player is winner')
            break