# data model definition
class s(object):
    """
    class software, with two attributes:
    1. publisher: the developer of software
    2. paper: the count of software corresponding papers
    """
    def __init__(self, publisher, paper):
        self.publisher = publisher
        self.paper = paper
    
if __name__ == "__main__":
    pass