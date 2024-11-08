from parser import Parser
from data.config import driver

parser = Parser(driver=driver)

print(parser.parser_name(185457772))
