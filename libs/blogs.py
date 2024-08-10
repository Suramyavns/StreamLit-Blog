class blogs:
    blogss = tuple()
    def __init__(self) -> None:
        pass
    
    @classmethod
    def add(cls,obj)->None:
        cls.blogss+=(obj)

    @classmethod
    def display(cls)->None:
        for blog in cls.blogss:
            print(blog)