import time

import logging as lg
lg.basicConfig(filename='decorators_logfiles', filemode='w', level=lg.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

# creating decorator function
def dec1(original_func): # taking another function as an argument

    try:
        # creating another function inside function
        lg.debug('initialization of timer function started')
        def timer():
            """
            This function calculates how much time a function took to run.
            """
            try:
                t1 = time.time()
                lg.debug('time initialization before calling the function {} sec'.format(t1))
                # calling outside function
                lg.debug('calling the outside {} function'.format(original_func))
                result = original_func()
                t2 = time.time() - t1
                lg.debug('It took {} secs to run'.format(t2))
                print('It took {} secs to run'.format(t2))
                return result

            except Exception as e:
                lg.exception('This error occurred: {}'.format(e))

        return timer

    except Exception as e:
        lg.exception('This error occurred: {}'.format(e))





@dec1
def add():
    # using sleep function
    # lg.debug('initialization of sleep function')
    try:
        time.sleep(1)
        result = 4 + 6
        lg.debug('addition of two numbers is {}'.format(result))
        print(result)
    except Exception as e:
        lg.exception('This error occurred : {}'.format(e))



# there are two ways to call the decorators first one using @function name like above
# calling the function along with decorator
add()

# second one is like below
#call = dec1(add)
#call()


