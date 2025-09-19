from collections.abc import Callable


def usecase_executing_business_rules(
        runtime_port: Callable[[str], int]
        ) -> dict[int, list[str]]:
    """
    Executes the business rules of the usecase

    Parameters
    ----------
    runtime_port :
        function that takes a string and returns an int

    Returns
    -------
    dict[int, list[str]]
        dict with the result of the business rules
    """
    return({runtime_port("test"): ["result", "str"]})


def good_runtime_port(test: str) -> int:
    """"""
    return(1)

def bad_runtime_port(test: str) -> None:
    """"""
    pass

if __name__ == "__main__":
    print(usecase_executing_business_rules(good_runtime_port))
    # dynamically runs, but mypy raises error on
    # mismatched signature
    print(usecase_executing_business_rules(bad_runtime_port))