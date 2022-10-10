def safe_print_list(my_list=[], x=0):



    try:

        for i in range(x):

            print('{}'.format(my_list[i]), end="")

        print('\n')

    except:

        print('Number is not in range')

safe_print_list([1,2,3,4,5], 3)
