Status: published
Date: 2025-07-06 08:55:45
Modified: 2025-07-06 13:19:23
Author: Benjamin Du
Slug: tips-on-google-gemini-cli
Title: Tips on Google Gemini CLI
Category: Computer Science
Tags: Computer Science, programming, Google, Gemini, CLI, AI, LLM

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**




## Tips & Traps

1. Gemini CLI is extremely useful as it doesn't requires your favorite IDE to have integration with LLM tools.
    You can use whichever IDE you like.
    What you need is just a terminal.

2. You can do concurrent tasks by opening multiple Gemini CLI (in a multiplexing tool, say Zellij).  

3. You can pipe output of another command into Gemini.
    Below is such an example.

    ```
    git diff --cached | gemini -p "Generate a conventional commits message based on this diff. Output only the message."
    ```

3. Gemini CLI allows you run shell commands directly by prefixing it with an exclamation mark (!)
    similar to IPython.
    
4. Use `/help` for more information on Gemini CLI.

## References

- [The Gemini CLI turns me into an unstoppable coding beast](https://www.youtube.com/watch?v=YAy7kd5Nqm0)

- [Google Gemini CLI: AI in Your Terminal (Windows • Linux • macOS)](https://www.youtube.com/watch?v=xqvprnPocHs)

