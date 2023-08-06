from manim import *
import tokenize_all

import json
import re as regex
from abc import ABC as abstract
from urllib.request import urlopen


class Theme:
    """A theme used to syntax highlight a code block."""
    
    colors: dict[str, list[str]]
    """
    The colors of this theme represented as a dictionary. The keys of the dictionary are hexidecimal colors (such as `"#FFFFFF"`), and the values are lists of token types that should be colored with that color (such as `["keyword", "operation"]`).
    """

    def __init__(self, colors: dict[str, list[str]]):
        """
        Creates a new `Theme` with the specified `colors`. See the `colors` field for specification
        """
        self.colors = colors

    def color_for(self, token: tokenize_all.Token) -> str:
        """Returns the color for the given token as specified by this theme, or `"#FFFFFF"` if none is specified."""
        for key, value in self.colors.items():
            if token.type in value:
                return key
        return "#FFFFFF"


OneDark = Theme(
    colors = {
        "#C678DD": ["keyword"],
        "#61AFEF": ["function"],
        "#E06C75": ["identifier"],
        "#98C379": ["string"],
        "#56B6C2": [],
        "#E5C07B": ["class name", "number"],
        GRAY_C: ["comment"]
    }
)
"""The 'One Dark' theme from the `Atom` text editor."""


language_colors = json.loads(urlopen("https://raw.githubusercontent.com/ozh/github-colors/master/colors.json").read())
"""The `JSON` object representing colors for the various languages, fetched from https://raw.githubusercontent.com/ozh/github-colors/master/colors.json. """


class ProgrammingLanguage(abstract):
    """A programming language used to render `CodeBlocks`."""

    name: str
    """The name of the programming language. The name is displayed on the title card above the code block."""

    color: str
    """
    The color of the programming language. The color is used when displaying the name in the title card above the code block. by default, the official GitHub language colors are used for supported languages, see https://github.com/ozh/github-colors/blob/master/colors.json.
    """
    
    language: tokenize_all.TokenizableLanguage
    """
    The `TokenizableLanguage` of the language. 
    """

    def __init__(self, name):
        self.name = name
        self.language = getattr(tokenize_all, name)
        self.color = language_colors[name]["color"]


class CodeBlock(VGroup):
    """
    A block of code. By default code blocks are rendered as `MarkupText` objects with `BackgroundRectangles` behind them. Furthermore, a title with the name and color of the language is rendered above the code block on the left-hand side. Syntax highlighting is done using `TextMates` by extracting `.tmLanguage.json` files from `microsoft/vscode`. See https://github.com/microsoft/vscode/tree/main/extensions.
    """

    code: MarkupText
    """The primary `MarkupText` object that makes up the code block. Equivalent to indexing at `[1]`."""

    title: MarkupText
    """
    The title `MarkupText` object that makes up the langauge name title at the top of the code block. Equivalent to indexing at `[3]
    """

    code_background: BackgroundRectangle
    """The `BackgroundRectangle` for the code block markup object. Equivalent to indexing at `[0]`."""

    title_background: BackgroundRectangle
    """
    The `BackgroundRectangle` for the `title` object that lists the language name above the code block. Equivalent to indexing at `[2]`.
    """

    def __init__(
            self, 
            text: str, 
            language: ProgrammingLanguage, 
            theme: Theme = OneDark,
            font: str = "consolas",
            **kwargs: object
        ):
        """
        Creates a new `CodeBlock`.

        ### Parameters
        - `text [str]`:
            - The source code to render.
        - `language [ProgrammingLanguage]`:
            - The programming language to use when rendering the code. The language determines the text and color of the title of the code block, as well as the syntax highlighting of the code block.
        - `theme [Theme]`:
            - The theme to highlight the code in. `OneDark` by default.
        - `font [str]`: 
            - The font to render the code in. `Consolas` by default.
        - `**kwargs [Any]`:
            - Additional arguments passed to `VGroup`.
        """

        lines = text.split("\n")
        finished = []
        for line in lines:
            tokens = language.language.tokenize(line)
            for token in tokens:
                if token.type == "whitespace": finished.append(token.value)
                else: finished.append('<span foreground="' + theme.color_for(token = token) + '">' + token.value + '</span>')
            finished.append("\r")
        for line in finished: print(line)
        finished_text = "".join(finished)
        finished_text = regex.sub("&", "&amp;", finished_text)

        markup = MarkupText(f'<span font="{font}">' + finished_text + '</span>', z_index = 3).scale(0.4)
        background_rect = BackgroundRectangle(
            markup, 
            color = "#282C34", 
            buff = 0.2, 
            fill_opacity = 1
        )

        lang_name = MarkupText(
            f'<span font="{font}">{language.name}</span>',
             z_index = 3
        ).next_to(background_rect, UP).set_color(language.color)
        lang_name.scale(0.3, about_point=lang_name.get_corner(DOWN + LEFT))

        lang_background = BackgroundRectangle(lang_name, color="#282C34", buff=0.15, fill_opacity=1)
        pos = background_rect.get_corner(UP + LEFT) + np.array([lang_background.width/2, lang_background.height/2 - 0.005, 0])

        VGroup(lang_name, lang_background).move_to(pos)
        super().__init__(background_rect, markup, lang_background, lang_name, **kwargs)

        self.code = markup
        self.title = lang_name
        self.code_background = background_rect
        self.title_background = lang_background

    def create(self, run_time: float = 1) -> tuple[FadeIn, AddTextLetterByLetter, FadeIn, AddTextLetterByLetter]:
        """
        Return a tuple of animations for creating the code block. Use such as:\n
        ```
        python = CodeBlock('print("Hello World!")', language = Python)
        self.play(*python.create())
        ```
        By default the animation will `FadeIn` the `background` and `title_background`, and `AddTextLetterByLetter` the `code` and `title`. 
        """
        return (
            FadeIn(self.code_background, run_time = run_time), 
            AddTextLetterByLetter(self.code, run_time = run_time), 
            FadeIn(self.title_background, run_time = run_time), 
            AddTextLetterByLetter(self.title, run_time = run_time)
        )

    def uncreate(self, run_time: float = 1):
        """
        Return a tuple of animations for uncreating the code block. Use such as:
        ```
        python = CodeBlock('print("Hello World!")', language = Python)
        self.play(*python.uncreate())
        ```
        By default the animation will `FadeOut` the `background` and `title_background`, and `Uncreate` the `code` and `title`. 
        """
        return (
            FadeOut(self.code_background, run_time = run_time), 
            Uncreate(self.code, run_time = run_time), 
            FadeOut(self.title_background, run_time = run_time), 
            Uncreate(self.title, run_time = run_time)
        )


C = ProgrammingLanguage("C")
"""The `C` programming language."""

Java = ProgrammingLanguage("Java")
"""
The `Java` programming language, used to render `Java` code in `CodeBlocks`:

```python
java = CodeBlock(
    \"\"\"
    public class Main {
        public static void main(String[] args) {
            System.out.println("Hello world");
        }
    }
    \"\"\",
    language = Java
)
self.add(java)
```
Outputs:
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world");
    }
}
```
"""

Python = ProgrammingLanguage("Python")
"""The `Python` programming language."""
TypeScript = ProgrammingLanguage("TypeScript")
"""The `TypeScript` programming language."""
