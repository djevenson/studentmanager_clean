


class _C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[32m"
    YELLOW = "\033[33m"
    CYAN   = "\033[36m"
    RED    = "\033[31m"


def _banner(text: str) -> None:
    print(f"\n{_C.BOLD}{_C.CYAN}{'=' * 50}{_C.RESET}")
    print(f"{_C.BOLD}{_C.CYAN}  {text}{_C.RESET}")
    print(f"{_C.BOLD}{_C.CYAN}{'=' * 50}{_C.RESET}\n")


def _ok(msg: str) -> None:
    print(f"{_C.GREEN}  ✓  {msg}{_C.RESET}")


def _err(msg: str) -> None:
    print(f"{_C.RED}  ✗  {msg}{_C.RESET}")