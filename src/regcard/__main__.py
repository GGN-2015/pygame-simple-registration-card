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


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="python -m regcard",
        description="Show a centered rectangle in fullscreen. Enter rotates; Esc exits.",
    )
    parser.add_argument("width", type=positive_pixels, help="rectangle width in pixels")
    parser.add_argument("height", type=positive_pixels, help="rectangle height in pixels")
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
        pygame.draw.rect(rectangle, "black", rectangle.get_rect(), width=1)

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
