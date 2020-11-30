import logging

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log_python.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

# Test messages
logger.debug("This is a harmless debug message")
logger.info("Just some useful info")
logger.warning("Just some useful info")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

# import math
#
# logger = logging.getLogger()
#
#
# def quadratic_formula(a, b, c):
#     """Return the solutions to te equation ax^2 + bx + c = 0"""
#     logger.info(f"quadratic_formula({a}, {b}, {c})")
#
#     # Compute the discriminant
#     logger.debug("# Compute the discriminant")
#     disc = b ** 2 - 4 * a * c
#
#     # Compute the two roots
#     logger.debug("# Compute the two roots")
#     root1 = (-b + math.sqrt(disc)) / (2 * a)
#     root2 = (-b - math.sqrt(disc)) / (2 * a)
#
#     # Return the roots
#     logger.debug("# Return the roots")
#     return (root1, root2)
#
#
# roots = quadratic_formula(1, 0, 1)
# print(roots)
