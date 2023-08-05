# terraria PC player API

API for reading and modifying PC terraria player files.

## Examples

Change player max life to 300
```python
>>> import terraria_pc_player_api
>>> player = terraria_pc_player_api.TerrariaPCPlayer("PLAYER1.PLR")
>>> player.max_life = 300
>>> player.write_to_file("PLAYER1.PLR")
```

Set 999 dirt items to first inventory slot
```python
>>> import terraria_pc_player_api
>>> player = terraria_pc_player_api.TerrariaPCPlayer("PLAYER1.PLR")
>>> player.inventory[0][0] = terraria_pc_player_api.Item(2, 999, 0)
>>> player.write_to_file("PLAYER1.PLR")
```

Read player name
```python
>>> import terraria_pc_player_api
>>> terraria_pc_player_api.TerrariaPCPlayer("PLAYER1.PLR").name
'test_plr'
```

## Dependencies

* [bitarray](https://github.com/ilanschnell/bitarray)
* [binary-rw](https://gitlab.com/fkwilczek/binary-rw)
* [pycryptodome](https://github.com/Legrandin/pycryptodome/)
* [terraria-pc-apis-ids](https://gitlab.com/terraria-converters/terraria-pc-apis-ids)
* [terraria-apis-objects](https://gitlab.com/terraria-converters/terraria-apis-objects)

## Installation
```
pip install terraria-pc-player-api
```

## License

[GPL v3](LICENSE) © Filip K.
