import argparse
import os


def positive_pixels(value: str) -> int:
    try:
        pixels = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be a positive integer") from error
    if pixels <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return pixels


def color_channel(value: str) -> int:
    try:
        channel = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer between 0 and 255") from error
    if not 0 <= channel <= 255:
        raise argparse.ArgumentTypeError("must be an integer between 0 and 255")
    return channel


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="python -m regcard",
        description="Show a centered rectangle in fullscreen. Enter rotates; Esc exits.",
    )
    parser.add_argument("width", type=positive_pixels, help="rectangle width in pixels")
    parser.add_argument("height", type=positive_pixels, help="rectangle height in pixels")
    parser.add_argument(
        "--linecolor",
        nargs=3,
        type=color_channel,
        default=(0, 0, 0),
        metavar=("R", "G", "B"),
        help="border and line RGB color (0-255; default: 0 0 0)",
    )
    parser.add_argument(
        "--lineweight",
        type=positive_pixels,
        default=1,
        metavar="PIXELS",
        help="border and line width in pixels (default: 1)",
    )
    arguments = parser.parse_args()

    os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
    os.environ.setdefault("SDL_WINDOWS_DPI_AWARENESS", "permonitorv2")

    import pygame

    try:
        pygame.display.init()
        pygame.display.set_caption("Registration Card")
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        rectangle = pygame.Surface((arguments.width, arguments.height)).convert()
        rectangle.fill("white")
        rectangle_bounds = rectangle.get_rect()
        pygame.draw.rect(
            rectangle, arguments.linecolor, rectangle_bounds, width=arguments.lineweight
        )
        pygame.draw.line(
            rectangle,
            arguments.linecolor,
            rectangle_bounds.midleft,
            rectangle_bounds.midtop,
            width=arguments.lineweight,
        )

        while True:
            screen.fill("white")
            screen.blit(rectangle, rectangle.get_rect(center=screen.get_rect().center))
            pygame.display.flip()

            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    rectangle = pygame.transform.rotate(rectangle, 90)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
