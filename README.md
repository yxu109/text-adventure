# Text Adventure Game

## Yizheng Xu yxu109@stevens.edu


## Repository URL
https://github.com/yxu109/text-adventure.git

## Time Spent on the Project
- Approximately 50 hours.

## Testing Strategy
- Manual playtesting to ensure logical progression and consistency in the narrative and gameplay.
- Rigorous testing of all commands, including edge cases and invalid inputs.
- Verification of map integrity to ensure all rooms are accessible and exits function as expected.

## Known Bugs and Issues
- No unresolved bugs currently known. However, potential edge cases might exist in complex map configurations.

## Difficult Issues and Resolutions
- **Issue**: Challenges in implementing dynamic direction commands (e.g., 'n' for 'north') without interfering with other commands starting with the same letter.
  - **Resolution**: Developed a context-aware command parser that distinguishes between direction commands and other actions, ensuring smooth gameplay.

## Implemented Extensions
1. **Directions as Commands**: Enables the use of direction abbreviations as standalone commands.
   - **Usage**: Type 'n' to move north, 'e' to move east, etc.
   - **Location in Code**: See `parse_command` function in `adventure.py`.

2. **Inventory Management**: Players can pick up and drop items, affecting the game state.
   - **Usage**: Use 'get [item]' to pick up an item and 'drop [item]' to leave it in the current room.
   - **Location in Code**: Refer to `get` and `drop` functions.

3. **Dynamic Help Command**: A help command that lists all currently available commands and how to use them.
   - **Usage**: Type 'help' to see available actions.
   - **Location in Code**: Implemented in the `help_command` function.



