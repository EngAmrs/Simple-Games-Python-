import random
import curses

screen = curses.initscr()

curses.curs_set(0)

screenHeight, screenWidth = screen.getmaxyx()

window = curses.newwin(screenHeight, screenWidth, 0, 0)

curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_CYAN)
window.bkgd(curses.color_pair(1))

speed = 100
counter = 0
window.keypad(1)
window.timeout(speed)
snakeX = screenWidth // 2
snakeY = screenHeight // 2
snake = [
  # Snake head
  [snakeY, snakeX],
  # Snake body
  [snakeY, snakeX - 1],
  # Snake tail
  [snakeY, snakeX - 2]
]

food = [screenHeight // 8, screenWidth // 2]

window.addch(food[0], food[1], curses.ACS_DIAMOND)
window.addstr(0,0, "Score: " + str(counter))
key = curses.KEY_RIGHT

while True:
  next_key = window.getch()
  key = key if next_key == -1 else next_key


  if snake[0][0] in [0, screenHeight - 1] or snake[0][1] in [0, screenWidth - 1] or snake[0] in snake[2:]:
    window.clear()
    window.addstr(screenHeight // 2, screenWidth // 2, "Game Over")
    window.refresh()
    curses.napms(5000)
    curses.endwin()
    quit()


  new_head = [snake[0][0], snake[0][1]]
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  elif key == curses.KEY_UP:
    new_head[0] -= 1
  elif key == curses.KEY_RIGHT:
    new_head[1] += 1
  elif key == curses.KEY_LEFT:
    new_head[1] -= 1

  snake.insert(0, new_head)
  if snake[0] == food:
    food = None
    while food is None:
      counter += 1
      window.addstr(0,0,  "Score: " + str( + counter))
      speed -= 2
      window.timeout(speed)

      new_food = [
        random.randint(1, screenHeight - 2),
        random.randint(1, screenWidth - 2)
      ]
      food = new_food if new_food not in snake else None
    window.addch(food[0], food[1], curses.ACS_DIAMOND)
  else:
    tail = snake.pop()
    window.addch(tail[0], tail[1], ' ')
  window.addch(snake[0][0], snake[0][1], curses.ACS_DIAMOND)
  window.refresh()
