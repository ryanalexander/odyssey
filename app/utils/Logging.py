import logging

# Custom formatter
class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and custom time format with ASCII characters for severity indication"""

    grey = "\x1b[38;21m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    cyan = "\x1b[36;21m"
    reset = "\x1b[0m"
    format_str = "%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)"

    icons = {
        logging.DEBUG: "?",
        logging.INFO: "i",
        logging.WARNING: "!",
        logging.ERROR: "X",
        logging.CRITICAL: "!!"
    }

    test = f"{grey}[{red}{icons[logging.DEBUG]}{reset}{grey}] {reset} {format_str} {reset}"
    FORMATS = {
        logging.DEBUG: f"{grey}[{yellow}{icons[logging.DEBUG]}{grey}] {reset} {format_str} {reset}",
        logging.INFO: f"{grey}[{green}{icons[logging.DEBUG]}{grey}] {reset} {format_str} {reset}",
        logging.WARNING: f"{grey}[{cyan}{icons[logging.DEBUG]}{grey}] {reset} {format_str} {reset}",
        logging.ERROR: f"{grey}[{bold_red}{icons[logging.DEBUG]}{grey}] {reset} {format_str} {reset}",
        logging.CRITICAL: f"{grey}[{bold_red}{icons[logging.DEBUG]}{grey}] {reset} {format_str} {reset}"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)