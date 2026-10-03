Start
    Declarations
        num Quanity
        num ITEM_PRICE = 2.99
        num SIZE = 5
        num Discounts[5] = 0, 0.05, 0.10, 0.15, 0.20
        num QUAN_LIMITS[5] = 0, 11, 26, 51, 101
        num x
        num QUIT = -1
        num TOTAL_DISCOUNT
        num FINAL_BILL
    itemsbought()
    while quanity <> QUIT
        determineDiscount()
    endwhile
    finish()
Stop


itemsbought()
    output "Enter quanity ordered or ", QUIT, "to quit "
    input quanity
return

determineDiscount()
    x = SIZE - 1
    while quanity < QUAN_LIMITS[x]
    x = x -1
    endwhile
    output "Your discount rate is ", DISCOUNTS[x]
    output "Enter quanity ordered or ", QUIT, "to quit"
    input quanity
return

finish()
    output "Thanks for shopping"
return
