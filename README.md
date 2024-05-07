# Translatify

Translatify is a Python package for translating text into various languages making use of google translate.

## Installation

You can install Translatify using pip:

```bash
pip install git+https://github.com/reddyyateesh/Translatify.git
```

## Example Usage
- Synchronous Version
```python
from Translatify import translate

translated_text: str = translator("Text_To_Translate", "hi", "en")

print(f"Translated Text: {translated_text}")
```

- Asynchronous Version
```python
import asyncio
from Translatify import async_translate

async def main():
    translated_text: str = await async_translator("Text_To_Translate", "hi", "en")

    print(f"Translated Text: {translated_text}")

asyncio.run(main())
```

## Documentation
For more detailed information and usage examples, please refer to the official [documentation](https://github.com/reddyyateesh/Translatify/blob/main/README.md).

## Contributing
Contributions are welcome! Please read the [contributing guidelines](#) before making any changes.

## License
This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/reddyyateesh/Translatify/blob/main/LICENSE) file for details.
