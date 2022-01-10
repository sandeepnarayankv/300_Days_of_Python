def check_guess(num, guess):
    try:
        if  0 < guess < 11:
            if guess == num:
                print('you are a genius!')
                return True
            else:
                return False
        else:
            return 'Please Enter a Number between 1~10'
    except TypeError as err:
        return err