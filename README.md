# Markdown to HTML

## Description:

A Python package, designed to convert the Github mark down syntax to HTML code.

## Supporting Features
  * headings 
  * text styling: Bold, Italic, Strikethrough, Bold and italic
  * unordered and ordered lists
  * paragraphs
  * Multiple and Single line Code Blocks
  * Setext for <*h1*> and <*h2*> Tags
  * horizontal rule <*hr*> tag
  * Link text (Hyperlinks)
  * Image links
  * inline code
  * Web links (example: https://www.google.com)
  * accepts html tags <*img*> inside a <*p*> tag 

*Note: Additional support in progress

## Install

  ```
  python3 -m pip install markdown-to-html

  ```
## Usage
  ```

  >>> from markdown2html import md
  >>> md.markdown("**Hi**")
  '\n<p><strong>Hi</strong></p>\n'
  
  ```
  Command Line Interface
  
  ```
  $ md -h
  usage: Input a file [-h] [-f F]

  optional arguments:
    -h, --help  show this help message and exit
    -f F
  ```
  
  ```
  $ md -f sample.md > output.html
  ```
  
