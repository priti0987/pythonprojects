import logging
import logging.handlers


class LogGen:
    @staticmethod
    def logGen():
        logging.basicConfig(filename="Logs/KhanBankAutomationLog.log", format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler("Logs/KhanBankAutomationLog.log", maxBytes=1024 * 1024 * 20,
                                                           backupCount=3)

        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger
