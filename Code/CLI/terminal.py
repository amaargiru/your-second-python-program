from colorama import Fore, Style, init

init(autoreset=True)


class Terminal:
    @staticmethod
    def pretty_print_2d_list(board):
        max_length = max(max(len(str(item)) for item in row) for row in board)
        separator = '+'.join('-' * (max_length + 2) for _ in range(len(board[0])))
        separator = f"+{separator}+"

        print(separator)
        for row in board:
            row_str = "|"
            for item in row:
                item_str = str(item).center(max_length)
                if Terminal._is_power_of_two(item):
                    item_str = Terminal._get_color_for_power_of_two(item) + item_str + Style.RESET_ALL
                row_str += f" {item_str} |"
            print(row_str)
            print(separator)

    @staticmethod
    def _is_power_of_two(n):
        return (n != 0) and (n & (n - 1)) == 0

    @staticmethod
    def _get_color_for_power_of_two(n):
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        # Find the power of the number (2^k) and use it to select a color
        power = 0
        while (1 << power) <= n:
            if (1 << power) == n:
                return colors[power % len(colors)]
            power += 1
        return Style.RESET_ALL  # Default color if not a power of two


# Example usage
board = [
    [0, 2, 4, 8],
    [16, 32, 64, 128],
    [256, 512, 1024, 2048],
    [4096, 8192, 16384, 32768]
]

Terminal.pretty_print_2d_list(board)
