import quadratic, zfactorial, logging

quadratic.logger.addHandler(logging.StreamHandler())
zfactorial.logger.addHandler(logging.StreamHandler())

print("\n\n### Running with all loggers at warning level\n")
print(quadratic.quadratic_formula(1, 0, -4))
print(zfactorial.factorial(5))

print("\n\n### Running with quadratic logger at info level\n")
quadratic.logger.setLevel(logging.INFO)
print(quadratic.quadratic_formula(1, 0, -4))
print(zfactorial.factorial(5))

print("\n\n### Running with zfactorial logger at info level\n")
quadratic.logger.setLevel(logging.WARNING)
zfactorial.logger.setLevel(logging.INFO)
print(quadratic.quadratic_formula(1, 0, -4))
print(zfactorial.factorial(5))

print("\n\n### Running with both loggers at info level\n")
quadratic.logger.setLevel(logging.INFO)
zfactorial.logger.setLevel(logging.INFO)
print(quadratic.quadratic_formula(1, 0, -4))
print(zfactorial.factorial(5))

