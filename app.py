import pygame as pg

W: int = 20
H: int = 20

BLOCK_SIZE = 10

WIDTH = W * BLOCK_SIZE
HEIGHT = H * BLOCK_SIZE


class Position:
	"""
	Position class that acts as coordinates in a 2d plane
	"""
	def __init__(self, x: int, y: int) -> None:
		self.x = x
		self.y = y


	def __eq__(self, other: tuple | object) -> bool:
		if isinstance(other, tuple):
			return self.astuple == other

		elif isinstance(other, Position):
			return ((self.x == other.x) and (self.y == other.y))


	def __ne__(self, other: tuple | object) -> bool:
		if isinstance(other, tuple):
			return self.astuple != other

		elif isinstance(other, Position):
			return ((self.x != other.x) or (self.y != other.y))


	@property
	def astuple(self):
		return (self.x, self.y)


	def __repr__(self) -> str:
		return str(self.astuple)
 


class GameOfLife:
	def __init__(self, width: int, height: int) -> None:
		self.width = width
		self.height = height

		self.world: list[list[Position]] = []
		


class GOL_GAME:
	def __init__(self) -> None:
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))

		self.gol: GameOfLife = GameOfLife(width=WIDTH, height=HEIGHT)
		
	def	step(self) -> None:
		pg.display.update()


if __name__ == '__main__':
	game = GOL_GAME()

	while True:
		game.step()