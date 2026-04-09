import logging
logger = logging.getLogger("factorial")

# from quadratic_with_wrong_log_initialization import quadratic_formula
# from quadratic import quadratic_formula

# logging.basicConfig(level=logging.DEBUG)  # Don't do it!

# Example function
def factorial(n:int) -> int:
    logger.info('factorial(%d)', n)
    return 1 if n<=1 else n*factorial(n-1)


if __name__=="__main__":
    print(factorial(6))

