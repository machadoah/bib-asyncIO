def hello() -> str:
    return "Hello world"


def hello_name(name: str) -> str:
    return f"Hello {name}"


def hello_name_with_default(name: str = "Antonio") -> str:
    return f"Hello {name}"


def add_two_numbers(a: float,b: float) -> float:
    return a + b 


def hello_multiple_people(*names: str) -> str:
    """
    Quando usamos *args em uma função, estamos permitindo que ela 
    receba um número variável de argumentos posicionais. 
    Os argumentos são passados como uma tupla.

    e.g:

    print(hello_multiple_people("Alice", "Bob", "Charlie"))
    """
    list = [f"Hello, {name}!" for name in names]
    return " ".join(list)


def print_info(**info: str) -> None:
    """
    Quando usamos **kwargs em uma função, estamos permitindo que ela 
    receba um número variável de argumentos nomeados. 
    Os argumentos são passados como um dicionário.
    
    e.g:

    print_info(name="Alice", age="25", city="Wonderland")

    """
    for key, value in info.items():
        print(f"{key}: {value}")


def square(number: float) -> float:
    return number ** 2
