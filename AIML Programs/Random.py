import random

def create_environment(size):
    return {
        'size': size,
        'agent_position': [0, 0]
    }

def is_valid_move(environment, position):
    size = environment['size']
    return 0 <= position[0] < size and 0 <= position[1] < size

def perceive(environment):
    return environment['agent_position']

def act(environment):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    random_move = random.choice(moves)
    new_position = [
        environment['agent_position'][0] + random_move[0],
        environment['agent_position'][1] + random_move[1]
    ]

    if is_valid_move(environment, new_position):
        environment['agent_position'] = new_position
        return f"Moved to {environment['agent_position']}"
    else:
        return "Cannot move, stayed in place"

def main():
    env_size = 5
    num_steps = 10

    environment = create_environment(env_size)

    print(f"Starting position: {perceive(environment)}")

    for step in range(num_steps):
        print(f"Step {step + 1}: {act(environment)}")

if __name__ == "__main__":
    main()