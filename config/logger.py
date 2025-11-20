from datetime import datetime

COLORS = {
    'INFO': '\033[36m',
    'GRAY': '\033[90m',
    'RESET': '\033[0m',
    'ERROR': '\033[31m',
    'WARNING': '\033[33m',
    'SUCCESS': '\033[32m',
}


class Logger:
    @staticmethod
    def _log(level: str, title: str, message: str):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        colored_timestamp = f"{COLORS['GRAY']}{timestamp}{COLORS['RESET']}"

        print(
            f"{colored_timestamp} | {COLORS[level]}{title}{COLORS['RESET']} | {message}")

    @staticmethod
    def success(message: str):
        Logger._log('SUCCESS', 'ÉXITO', message)

    @staticmethod
    def info(message: str):
        Logger._log('INFO', 'INFO', message)

    @staticmethod
    def warning(message: str):
        Logger._log('WARNING', 'ADVERTENCIA', message)

    @staticmethod
    def error(message: str):
        Logger._log('ERROR', 'ERROR', message)
