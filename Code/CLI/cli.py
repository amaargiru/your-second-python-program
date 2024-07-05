from colorama import Fore, Style, init

from Core.game import Tile

init(autoreset=True)


class Cli:
    @staticmethod
    def pretty_print_board(board: list[list[Tile]]):
        max_length = max(max(len(str(item.value)) for item in row) for row in board)
        separator = '+'.join('-' * (max_length + 2) for _ in range(len(board[0])))
        separator = f"+{separator}+"

        print(separator)
        for row in board:
            row_str = "|"
            for item in row:
                item_str: str = str(item.value).center(max_length)
                if Cli._is_power_of_two(item.value):
                    item_str = Cli._get_color_for_power_of_two(item.value) + item_str + Style.RESET_ALL
                row_str += f" {item_str} |"
            print(row_str)
            print(separator)

    @staticmethod
    def pretty_print_score(score: tuple[int, int]):
        print(f"Score: {score[0]} ({Cli._get_color_of_score_diff(score[1])}+{score[1]}{Style.RESET_ALL})")

    @staticmethod
    def _is_power_of_two(n: int):
        return (n != 0) and (n & (n - 1)) == 0

    @staticmethod
    def _get_color_for_power_of_two(n: int):
        colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        # Find the power of the number (2^k) and use it to select a color
        power = 0
        while (1 << power) <= n:
            if (1 << power) == n:
                return colors[power % len(colors)]
            power += 1
        return Style.RESET_ALL  # Default color if not a power of two

    @staticmethod
    def _get_color_of_score_diff(n: int):
        if n <= 16:
            return Fore.BLACK
        if n <= 32:
            return Fore.GREEN
        return Fore.RED


if __name__ == "__main__":
    # Example usage
    board: list[list[Tile]] = [
        [Tile(0), Tile(2), Tile(4), Tile(8)],
        [Tile(16), Tile(32), Tile(64), Tile(128)],
        [Tile(256), Tile(512), Tile(1024), Tile(2048)],
        [Tile(4096), Tile(8192), Tile(16384), Tile(32768)]
    ]

    Cli.pretty_print_board(board)
    Cli.pretty_print_score((1024, 34))
