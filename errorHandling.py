import logging
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
logging.info("Started")
try:
    age = int(input("Enter Your Age: "))
    now = age + 1
    print(now)
except Exception as err:
    logging.warning("Only Integer Value allow")
    # logging.error("Only Integer Value allow")
else:
    logging.info("Try Runs")
finally:
    logging.info("program completed")

print("End")